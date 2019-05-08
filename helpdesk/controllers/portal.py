# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import OrderedDict
from operator import itemgetter

from odoo import http, _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem

from odoo.osv.expression import OR


class CustomerPortal(CustomerPortal):

    MANDATORY_HELPDESK_FIELDS = ["name", "ticket_subject", "ticket_detail"]

    def _prepare_portal_layout_values(self):
        values = super(CustomerPortal, self)._prepare_portal_layout_values()
        values['helpdesk_count'] = request.env['helpdesk.ticket'].sudo().search_count([('partner_id.id', '=', request.env.user.partner_id.id)])
        return values

    # ------------------------------------------------------------
    # My Tickets
    # ------------------------------------------------------------
    def _helpdesk_get_page_view_values(self, helpdesk, access_token, **kwargs):
        values = {
            'page_name': 'helpdesk',
            'helpdesk': helpdesk,
        }
        return self._get_page_view_values(helpdesk, access_token, values, 'my_helpdesk_history', False, **kwargs)

    @http.route(['/my/helpdesk', '/my/helpdesk/page/<int:page>'], type='http', auth="public", website=True)
    def portal_my_helpdesk(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        Helpdesk = request.env['helpdesk.ticket'].sudo()
        domain = [('partner_id.id', '=', request.env.user.partner_id.id)]

        searchbar_sortings = {
            'date': {'label': _('Newest'), 'order': 'create_date desc'},
            'name': {'label': _('Name'), 'order': 'name'},
        }
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']

        # archive groups - Default Group By 'create_date'
        #archive_groups = self._get_archive_groups('helpdesk.ticket', domain)
        if date_begin and date_end:
            domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]
        # helpdesk count
        helpdesk_count = Helpdesk.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/helpdesk",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=helpdesk_count,
            page=page,
            step=self._items_per_page
        )

        # content according to pager and archive selected
        tickets = Helpdesk.search(domain, order=order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_helpdesk_history'] = tickets.ids[:100]

        values.update({
            'date': date_begin,
            'date_end': date_end,
            'tickets': tickets,
            'page_name': 'helpdesk',
            #'archive_groups': archive_groups,
            'default_url': '/my/helpdesk',
            'pager': pager,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby
        })
        return request.render("helpdesk.portal_my_helpdesk", values)

    @http.route(['/my/helpdesk/<int:ticket_id>'], type='http', auth="public", website=True)
    def portal_my_ticket(self, ticket_id=None, access_token=None, **kw):
        try:
            helpdesk_sudo = self._ticket_check_access('helpdesk.ticket', ticket_id, access_token).sudo()
        except (AccessError, MissingError):
            return request.redirect('/my')

        values = self._helpdesk_get_page_view_values(helpdesk_sudo, access_token, **kw)
        return request.render("helpdesk.portal_my_ticket", values)

    def _ticket_check_access(self, model_name, document_id, access_token=None):
        document_search = request.env[model_name].sudo().search([('id', '=', document_id), ('partner_id.id', '=', request.env.user.partner_id.id)])
        document = request.env[model_name].sudo().browse([document_id])
        document_sudo = document.sudo().exists()
        if not document_sudo or not document_search:
            raise MissingError("This document does not exist.")
        try:
            document.check_access_rights('read')
            document.check_access_rule('read')
        except AccessError:
            if not access_token or not consteq(document_sudo.access_token, access_token):
                raise
        return document_sudo

    # ------------------------------------------------------------
    # New Tickets
    # ------------------------------------------------------------
    @http.route(['/my/helpdesk/new'], type='http', auth="public", website=True)
    def portal_new_ticket(self, redirect=None, **post):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        ticket_subject = post.get('ticket_subject')
        ticket_detail = post.get('ticket_detail')
        values.update({
            'error': {},
            'error_message': [],
        })

        if post:
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            values.update(post)
            if not error:
                values = {key: post[key] for key in self.MANDATORY_HELPDESK_FIELDS}
                if redirect:
                    return request.redirect(redirect)
                return request.redirect('/my/helpdesk')

        values.update({
            'partner': partner,
            'redirect': redirect,
            'ticket_subject': ticket_subject,
            'ticket_detail': ticket_detail,
            'page_name': 'my_new_ticket',
        })

        return request.render('helpdesk.portal_new_ticket', values)

    def details_form_validate(self, data):
        error = dict()
        error_message = []

        # Validation
        for field_name in self.MANDATORY_HELPDESK_FIELDS:
            if not data.get(field_name):
                error[field_name] = 'missing'

        # error message for empty required fields
        if [err for err in error.values() if err == 'missing']:
            error_message.append(_('Some required fields are empty.'))

        unknown = [k for k in data if k not in self.MANDATORY_HELPDESK_FIELDS]
        if unknown:
            error['common'] = 'Unknown field'
            error_message.append("Unknown field '%s'" % ','.join(unknown))

        return error, error_message

    @http.route(['/new/helpdesk'], type='http', auth="public", website=True)
    def portal_new_helpdesk(self, **post):
        partner = request.env.user.partner_id
        ticket_subject = post.get('ticket_subject')
        ticket_detail = post.get('ticket_detail')
        ticket = request.env['helpdesk.ticket'].sudo().create(
            {'name': ticket_subject,
             'description': ticket_detail,
             'partner_id': partner.id})
        return request.redirect('/my/helpdesk')

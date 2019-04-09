# Copyright 2018 Dario Lodeiros
# Copyright 2018 Angel Moya
# Copyright 2019 Espadesa Retail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class HelpdeskTeam(models.Model):

    _name = 'helpdesk.team'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    code = fields.Char(
        string='Code')
    name = fields.Char(string='Name', required=True)
    user_ids = fields.Many2many(string='Members',
                                comodel_name='res.users',
                                relation='helpdesk_team_user_rel',
                                column1='team_id',
                                column2='user_id')
    ticket_ids = fields.One2many(string='Tickets',
                                 comodel_name='helpdesk.ticket',
                                 inverse_name='team_id')
    ticket_qty = fields.Integer(string='# Tickets',
                                compute='_compute_ticket_qty',
                                store=True)

    @api.multi
    @api.depends('ticket_ids')
    def _compute_ticket_qty(self):
        for record in self:
            record.ticket_qty = len(record.ticket_ids)

    @api.multi
    def name_get(self):
        # Prefetch the fields used by the `name_get`,
        # so `browse` doesn't fetch other fields
        self.read(['name', 'code'])
        return [(record.id, '%s%s' % (
            record.code and '[%s]' % record.code or '',
            record.name)) for record in self]

    @api.model
    def _name_search(self, name, args=None, operator='ilike',
                     limit=100, name_get_uid=None):
        args = args or []
        ticket_ids = []
        if name:
            ticket_ids = self._search(
                [('code', '=', name)] + args, limit=limit,
                access_rights_uid=name_get_uid)
        if not ticket_ids:
            ticket_ids = self._search(
                [('name', operator, name)] + args, limit=limit,
                access_rights_uid=name_get_uid)
        return self.browse(ticket_ids).name_get()

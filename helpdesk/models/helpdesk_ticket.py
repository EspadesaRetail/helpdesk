# Copyright 2018 Dario Lodeiros
# Copyright 2018 Angel Moya
# Copyright 2019 Espadesa Retail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def _default_user_id(self):
        return self.env.user

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id

    code = fields.Char(
        string='Code',
        default='New')
    name = fields.Char(string='Name', required=True)
    description = fields.Text('Description')
    date_deadline = fields.Datetime('Date limit')
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Medium'),
        ('2', 'Hight'),
        ('3', 'Very Hight')], string='Priority', default='0')
    partner_id = fields.Many2one('res.partner', 'Customer')
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='Assigned to',
        default=_default_user_id)
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=_default_company_id,
        required=True)
    team_id = fields.Many2one(
        comodel_name='helpdesk.team',
        string='Team')
    stage_id = fields.Many2one(
        comodel_name='helpdesk.stage',
        group_expand='_read_group_stage_ids',
        string='Stage')
    company_id = fields.Many2one(string='Company', comodel_name='res.company',
                                 default=_default_company_id, required=True)
    user_id = fields.Many2one(string='Assigned to', comodel_name='res.users',
                              default=_default_user_id)
    cause_id = fields.Many2one(string='Cause', comodel_name='helpdesk.cause')
    decission = fields.Text(string='Decission')
    action_ids = fields.One2many('helpdesk.action',
                                 'ticket_id',
                                 'Actions')

    def assign_to_me(self):
        # aseguramos que sólo es para un registro con ensure_one()
        # toda función llamada sin decorador es @api.multi
        # self.ensure_one()
        # self.user_id = self.env.uid
        self.write({'user_id': self.env.uid})

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return stages.search([])

    @api.onchange('priority')
    def _onchange_priority(self):
        if self.priority == '3':
            self.date_deadline = fields.Datetime.now()

    @api.model
    def create(self, vals):
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'helpdesk.ticket') or _('New')
        return super(HelpdeskTicket, self).create(vals)

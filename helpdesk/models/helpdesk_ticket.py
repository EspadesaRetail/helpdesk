# Copyright 2018 Dario Lodeiros
# Copyright 2018 Angel Moya
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
        ('3', 'Very Hight')], default='0')
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
    cause = fields.Selection([
        ('0', 'Causa 0'),
        ('1', 'Causa 1'),
        ('2', 'Causa 2'),
        ('3', 'Causa 3')])
    decision = fields.Text('Decision Adopted')
    # action_ids = fields.One2many(
    #     comodel_name='helpdesk.action',
    #     inverse_name='action_id',
    #     string='Actions')
    action_ids = fields.Many2many(
        "helpdesk.action",
        String="Action"
    )

    def assign_to_me(self):
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

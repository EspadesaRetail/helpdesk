# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    helpdesk_team_ids = fields.Many2many(
        comodel_name='helpdesk.team',
        relation='helpdesk_team_user_rel',
        column1='user_id',
        column2='team_id',
        string='Helpdesk Teams')

# Copyright 2018 Angel Moya
# Copyright 2019 Espadesa Retail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class InheritedResUsers(models.Model):

    _inherit = 'res.users'

    helpdesk_team_ids = fields.Many2many(string='Member of Helpdesk Teams',
                                         comodel_name='helpdesk.team',
                                         relation='helpdesk_team_user_rel',
                                         column1='user_id',
                                         column2='team_id')

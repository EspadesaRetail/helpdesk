# Copyright 2018 Angel Moya
# Copyright 2019 Espadesa Retail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HelpdeskStage(models.Model):

    _name = 'helpdesk.stage'
    _description = 'Helpdesk Stage'

    name = fields.Char(string='Name', required=True)

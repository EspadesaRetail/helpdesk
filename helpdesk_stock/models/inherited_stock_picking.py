# Copyright 2018 Angel Moya
# Copyright 2019 Espadesa Retail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class InheritedStockPicking(models.Model):

    _inherit = 'stock.picking'

    ticket_id = fields.Many2one(string='Helpdesk ticket',
                                comodel_name='helpdesk.ticket')

# Copyright 2018 Angel Moya
# Copyright 2019 Espadesa Retail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class InheritedHelpdeskTicket(models.Model):

    _inherit = 'helpdesk.ticket'

    picking_ids = fields.One2many(string='Pickings',
                                  comodel_name='stock.picking',
                                  inverse_name='ticket_id')

# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    stock_picking_ids = fields.One2many(
        string="Stock Picking",
        comodel_name="stock.picking",
        inverse_name="ticket_id"
    )
    # TODO: Añadir el campo o2m de albaranes y en el albarán hay que añadir un
    # m2o a ticket
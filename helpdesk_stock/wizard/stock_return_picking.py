# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class StockReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    ticket_id = fields.Many2one(
        string="Ticket",
        comodel_name="helpdesk.ticket")

    # TODO: Heredar funcion de creacion de devolucion

    def _create_returns(self):
        res = super(
            StockReturnPicking, self)._create_returns()
        # import pdb; pdb.set_trace()
        # guardamos el valor del id del ticket en una variable
        ticket = self.ticket_id.id
        # import pdb; pdb.set_trace()
        # sacamos el objeto del picking que estamos creando y le damos valor
        # \l
        stock_picking = self.env['stock.picking']
        # Cogemos el record (dato) que queremos coger
        # SELECT * FROM stock.picking WHERE id = 23
        picking_return = stock_picking.browse(res[0])
        # escribimos sobre el dato que hemos cogido
        # update stock_picking set ticket_id = 2 WHERE id = 23;
        picking_return.write({"ticket_id": ticket})
        return res[0], res[1]
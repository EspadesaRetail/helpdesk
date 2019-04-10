# Copyright 2019 Espadesa Retail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class InheritedStockReturnPicking(models.TransientModel):
    _inherit = "stock.return.picking"

    ticket_id = fields.Many2one(string='Helpdesk ticket',
                                comodel_name='helpdesk.ticket')

    def create_returns(self):
        res = super(InheritedStockReturnPicking, self).create_returns()
        if self.ticket_id:
            self.env['stock.picking'].browse(res['res_id']).write(
                {'ticket_id': self.ticket_id.id}
            )
        return res

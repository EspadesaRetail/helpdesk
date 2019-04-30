# Copyright 2019 Pedro Montagud
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _
import datetime

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    all_included = fields.Boolean(
        string="All included",
        default=False,
    )

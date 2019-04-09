# Copyright 2019 Espadesa Retail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class HelpdeskCause(models.Model):

    _name = 'helpdesk.cause'

    name = fields.Char(string='Name', required=True)

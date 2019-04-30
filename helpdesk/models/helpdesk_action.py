# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class HelpdeskAction(models.Model):
    _name = 'helpdesk.action'
    _description = 'Helpdesk Action'

    name = fields.Char()


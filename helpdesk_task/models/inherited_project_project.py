# Copyright 2018 EspadesaRetail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models, _


class InheritedProjectProject(models.Model):

    _inherit = 'project.project'

    ticket_ids = fields.One2many(
        comodel_name='helpdesk.ticket',
        inverse_name='project_id',
        string='Tickets')

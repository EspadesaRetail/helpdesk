# Copyright 2018 EspadesaRetail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class InheritedHelpdeskTicket(models.Model):

    _inherit = 'helpdesk.ticket'

    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project')
    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task')
    planned_hours = fields.Float(
        "Planned Hours",
        related='task_id.planned_hours',
        readonly=True)

    @api.onchange('project_id')
    def _onchange_project_id(self):
        res = {'domain': {'task_id':[]}}
        if self.project_id:
            res['domain']['task_id'] = [('project_id', '=', self.project_id.id)]
        return res

    @api.onchange('task_id')
    def _onchange_task_id(self):
        if self.task_id:
            self.project_id = self.task_id.project_id

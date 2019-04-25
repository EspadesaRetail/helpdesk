# Copyright 2018 EspadesaRetail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class InheritedHelpdeskTicket(models.Model):

    _inherit = 'helpdesk.ticket'

    project_id = fields.Many2one(
        comodel_name='project.project',
        domain='{"partner_id": partner_id}',
        string='Project')
    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task')
    planned_hours = fields.Float(
        string="Planned Hours",
        related='task_id.planned_hours',
        readonly=True)
    subtask_planned_hours = fields.Float(
        string="Planned Hours",
        related='task_id.subtask_planned_hours',
        readonly=True)
    analytic_account_active = fields.Boolean(
        string="Analytic Account",
        related='task_id.analytic_account_active',
        readonly=True)
    allow_timesheets = fields.Boolean(
        string="Allow Timesheets",
        related='task_id.allow_timesheets',
        readonly=True)
    subtask_count = fields.Integer(
        string="Sub-task count",
        related='task_id.subtask_count',
        readonly=False)
    remaining_hours = fields.Float(
        string="Remaining Hours",
        related='task_id.remaining_hours',
        readonly=True)
    effective_hours = fields.Float(
        string="Effective Hours",
        related='task_id.effective_hours',
        readonly=True)
    total_hours_spent = fields.Float(
        string="Total Hours",
        related='task_id.total_hours_spent',
        readonly=True)
    progress = fields.Float(
        string="Progress",
        related='task_id.progress',
        readonly=True)
    subtask_effective_hours = fields.Float(
        string="Sub-tasks Hours Spent",
        related='task_id.subtask_effective_hours',
        readonly=True)
    timesheet_ids = fields.One2many(
        related='task_id.timesheet_ids',
        string='Timesheets',
        readonly=False)
    service_policy = fields.Selection(
        related='task_id.sale_line_id.product_id.service_policy',
        string='Service Invoicing Policy',
        readonly=True)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.project_id.partner_id != self.partner_id:
            self.project_id = None
            self.task_id = None
        res = {'domain': {'project_id': [], 'task_id': []}}
        if self.partner_id:
            res['domain']['project_id'] = [
                ('partner_id', '=', self.partner_id.id)]
            res['domain']['task_id'] = [
                ('project_id.partner_id', '=', self.partner_id.id)]
        return res

    @api.onchange('project_id')
    def _onchange_project_id(self):
        if not self.partner_id:
            self.partner_id = self.project_id.partner_id
        if self.task_id and self.task_id.project_id != self.project_id:
            self.task_id = None
        res = {'domain': {'task_id': []}}
        if self.project_id:
            res['domain']['task_id'] = [
                ('project_id', '=', self.project_id.id)]
        return res

    @api.onchange('task_id')
    def _onchange_task_id(self):
        if self.task_id:
            self.project_id = self.task_id.project_id
            self.partner_id = self.task_id.project_id.partner_id

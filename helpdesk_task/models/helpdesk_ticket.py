# Copyright 2019 Pedro Montagud
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _
import datetime


class HelpdeskTicket(models.Model):

    _inherit = 'helpdesk.ticket'


    # def _compute_all_included(self):
    #     for record in self:
    #         if record.task_id and record.task_id.sale_line_id:
    #             record.all_included_computed= record.task_id.sale_line_id.product_id.all_included
    #         else:
    #             record.all_included_computed = False
    #         # task_id.sale_line_id.product_id.all_included

    @api.depends('service_policy', 'qty_delivered', 'qty_ordered')
    def _compute_allow_timesheet(self):
        for record in self:
            if record.all_included:
                record.allow_timesheet= True
            else:
                if record.service_policy and record.service_policy == 'ordered_timesheet' \
                        and record.qty_delivered >= record.qty_ordered:
                    record.allow_timesheet= False
                else:
                    record.allow_timesheet= True

    @api.depends('allow_timesheet', 'qty_delivered', 'qty_ordered')
    def _compute_alert_hours(self):
        for record in self:
            if record.allow_timesheet and record.qty_delivered >= record.qty_ordered:
                record.alert_hours = True
            else:
                record.alert_hours = False

    project_id = fields.Many2one(
        string="Project",
        comodel_name="project.project",
    )

    task_id = fields.Many2one(
        string="Task",
        comodel_name="project.task",
        domain="[('project_id','=',True)]"
    )

    planned_hours = fields.Float(
        string="Planned Hours",
        related="task_id.planned_hours",
        readonly=True,
    )

    progress = fields.Float(
        string="Progress",
        related="task_id.progress",
        readonly=False,
    )

    timesheet_ids = fields.One2many(
        string="Timesheets",
        related="task_id.timesheet_ids",
        readonly=False,
    )

    effective_hours = fields.Float(
        related="task_id.effective_hours",
        readonly=True,
    )

    total_hours_spent = fields.Float(
        related="task_id.total_hours_spent",
        readonly=True,
    )

    remaining_hours = fields.Float(
        related="task_id.remaining_hours",
        readonly=True,
    )

    # all_included_computed = fields.Boolean(
    #     # related="task_id.sale_line_id.product_id.all_included",
    #     compute='_compute_all_included',
    #     store=True,
    # )

    all_included = fields.Boolean(
        related="task_id.sale_line_id.product_id.all_included",
        store=True,
    )

    service_policy = fields.Selection(
        related="task_id.sale_line_id.product_id.service_policy",
        readonly=True,
    )

    qty_ordered = fields.Float(
        related="task_id.sale_line_id.product_uom_qty",
        readonly=True,
    )

    qty_delivered = fields.Float(
        related="task_id.sale_line_id.qty_delivered",
        readonly=True,
    )

    allow_timesheet = fields.Boolean(
        compute='_compute_allow_timesheet',
        store=True,
        readonly=True,
    )

    alert_hours = fields.Boolean(
        compute='_compute_alert_hours',
        store=True,
        readonly=True,
    )


    # ticket_qty = fields.Integer(
    #     string='',
    #     compute='_compute_tickets',
    #     store=True,
    # )


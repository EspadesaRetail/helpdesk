# Copyright 2018 EspadesaRetail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "HelpDesk Task",
    "summary":
        "Module to Support Teams",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "Alberto Calvo Bazco <alberto.calvo@beds.es> \n,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "data": [
        "views/inherited_helpdesk_ticket_views.xml",
    ],
    "application": True,
    "installable": True,
    "depends": ["base",
                "helpdesk",
                "project",
                "hr_timesheet",
                "analytic",
                "hr",
                "uom",
                "sale_timesheet",
                "product"],
}

# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Helpdesk Task Curso",
    "summary":
        "Module to relate task to tickets.",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "Pedro Montagud <pmontagud@puntsistemes.es>",
            "Tolo Torres <ttorres@puntsistemes.es>"
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "helpdesk",
        "sale",
        "project",
        "hr_timesheet",
        "sale_timesheet"
    ],
    'data':[
        "views/helpdesk_ticket.xml",
        "views/product_template.xml"
    ],
}
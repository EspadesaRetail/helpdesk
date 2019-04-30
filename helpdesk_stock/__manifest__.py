# Copyright 2019 Daniel Cano, María Alhambra, Adrián Cruz
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "HelpDesk Stock",
    "summary":
        "Module to Add Tickets to delivery note",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "Daniel Cano,"
              "María Alhambra,"
              "Adrián Cruz",
    "license": "AGPL-3",
    "data": [
        "views/stock_picking_view.xml",
        "views/helpdesk_ticket_view.xml",
        "wizard/stock_return_picking_view.xml"
    ],
    "application": True,
    "installable": True,
    "depends": ["helpdesk","stock","base", "mail"],
}

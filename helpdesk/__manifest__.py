# Copyright 2017 Dario Lodeiros - Dario Lodeiros <dariodafoz@gmail.com>
# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "HelpDesk",
    "summary":
        "Module to Support Teams",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "Dario Lodeiros Vazquez <dariodafoz@gmail.com>,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "data": [
        "data/ir_sequence_data.xml",
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_menu_views.xml",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_team_views.xml",
        "views/helpdesk_stage_views.xml",
        "views/helpdesk_action_views.xml",
        "views/res_users_views.xml",
        "views/templates.xml",
    ],
    "application": True,
    "installable": True,
    "depends": ["base", "mail"],
}

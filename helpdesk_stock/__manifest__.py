# Copyright 2018 Dario Lodeiros
# Copyright 2018 Angel Moya
# Copyright 2019 Espadesa Retail - Alberto Calvo Bazco <alberto.calvo@beds.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "HelpDesk Stock",
    "summary":
        "Module to Support Teams.",
    "version": "12.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "Alberto Calvo Bazco <alberto.calvo@beds.es>,\n"
              "Dario Lodeiros Vazquez <dariodafoz@gmail.com>,\n"
              "Angel Moya <angel.moya@pesol.es>, \n"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "data": [
        "views/inherited_helpdesk_ticket_views.xml",
        "views/inherited_stock_picking_views.xml",
        "views/inherited_stock_return_picking_views.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": True,
    "depends": [
        "base",
        "mail",
        "helpdesk",
        "stock",
    ],
}

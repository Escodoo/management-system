# Copyright 2020 Escodoo (<https://escodoo.com.br>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Equipment Calibration Control - Management System",
    "version": "12.0.1.0.0",
    "author": "Escodoo,"
              "Odoo Community Association (OCA)",
    "website": "https://github.com/oca/management-system",
    "license": "AGPL-3",
    "category": "Management System",
    "depends": ["mgmtsystem"],
    "data": [
        "security/mgmtsystem_calibration_security.xml",
        "views/calibration_certificationtype_view.xml",
        "views/calibration_certification_view.xml",
        "views/menus.xml",
    ],
    'installable': True
}

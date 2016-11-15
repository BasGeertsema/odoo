# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Ontwikkeling van module als test volgens tutorial. Manages trainings.""",

    'description': """
        Dit is de langere omschrijving van de module. Managings trainings: courses, session, registration.
    """,

    'author': "Bas Geertsema",
    'website': "http://www.bizzcloud.nl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/session_workflow.xml',
        'views/session_board.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

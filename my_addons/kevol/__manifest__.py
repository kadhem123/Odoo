# -*- coding: utf-8 -*-
{
    'name': "kevol",

    'summary': """
       Module qui organise les vols par compagnie , pilote et avion """,

    'description': """
       Module qui organise les vols par compagnie , pilote et avion
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/compagnie_views.xml',
        'views/avion_views.xml',
        'views/pilote_views.xml',
        'views/passager_views.xml',
        'views/siege_views.xml',
        'views/billet_views.xml',
        'views/vol_views.xml',
        'reports/billet_card.xml',
        'reports/report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

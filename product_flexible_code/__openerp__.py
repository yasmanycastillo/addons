# -*- coding: utf-8 -*-
{
    'name': "Product Flexible Code",

    'summary': """
    """,

    'description': """
    """,
    
    'author': 'Odoo CN Community, Jeffery <jeffery9@gmail.com>',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','sale', 'stock', 'purchase', 'mrp'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/stock_category.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
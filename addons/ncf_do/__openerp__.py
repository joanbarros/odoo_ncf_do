# -*- coding: utf-8 -*-
{
    'name': "Base NCF",

    'summary': """
        Implements NCF handling for invoicing and sales in the Dominican Republic.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Joan Barros",
    'website': "http://github.com/joanbarros/ncf_do",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting & Finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        # 'sequences.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True
}

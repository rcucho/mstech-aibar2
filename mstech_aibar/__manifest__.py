# -*- coding: utf-8 -*-

{
    'name': 'Odoo - Aibar',
    'version': '14.0.1.0.0',
    'author': 'Mstech Solutions',
    'category': 'Manufacure, Products and Sales',
    'summary': 'Módulo de personalizaciones de Aibar',
    'license': 'LGPL-3',
    'website': 'https://www.mstech.pe',
    'depends': [
        'product',
        'sale',
        'mrp',
    ],
    'data' : [
        'views/products_template_views.xml',
        'views/sale_order_view.xml',
        'views/res_partner_view.xml',
        'views/mrp_bom_view.xml',
        'report/mrp_report_bom_structure.xml',
        
    ],
    'installable': True,
    'sequence': 1,
}

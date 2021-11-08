# -*- coding: utf-8 -*-
{
    'name': "AEfood-SALE",
    'description': """Sale for Aefood company""",
    'website': "cungcaprau.weebly.com",
    'category':'Sales',
    'version': '0.1',
    'depends': [
        'mail',
        'sale',
        'hr',
    ],
    'data': [
        'views/manage_shipper_views.xml',
        'data/sequense.xml',
        'views/quanly_shipper.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
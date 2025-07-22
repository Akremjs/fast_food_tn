{
    'name': 'Fast Food Tunisien',
    'version': '1.0',
    'summary': 'Gestion des commandes et ventes pour fast-food tunisien',
    'description': 'Module Odoo pour gérer les commandes, menus, stocks et ventes d\'un fast-food tunisien.',
    'category': 'Sales',
    'author': 'AKREM KHELIFI',
    'depends': ['base', 'sale', 'stock'],
    'data': [
        'security/fast_food_security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/fast_food_order_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}


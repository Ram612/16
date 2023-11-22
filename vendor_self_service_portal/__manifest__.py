# __manifest__.py

{
    'name': 'Vendor Self Service Portal',
    'version': '16.0.1',
    'summary': 'Vendor portal for forecasts and order adjustments',
    'author': 'Ramkumar',
    'depends': ['base', 'sale', 'purchase', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'views/vendor_forecast_views.xml',
        'views/vendor_adjustment_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
}

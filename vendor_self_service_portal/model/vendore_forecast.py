# -*- coding: utf-8 -*-
#############################################################################
#    Author: Ramkumar (ram612fullstack@gmail.com)
#############################################################################

from odoo import models, fields


class VendorForecast(models.Model):
    _name = 'vendor.forecast'
    _description = 'Vendor Forecast'

    product_id = fields.Many2one('product.product', string='Product')
    expected_quantity = fields.Integer(string='Expected Quantity')
    forecast_date = fields.Date(string='Forecast Date')

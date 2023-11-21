# -*- coding: utf-8 -*-
#############################################################################
#    Author: Ramkumar (ram612fullstack@gmail.com)
#############################################################################

from odoo import models, fields


class VendorAdjustmentRequest(models.Model):
    _name = 'vendor.adjustment.request'
    _description = 'Vendor Adjustment Request'

    order_id = fields.Many2one('sale.order', string='Order Reference')
    adjustment_detail = fields.Text(string='Requested Adjustment')
    comment = fields.Text(string='Additional Comments')

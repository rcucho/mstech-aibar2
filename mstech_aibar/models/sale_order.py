# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError, Warning


class SaleOrder(models.Model) :
    _inherit = 'sale.order'

    @api.model
    def _get_mrp_lead(self, product_tmpl_id):
        return product_tmpl_id.produce_delay


class SaleOrderLine(models.Model) :
    _inherit = 'sale.order.line'
    
    mrp_lead = fields.Float('Manufacturing Time', required=True, default=0.0, help="Number of days between order confirmation and completion of manufacturing", compute='_onchange_product_id_set_mrp_lead')
    
    @api.onchange('product_id')
    def _onchange_product_id_set_mrp_lead(self):
        self.mrp_lead = self.product_id.produce_delay

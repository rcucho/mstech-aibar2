# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError, Warning


class SaleOrder(models.Model) :
    _inherit = 'sale.order'
    partner_quotation = fields.One2many(comodel_name='res.partner', inverse_name='sale_order_ids', string='Historial')
    count_part_qu=fields.Integer(string='Cotizaciones Anteriores', compute='_onchange_count_part_qu')
    
    @api.onchange('partner_quotation')
    def _onchange_count_part_qu(self):
        #if partner_quotation:
        self.count_part_qu = len(self.partner_quotation)
    
    
    @api.model
    def _get_mrp_lead(self, product_tmpl_id):
        return product_tmpl_id.produce_delay


class SaleOrderLine(models.Model) :
    _inherit = 'sale.order.line'
    
    mrp_lead = fields.Float('Manufacturing Time', required=True, default=0.0, help="Number of days between order confirmation and completion of manufacturing", compute='_onchange_product_id_set_mrp_lead')
    
    @api.onchange('product_id')
    def _onchange_product_id_set_mrp_lead(self):
        self.mrp_lead = self.product_id.produce_delay

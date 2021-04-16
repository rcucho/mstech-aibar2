# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError, Warning


class MrpBom(models.Model) :
    _inherit = 'mrp.bom'
    
    mrp_currency = fields.Many2one('res.currency', 'Moneda', compute='_compute_mrp_currency_id')
    costos_fijos = fields.Float(string="Costos Fijos", required=True, default=0.0)
    
    @api.depends('company_id')
    def _compute_mrp_currency_id(self):
        #self.mrp_currency = self.company_id.currency_id.id
        for rec in self
            rec.mrp_currency = self.company_id.currency_id.id

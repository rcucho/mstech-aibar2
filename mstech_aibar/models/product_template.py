# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError, Warning

class ProductTemplate(models.Model) :
    _inherit = 'product.template'
    
    product_example= fields.Integer(string='Prueba')

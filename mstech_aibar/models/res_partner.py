# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError, Warning


class ResPartner(models.Model) :
    inherit='res.partner'
    
    number_quotation=fields.One2many(comodel_name='sale.order', inverse_name='partner_id', string='Probando contactos')

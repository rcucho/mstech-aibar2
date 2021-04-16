# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError, Warning


class ReportBomStructure(models.AbstractModel):
    _inherit = 'report.mrp.report_bom_structure'
    
    def _get_costo_fijo(self, bom_id=False):
        bom = self.env['mrp.bom'].browse(bom_id)
        return bom.costos_fijos

    def _get_bom(self, bom_id=False, product_id=False, line_qty=False, line_id=False, level=False):
        lines = super()._get_bom(bom_id, product_id, line_qty, line_id, level)
        cos_fijo = self._get_costo_fijo(bom_id)
        lines['costos_fijos'] = cos_fijo
        #lines['total'] += cos_fijo
        return lines

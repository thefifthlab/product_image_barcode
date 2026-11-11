from odoo import fields, models

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    product_barcode = fields.Char(
        related='product_id.barcode',
        string='Barcode',
        readonly=True,
        store=False, 
    )
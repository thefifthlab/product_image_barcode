from odoo import models, fields

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_image_small = fields.Binary(
        string="Image",
        related='product_id.image_128',
        readonly=True,
        store=False,
    )

    product_barcode = fields.Char(
        string="Barcode/ISBN",
        related='product_id.barcode',
        readonly=True,
        store=False,
    )

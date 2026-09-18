from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_barcode = fields.Char(
        related='product_id.barcode',
        string="Barcode",
        readonly=True,
    )

    product_image = fields.Image(
        related='product_id.image_128',
        string="Product Image",
        readonly=True,
    )

    warehouse_id = fields.Many2one(
        related='order_id.warehouse_id',
        string='Warehouse',
        readonly=True,
    )

    qty_on_hand = fields.Float(
        related='product_id.qty_available',
        string='Avaliable Qty',
        readonly=True,
    )

    @api.onchange('product_barcode')
    def _onchange_product_barcode(self):
        if self.product_barcode:
            product = self.env['product.product'].search(
                [('barcode', '=', self.product_barcode)],
                limit=1
            )

            if product:
                self.product_id = product.id

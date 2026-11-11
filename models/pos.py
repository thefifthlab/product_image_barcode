from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_show_product_price = fields.Boolean(related='pos_config_id.show_product_price', readonly=False)
    pos_show_product_barcode = fields.Boolean(related='pos_config_id.show_product_barcode', readonly=False)

class PosConfig(models.Model):
    _inherit = 'pos.config'

    show_product_price = fields.Boolean(string="Show Price", default=True)
    show_product_barcode = fields.Boolean(string="Show Barcode", default=False)


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    barcode = fields.Char(
        related='product_id.barcode',
        string='Barcode',
        store=True
    )

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_pos_config(self):
        result = super()._loader_params_pos_config()
        result['search_params']['fields'].extend(['show_product_price', 'show_product_barcode'])
        return result

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        if 'barcode' not in result['search_params']['fields']:
            result['search_params']['fields'].append('barcode')
        return result


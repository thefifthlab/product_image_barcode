from odoo import api, models
from odoo.osv import expression

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def _name_search(
        self, name='', args=None, operator='ilike',
        limit=100, order=None
    ):
        args = args or []

        if name:
            domain = expression.AND([
                args,
                ['|', '|',
                    ('barcode', operator, name),
                    ('default_code', operator, name),
                    ('name', operator, name)
                ]
            ])

            products = self.search(
                domain,
                limit=limit,
                order=order,
            )
            return products.name_get()

        return super()._name_search(
            name=name,
            args=args,
            operator=operator,
            limit=limit,
            order=order,
        )
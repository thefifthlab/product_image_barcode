# -*- coding: utf-8 -*-
# from odoo import http


# class ProductIamgeBarcode(http.Controller):
#     @http.route('/product_image_barcode/product_image_barcode', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_image_barcode/product_image_barcode/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_image_barcode.listing', {
#             'root': '/product_image_barcode/product_image_barcode',
#             'objects': http.request.env['product_image_barcode.product_image_barcode'].search([]),
#         })

#     @http.route('/product_image_barcode/product_image_barcode/objects/<model("product_image_barcode.product_image_barcode"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_image_barcode.object', {
#             'object': obj
#         })


from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_code = fields.Char(string="Customer Code")
    vendor_code = fields.Char(string="Vendor Code")

    def generate_customer_id(self):
        for partner in self:
            if not partner.customer_code:
                sequence = self.env['ir.sequence'].next_by_code('res.partner.customer.id.unique') or '/'
                partner.customer_code = sequence

    def generate_vendor_id(self):
        for partner in self:
            if not partner.vendor_code:
                sequence = self.env['ir.sequence'].next_by_code('res.partner.vendor.id.unique') or '/'
                partner.vendor_code = sequence
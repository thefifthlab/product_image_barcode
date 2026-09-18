from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    customer_id = fields.Char(string="Customer ID")
    vendor_id = fields.Char(string="Vendor ID")

    def generate_customer_id(self):
        for partner in self:
            if not partner.customer_id:
                sequence = self.env['ir.sequence'].next_by_code('res.partner.customer.id.unique') or '/'
                partner.customer_id = sequence

    def generate_vendor_id(self):
        for partner in self:
            if not partner.vendor_id:
                sequence = self.env['ir.sequence'].next_by_code('res.partner.vendor.id.unique') or '/'
                partner.vendor_id = sequence
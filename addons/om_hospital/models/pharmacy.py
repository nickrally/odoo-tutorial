import time
from odoo import api, models, fields

class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"

    product_id = fields.Many2one('product.product')
    price_unit = fields.Float(string='Price')
    #price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    #currency_id = fields.Many2one('res.currency', related='appointment_id.currency_id')
    price_total = fields.Float(string='Subtotal', compute='_compute_price_total')

    @api.depends('price_unit', 'qty')
    def _compute_price_total(self):
        for rec in self:
            rec.price_total = rec.price_unit * rec.qty
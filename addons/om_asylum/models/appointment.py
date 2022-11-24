from odoo import api, models, fields

class HospitalAppointment(models.Model):
    _inherit=['hospital.appointment']

    must_have = fields.Html(string='Must Have')
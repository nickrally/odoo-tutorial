from odoo import api, models, fields

class HospitalAppointment(models.Model):
    _inherit=['hospital.appointment']

    must_have = fields.Html(string='Must Have')
    doctor_id = fields.Many2one('res.users',
                                 related='patient_id.primary_doctor_id',
                                 string='Doctor')
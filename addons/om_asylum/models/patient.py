from odoo import api, models, fields

class HospitalPatient(models.Model):
    _inherit=['hospital.patient']

    primary_doctor_id = fields.Many2one('res.users', string='Primary Doctor')
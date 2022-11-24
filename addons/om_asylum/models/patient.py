from odoo import api, models, fields

class HospitalPatient(models.Model):
    _inherit=['hospital.patient']

    crazy_doctor = fields.Many2one('res.users', string='Crazy Doctor')
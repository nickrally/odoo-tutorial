from datetime import date
from odoo import api, models, fields

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit=['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"
    _rec_name = 'name'

    name = fields.Char(string="Name", tracking=True)
    ref = fields.Char(string="Reference")
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
    active = fields.Boolean(string="Active", default=True)
    country = fields.Char(string="Country")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            today = date.today()
            if record.date_of_birth:
                record.age  = today.year - record.date_of_birth.year
            else:
                record.age = 0
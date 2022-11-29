import time
from odoo import api, models, fields

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit=['mail.thread','mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'apt_ref'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    gender = fields.Selection(related='patient_id.gender')
    ref = fields.Char(related='patient_id.ref', readonly=False)
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    country = fields.Char(string="Country")
    apt_ref = fields.Char(string="Apt Ref", compute="_compute_apt_ref", store=True)
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2','High'),
        ('3','Very High')], string="Priority", help='Gives sequence order when displaying a list')
    state = fields.Selection([
        ('draft','Draft'),
        ('in_consultation','In Consultation'),
        ('done','Done'),
        ('cancel','Cancelled')], string="Status", default='draft', required=True)
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')
    hide_price = fields.Boolean(string='Hide Price')

    @api.onchange('patient_id')
    def onchage_patient_id(self):
        self.country = self.patient_id.country

    @api.depends('ref','appointment_time')
    def _compute_apt_ref(self):
        for record in self:
            if record.ref and record.appointment_time:
                record.apt_ref  =  record.ref + str(int(time.mktime(record.appointment_time.timetuple())))
            else:
                record.apt_ref = '0'

    def cancel_appointment(self):
        # self.state = 'cancel'
        # ------------------------
        # for record in self:
        #     record.state = 'cancel'
        # -------------------------
        action = self.env.ref('om_hospital.action_cancel_appointment').read()[0]
        return action

    def reset_to_draft(self):
        self.state = 'draft'
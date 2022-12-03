from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    @api.model
    def default_get(self, fields):
        rec = super(CancelAppointmentWizard, self).default_get(fields)
        if self.env.context.get('active_id'):
            rec['appointment_id'] = self.env.context.get('active_id')
        return rec

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    reason = fields.Text(string="Reason")

    def action_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_(f'Cannot cancel today appointment {fields.Date.today()}'))

        print("will cancel at one point...")
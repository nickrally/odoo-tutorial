from odoo import models, fields

class Bar(models.Model):
    _name = "foo.bar"
    _description = "Foo Bar"

    name = fields.Char(string='Name')
    secret = fields.Integer(string='SecretNumber')
    kind = fields.Selection([('good','Good'),('bad','Bad'),('ugly','Ugly')], string='Kind')
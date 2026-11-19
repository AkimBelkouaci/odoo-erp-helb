from odoo import models, fields, api

class Contact(models.Model):
    _name = "openacademy.contact"
    _description = "Contact"

    name = fields.Char(required=True)
    session_ids = fields.Many2many('openacademy.session')
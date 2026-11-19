from odoo import models, fields, api

class Course(models.Model):
    _name = "openacademy.course"
    _description = "Cours"

    name = fields.Char(required=True)

    niveau = fields.Selection([
        ('junior', 'Junior'),
        ('senior', 'Senior')
    ])

    responsable_id = fields.Many2one('openacademy.contact')
    session_ids = fields.One2many('openacademy.session', 'course_id')
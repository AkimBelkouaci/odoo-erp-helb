from odoo import models, fields

class Session(models.Model):
    _name = "openacademy.session"
    _description = "Session"

    name = fields.Char(required=True)
    
    date_de_debut = fields.Date()
    date_de_fin = fields.Date()

    course_id = fields.Many2one('openacademy.course')
    professeur_id = fields.Many2one('openacademy.contact')
    niveau = fields.Selection(related='course_id.niveau')

    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('confirm', 'Confirmé'),
        ('done', 'Terminé'),
        ('cancel', 'Annulé')
    ], default='draft', readonly=True)

    def action_confirm(self):
        for record in self:
            record.state = 'confirm'
        return True

    def action_done(self):
        for record in self:
            record.state = 'done'
        return True

    def action_cancel(self):
        for record in self:
            record.state = 'cancel'
        return True

    def action_set_draft(self):
        for record in self:
            record.state = 'draft'
        return True
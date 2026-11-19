from odoo import models, fields, api

class EstateLead(models.Model):
    _name = 'estate.lead'
    _description = 'Estate Lead'

    name = fields.Char()
    phone = fields.Char()
    email = fields.Char()

    property_ids = fields.One2many('estate.property', 'lead_id')
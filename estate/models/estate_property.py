from odoo import models, fields,api

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char()
    description = fields.Text()
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([('new', 'New'),
    ('offer_received', 'Offer Received'),
     ('offer_accepted', 'Offer Accepted'), 
     ('sold', 'Sold'), ('canceled', 'Canceled')])

    tag_ids = fields.Many2many('estate.property.tag')
    lead_id = fields.Many2one('estate.lead')
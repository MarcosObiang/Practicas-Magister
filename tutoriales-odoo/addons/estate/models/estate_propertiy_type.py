
from odoo import models,fields

class PropertyType(models.Model):
    _name="property_type"
    _description="holds the type of properties available"

    partner_id= fields.Char("Compa",required =True)


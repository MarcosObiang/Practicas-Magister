
from odoo import models,fields

class PropertyType(models.Model):
    _name="property_type"
    _description="holds the type of properties available"

    property_type= fields.Char("Property type", required=True,default="Sweet Home")


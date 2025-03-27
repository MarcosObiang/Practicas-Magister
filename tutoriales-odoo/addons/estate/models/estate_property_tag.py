from odoo import models,fields

class PropertyTag(models.Model):
    _name = "property_tag"
    _description= "a tag to attach to estates"

    tag = fields.Char("tag",required=True)
from odoo import models, fields


class PropertyType(models.Model):
    _name = "property_type"
    _description = "holds the type of properties available"
    _order = "sequence"
    property_type = fields.Char("Property type", required=True, default="Sweet Home")

    sequence = fields.Integer("Sequence", default=1, help="Used to ordet by type")
    property_ids = fields.One2many(
        "test_model", "property_type_id", string="Propiedades"
    )

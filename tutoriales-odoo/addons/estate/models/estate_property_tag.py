from odoo import models, fields


class PropertyTag(models.Model):
    _name = "property_tag"
    _description = "a tag to attach to estates"
    _order = "tag"

    color = fields.Integer()

    tag = fields.Char("tag", required=True)

    _sql_constraints = [
        (
            "tag_must_be_unique",
            "UNIQUE(tag)",
            "A tag cannot be duplicated in the database",
        ),
    ]

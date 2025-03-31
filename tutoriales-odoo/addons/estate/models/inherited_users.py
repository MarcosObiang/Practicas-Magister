from odoo import fields, models


class InheritedUser(models.Model):
    _inherit = "res.users"
    property_ids = fields.One2many(
        "test_model",
        "user_id",
        string="Property Ids",
        domain=[("state", "in", ["new", "offer_received"])],
    )

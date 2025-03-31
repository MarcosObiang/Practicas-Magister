from odoo import models, fields, api


class PropertyType(models.Model):
    _name = "property_type"
    _description = "holds the type of properties available"
    _order = "sequence"
    property_type = fields.Char("Property type", required=True, default="Sweet Home")
    offer_ids = fields.One2many(
        "estate_property_offers", "property_id", string="Offers"
    )
    sequence = fields.Integer("Sequence", default=1, help="Used to ordet by type")
    property_ids = fields.One2many(
        "test_model", "property_type_id", string="Propiedades"
    )

    offer_count = fields.Integer(string="Offer count", compute="offer_counter")

    @api.depends("offer_ids")
    def offer_counter(self):
        for record in self:
            record.offer_count = len(offer_ids)

    def action_open_offers(self):
        self.ensure_one()
        return {
            "name": "Offers",
            "type": "ir.actions.act_window",
            "res_model": "estate_property_offers",
            "view_mode": "tree,form",
            "domain": [("property_id.property_type_id", "=", self.id)],
            "context": {"default_property_id": self.id},
        }

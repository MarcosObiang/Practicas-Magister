from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.tools import float_utils


class TestModel(models.Model):
    _name = "test_model"
    _description = "Test Model"

    _sql_constraints = [
        (
            "expected_price_must_be_positive",
            "CHECK(expected_price > 0)",
            "price_mut_be_greater_than_zero",
        ),
        (
            "selling_price_must_be_positive",
            "CHECK(selling_price >= 0)",
            "The selling price must not be negative",
        ),
    ]

    _order = "id desc"

    name = fields.Char("Name", required=True, translate=True)
    description = fields.Char("Description", required=True)
    postcode = fields.Char("Post code", required=True)
    date_availability = fields.Date(
        "Availability date",
        copy=False,
        default=lambda self: fields.Date.add(fields.Date.today(), months=3),
    )
    expected_price = fields.Float("Expected price", required=True)
    selling_price = fields.Float("selling price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Has Garage", default=False)
    garden = fields.Boolean("Has Garden", default=False)
    garden_area = fields.Integer("Total garden area")
    garden_orientation = fields.Selection(
        string="Orientation",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("north", "West"),
        ],
    )
    active = fields.Boolean(
        "Active",
        default=False,
    )
    state = fields.Selection(
        string="Estado",
        selection=[
            ("new", "New"),
            ("offer_recieved", "Offer Recieved"),
            ("offer_accepted", "Offer Acepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
    )
    buyer_id = fields.Many2one("res.partner", "Buyer")
    salesman_id = fields.Many2one("res.partner", "Salesman")
    property_type_id = fields.Many2one("property_type", "Property Type")
    property_tag_ids = fields.Many2many("property_tag", string="Property Tags")
    offers_ids = fields.One2many(
        "estate_property_offers", "property_id", string="Offers"
    )
    total_area = fields.Float(compute="compute_total_area")

    @api.depends("living_area")
    def compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.onchange("garden")
    def on_garden_change(self):
        if self.garden:
            if self.garden == True:
                self.garden_orientation = "north"

                self.garden_area = 10
            else:
                self.garden_area = None
                self.graden_orientation = None

    @api.constrains("selling_price")
    def _minimum_selling_price_constraint(self):
        for record in self:
            if (
                float_utils.float_compare(
                    record.selling_price,
                    record.expected_price * 0.90,
                    precision_digits=2,
                )
                < 0
            ):
                raise ValidationError(
                    "The selling price cannot be more than 10% lower than the expected price"
                )

    def cancel_offer(self):
        for record in self:
            if record.state != "sold":
                record.state = "canceled"

    def sold_to_offer(self):
        for record in self:
            if record.state != "canecled":
                record.state = "sold"

from odoo import models, fields, api
from datetime import timedelta


class EstatePropertyOffers(models.Model):
    _name = "estate_property_offers"
    _description = "Offers made for a real estate property"
    _order = "price desc"
    _sql_constraints = [
        (
            "offer_must_be_strictly_positive",
            "CHECK(price > 0)",
            "The offer price mus be greater than zero",
        ),
    ]

    price = fields.Float("Price", default=0)
    status = fields.Selection(
        string="Status",
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        noCopy=True,
    )

    partner_id = fields.Many2one("res.partner", required=True, string="Partner")
    property_id = fields.Many2one("test_model", required=True, string="Property")

    validity = fields.Integer(inverse="get_validity", default=7)
    date_deadline = fields.Date(compute="get_deadline")

    @api.depends("validity")
    def get_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + timedelta(
                    days=record.validity
                )
            else:
                record.date_deadline = fields.Datetime.now() + timedelta(
                    days=record.validity
                )

    @api.depends("date_deadline")
    def get_validity(self):
        for record in self:
            if record.create_date:
                create_date = record.create_date.date()
            else:
                create_date = fields.DateTime.now().date()

    def accept_offer(self):
        for record in self:
            record.status = "accepted"
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price

    def refuse_offer(self):
        for record in self:

            record.status = "refused"
            record.property_id.selling_price = 0

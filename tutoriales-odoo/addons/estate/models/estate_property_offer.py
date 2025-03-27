from odoo import models, fields, api
from datetime import timedelta


class EstatePropertyOffers(models.Model):
    _name = "estate_property_offers"
    _description = "Offers made for a real estate property"

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
                record.date_deadline = record.create_date + timedelta(days=record.validity)
            else:
                record.date_deadline = fields.Datetime.now() + timedelta(days=record.validity)

    @api.depends("create_date")
    def get_validity(self):
        for record in self:
            record.validity = record.date_deadline - create_date

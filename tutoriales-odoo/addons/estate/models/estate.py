
from odoo import models,fields

class Estate(models.Model):
    _name ="test_model"
    _description="Casas"

    name=fields.Char("Model name", required=True,translate=True)
    description=fields.Char("Description", required =True,translate=True)
    postcode=fields.Char("Post code", required=True)
    date_availability=fields.Date("Availability date")
    expected_price=fields.Float('Expected price', required =True)
    selling_price=fields.Float('selling price')
    bedrooms=fields.Integer('Bedrooms')
    living_area=fields.Integer('Living area')
    facades=fields.Integer('Facades')
    garage= fields.Boolean('Has Garage')
    garden= fields.Boolean('Has Garden')
    garden_area=fields.Integer('Total garden area')
    garden_orienation= fields.Selection(string='Type',selection=[('north','North'),('south','South'),('east','East'),('north','West')])


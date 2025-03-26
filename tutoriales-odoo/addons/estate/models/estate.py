
from odoo import models,fields

class TestModel(models.Model):
    _name ="test_model"
    _description="Test Model"

    name=fields.Char("Name", required=True,translate=True)
    description=fields.Char("Description", required =True)
    postcode=fields.Char("Post code", required=True)
    date_availability=fields.Date("Availability date",copy=False,default=lambda self: fields.Date.add(fields.Date.today(),months=3))
    expected_price=fields.Float('Expected price', required =True)
    selling_price=fields.Float('selling price', readonly=True,copy=False)
    bedrooms=fields.Integer('Bedrooms',default=2)
    living_area=fields.Integer('Living area')
    facades=fields.Integer('Facades')
    garage= fields.Boolean('Has Garage')
    garden= fields.Boolean('Has Garden')
    garden_area=fields.Integer('Total garden area')
    garden_orientation= fields.Selection(string='Orientation',selection=[('north','North'),('south','South'),('east','East'),('north','West')])
    active=fields.Boolean("Active",default=False,)
    state= fields.Selection(string = 'Estado', selection=[("new","New"),("offer_recieved","Offer Recieved"),("offer_accepted","Offer Acepted"),("sold","Sold"),("canceled","Canceled")])
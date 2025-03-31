from odoo import fields, models


class EstateProperty(models.Model):
    _inherit = "test_model"

    def sold_to_offer(self):
        print("**************************************************")
        print("*** ¡MÉTODO SOLD_TO_OFFER EJECUTADO!  ***")
        print("**************************************************")

        invoice_vals = {
            "partner_id": self.buyer_id.id,
            "move_type": "out_invoice",
            "invoice_line_ids": [
                (
                    0,
                    0,
                    {
                        "name": f"6% de {self.name}",
                        "quantity": 1,
                        "price_unit": self.selling_price * 0.06,
                    },
                ),
                (
                    0,
                    0,
                    {
                        "name": "Gastos administrativos",
                        "quantity": 1,
                        "price_unit": 100.00,
                    },
                ),
            ],
        }
        invoice = self.env["account.move"].create(invoice_vals)

        print(f"Factura creada: {invoice.id}")

        print(f"Factura creada: {invoice.id}")
        return super().sold_to_offer()

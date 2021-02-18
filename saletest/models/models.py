from odoo import models, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def duplicate_line(self):
        max_seq = max(line.sequence for line in self.order_id.order_line)
        self.copy({'order_id': self.order_id.id, 'sequence': max_seq + 1})

    @api.model
    def create(self, values):
        print(values)
        result = super(SaleOrderLine, self).create(values)
        return result

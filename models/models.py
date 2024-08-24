# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ./addons_odoo17/exchange_rates(models.Model):
#     _name = './addons_odoo17/exchange_rates../addons_odoo17/exchange_rates'
#     _description = './addons_odoo17/exchange_rates../addons_odoo17/exchange_rates'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


# -*- coding: utf-8 -*-
# from odoo import http


# class ./addonsOdoo17/exchangeRates(http.Controller):
#     @http.route('/./addons_odoo17/exchange_rates/./addons_odoo17/exchange_rates', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./addons_odoo17/exchange_rates/./addons_odoo17/exchange_rates/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./addons_odoo17/exchange_rates.listing', {
#             'root': '/./addons_odoo17/exchange_rates/./addons_odoo17/exchange_rates',
#             'objects': http.request.env['./addons_odoo17/exchange_rates../addons_odoo17/exchange_rates'].search([]),
#         })

#     @http.route('/./addons_odoo17/exchange_rates/./addons_odoo17/exchange_rates/objects/<model("./addons_odoo17/exchange_rates../addons_odoo17/exchange_rates"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./addons_odoo17/exchange_rates.object', {
#             'object': obj
#         })


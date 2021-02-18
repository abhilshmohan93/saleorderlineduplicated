# -*- coding: utf-8 -*-
# from odoo import http


# class Saletest(http.Controller):
#     @http.route('/saletest/saletest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/saletest/saletest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('saletest.listing', {
#             'root': '/saletest/saletest',
#             'objects': http.request.env['saletest.saletest'].search([]),
#         })

#     @http.route('/saletest/saletest/objects/<model("saletest.saletest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('saletest.object', {
#             'object': obj
#         })

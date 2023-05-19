# -*- coding: utf-8 -*-
# from odoo import http


# class Odooknowledge(http.Controller):
#     @http.route('/odooknowledge/odooknowledge/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odooknowledge/odooknowledge/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odooknowledge.listing', {
#             'root': '/odooknowledge/odooknowledge',
#             'objects': http.request.env['odooknowledge.odooknowledge'].search([]),
#         })

#     @http.route('/odooknowledge/odooknowledge/objects/<model("odooknowledge.odooknowledge"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odooknowledge.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
from odoo import http

# class Kevol(http.Controller):
#     @http.route('/kevol/kevol/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kevol/kevol/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kevol.listing', {
#             'root': '/kevol/kevol',
#             'objects': http.request.env['kevol.kevol'].search([]),
#         })

#     @http.route('/kevol/kevol/objects/<model("kevol.kevol"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kevol.object', {
#             'object': obj
#         })
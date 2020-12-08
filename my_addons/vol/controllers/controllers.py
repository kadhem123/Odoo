# -*- coding: utf-8 -*-
from odoo import http

# class Vol(http.Controller):
#     @http.route('/vol/vol/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vol/vol/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vol.listing', {
#             'root': '/vol/vol',
#             'objects': http.request.env['vol.vol'].search([]),
#         })

#     @http.route('/vol/vol/objects/<model("vol.vol"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vol.object', {
#             'object': obj
#         })
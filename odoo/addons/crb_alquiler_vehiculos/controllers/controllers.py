# -*- coding: utf-8 -*-
# from odoo import http


# class CrbAlquilerVehiculos(http.Controller):
#     @http.route('/crb_alquiler_vehiculos/crb_alquiler_vehiculos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crb_alquiler_vehiculos/crb_alquiler_vehiculos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crb_alquiler_vehiculos.listing', {
#             'root': '/crb_alquiler_vehiculos/crb_alquiler_vehiculos',
#             'objects': http.request.env['crb_alquiler_vehiculos.crb_alquiler_vehiculos'].search([]),
#         })

#     @http.route('/crb_alquiler_vehiculos/crb_alquiler_vehiculos/objects/<model("crb_alquiler_vehiculos.crb_alquiler_vehiculos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crb_alquiler_vehiculos.object', {
#             'object': obj
#         })


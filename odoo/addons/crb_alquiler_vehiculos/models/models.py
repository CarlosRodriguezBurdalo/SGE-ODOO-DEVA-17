# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class crb_alquiler_vehiculos(models.Model):
#     _name = 'crb_alquiler_vehiculos.crb_alquiler_vehiculos'
#     _description = 'crb_alquiler_vehiculos.crb_alquiler_vehiculos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


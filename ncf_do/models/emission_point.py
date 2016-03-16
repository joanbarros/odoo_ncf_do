# -*- coding: utf-8 -*-

from openerp import models, fields, api

class EmissionPoint(models.Model):
    _name = 'ncf_do.emission_point'
    code = fields.Char()
    name = fields.Char(string = "Name")
    description = fields.Char()

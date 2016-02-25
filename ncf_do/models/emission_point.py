# -*- coding: utf-8 -*-

from openerp import models, fields, api

class EmissionPoint(models.Model):
    _name = 'ncf_do.emission_point'
    name = fields.Char(string = "Name")
    value = fields.Char()

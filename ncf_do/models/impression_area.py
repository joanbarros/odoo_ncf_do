# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ImpressionArea(models.Model):
    _name = 'ncf_do.impression_area'
    name = fields.Char(string = "Name")
    value = fields.Char()

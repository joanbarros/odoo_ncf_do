# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ImpressionArea(models.Model):
    _name = 'ncf_do.impression_area'
    code = fields.Char()
    name = fields.Char(string = "Name")
    description = fields.Char()
    

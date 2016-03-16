# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Series(models.Model):
    _name = 'ncf_do.series'
    code = fields.Char(string = "Name")
    name = fields.Char(string = "Code")
    description = fields.Char()

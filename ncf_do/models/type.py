# -*- coding: utf-8 -*-

from openerp import models, fields, api

class NCFType(models.Model):
    _name = 'ncf_do.type'
    name = fields.Char(string = "Name")
    value = fields.Char()

# -*- coding: utf-8 -*-

from openerp import models, fields, api

class NCFType(models.Model):
    _name = 'ncf_do.type'
    code = fields.Char()
    name = fields.Char(string = "Name")
    description = fields.Char()

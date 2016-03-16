# -*- coding: utf-8 -*-

from openerp import models, fields, api

class BusinessDivision(models.Model):
    _name = 'ncf_do.business_division'
    code = fields.Char()
    name = fields.Char(string = "Name")
    description = fields.Char()

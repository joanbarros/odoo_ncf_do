# -*- coding: utf-8 -*-

from openerp import models, fields, api

class BusinessDivision(models.Model):
    _name = 'ncf_do.business_division'
    name = fields.Char(string = "Name")
    value = fields.Char()

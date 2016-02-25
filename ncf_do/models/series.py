# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Series(models.Model):
    _name = 'ncf_do.series'
    # name = fields.Char()
    name = fields.Char(string = "Name")
    dn = fields.Char()
    pe = fields.Char()
    ai = fields.Char()
    tcf = fields.Char()
    sequencia = fields.Char()

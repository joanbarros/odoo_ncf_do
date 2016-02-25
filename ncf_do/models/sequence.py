# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Sequence(models.Model):
    _name = 'ncf_do.sequence'
    name = fields.Char()
    value = fields.Char()

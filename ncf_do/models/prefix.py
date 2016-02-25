# -*- coding: utf-8 -*-

from openerp import models, fields, api

class NCFPrefix(models.Model):
    _name = 'ncf_do.prefix'
    name = fields.Char()
    series = fields.Many2one('ncf_do.series', ondelete='set null')
    business_division = fields.Many2one('ncf_do.business_division', ondelete='set null')
    emission_point = fields.Many2one('ncf_do.emission_point', ondelete='set null')
    impression_area = fields.Many2one('ncf_do.impression_area', ondelete='set null')

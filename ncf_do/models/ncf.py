# -*- coding: utf-8 -*-

from openerp import models, fields, api

class NCF(models.Model):
    _name = 'ncf_do.ncf'
    name = fields.Char()
    description = fields.Char()
    prefix = fields.Char(compute='compute_prefix')

    series = fields.Many2one('ncf_do.series', ondelete='set null')
    business_division = fields.Many2one('ncf_do.business_division', ondelete='set null')
    emission_point = fields.Many2one('ncf_do.emission_point', ondelete='set null')
    impression_area = fields.Many2one('ncf_do.impression_area', ondelete='set null')

    def compute_prefix(self):
        if (self.series.code == False or self.business_division.code == False or self.emission_point.code == False or self.impression_area.code == False):
            self.prefix = 'Not Available'
        else:
            self.prefix = str(self.series.code) \
                       + str(self.business_division.code) \
                        + str(self.emission_point.code) \
                        + str(self.impression_area.code)

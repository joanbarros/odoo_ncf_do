# -*- coding: utf-8 -*-

from openerp import models, fields, api

class POSConfigIntegration(models.Model):
    _inherit = 'pos.config'

    ncf = fields.Many2one('ncf_do.ncf')

# -*- coding: utf-8 -*-

from openerp import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class POSOrderIntegration(models.Model):
    _inherit = 'pos.order'

    ncf = fields.Char()

    def create(self, cr, uid, values, context=None):
        _logger.info('========== creating order =============')
        return super(POSOrderIntegration, self).create(cr, uid, values, context=context)

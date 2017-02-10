# -*- coding: utf-8 -*-

from openerp import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class POSOrderIntegration(models.Model):
    _inherit = 'pos.order'

    ncf = fields.Char()

    @api.model
    def create(self, values):
    #def create(self, cr, uid, values, context=None):
        _logger.info('========== creating order =============')

        sup = super(POSOrderIntegration, self).create(values)

        sessionModel = self.env['pos.session']

        session = sessionModel.browse(values['session_id'])[0]
        config = session.config_id
        ncf = config.ncf

        new_values = {}

        new_values['ncf'] = ncf.next(12);

        sup.write(new_values)

        return sup

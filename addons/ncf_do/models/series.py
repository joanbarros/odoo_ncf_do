# -*- coding: utf-8 -*-

from openerp import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class Series(models.Model):
    _name = 'ncf_do.series'
    code = fields.Char()
    name = fields.Char()
    description = fields.Char()

    # Identifiers for Drop Downs
    _rec_name='identifier'
    identifier = fields.Char(compute='_gen_rec')
    def _gen_rec(self):
        for s in self:
            _logger.error('self count: %r', len(s))
            name = s.name if s.name != False else ''
            code = s.code if s.code != False else ''
            s.identifier = name + ' [' + code + ']'

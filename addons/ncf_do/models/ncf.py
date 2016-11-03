# -*- coding: utf-8 -*-

from openerp import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class NCF(models.Model):
    _name = 'ncf_do.ncf'
    name = fields.Char()
    description = fields.Char()
    prefix = fields.Char(compute='compute_prefix')

    series = fields.Many2one('ncf_do.series', ondelete='set null')
    business_division = fields.Many2one('ncf_do.business_division', ondelete='set null')
    emission_point = fields.Many2one('ncf_do.emission_point', ondelete='set null')
    impression_area = fields.Many2one('ncf_do.impression_area', ondelete='set null')

    # sequences
    seq_type1 = fields.Many2one('ir.sequence')
    seq_type2 = fields.Many2one('ir.sequence')
    seq_type3 = fields.Many2one('ir.sequence')
    seq_type4 = fields.Many2one('ir.sequence')
    seq_type11 = fields.Many2one('ir.sequence')
    seq_type12 = fields.Many2one('ir.sequence')
    seq_type13 = fields.Many2one('ir.sequence')
    seq_type14 = fields.Many2one('ir.sequence')
    seq_type15 = fields.Many2one('ir.sequence')

    def _create_sequence(self, type, values):
        # self.compute_prefix()
        prefix = self.prefix
        # prefix = '|test_prefix|'
        _logger.info('prefix ===> ' + str(self.prefix))


        if int(type) < 10:
            prefix += '0'
            prefix += str(type)
        else:
            prefix += str(type)

        values['seq_type'+str(type)] = self.env['ir.sequence'].create({'name': prefix, 'code': prefix, 'prefix': prefix})[0].id
        _logger.info('added value [' + str(values['seq_type'+str(type)]) + '] to the sequence [' + 'seq_type'+str(type) + ']')


    def compute_prefix(self):
        for ncf in self:
            if (ncf.series.code == False or ncf.business_division.code == False or ncf.emission_point.code == False or ncf.impression_area.code == False):
                ncf.prefix = False
            else:
                ncf.prefix = str(ncf.series.code) \
                           + str(ncf.business_division.code) \
                            + str(ncf.emission_point.code) \
                            + str(ncf.impression_area.code)

    @api.model
    def create(self, values):#, cr, uid, values, context=None):
        sup = super(NCF, self).create(values)[0]
        _logger.info('dir ==> ' + str(dir(self)))
        # _logger.info('self.series ==> ' + new_ncf.series)
        # _logger.info('cr ==> ' + str(cr))
        _logger.info('sup ==> ' + str(sup))
        # _logger.info('uid ==> ' + str(uid))
        _logger.info('values ==> ' + str(values))
        # _logger.info('new_ncf ==> ' + new_ncf._ids)

        new_vals = {}

        sup._create_sequence(1, new_vals)
        sup._create_sequence(2, new_vals)
        sup._create_sequence(3, new_vals)
        sup._create_sequence(4, new_vals)
        sup._create_sequence(11, new_vals)
        sup._create_sequence(12, new_vals)
        sup._create_sequence(13, new_vals)
        sup._create_sequence(14, new_vals)
        sup._create_sequence(15, new_vals)

        _logger.info('new_vals ==> ' + str(new_vals))

        sup.write(new_vals)

        return sup

    def next(self, type):
        pass

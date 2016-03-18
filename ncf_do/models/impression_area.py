# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ImpressionArea(models.Model):
    _name = 'ncf_do.impression_area'
    code = fields.Char()
    name = fields.Char(string = "Name")
    description = fields.Char()

    # Identifiers for Drop Downs
    _rec_name='identifier'
    identifier = fields.Char(compute='_gen_rec', hidden=True)
    def _gen_rec(self):
        name = self.name if self.name != False else ''
        code = self.code if self.code != False else ''
        self.identifier = name + ' [' + code + ']'

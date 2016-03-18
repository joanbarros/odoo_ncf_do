# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Series(models.Model):
    _name = 'ncf_do.series'
    _rec_name='code'
    code = fields.Char(string = "Name")
    name = fields.Char(string = "Code")
    description = fields.Char()

    # Identifiers for Drop Downs
    _rec_name='identifier'
    identifier = fields.Char(compute='_gen_rec', hidden=True)
    def _gen_rec(self):
        name = self.name if self.name != False else ''
        code = self.code if self.code != False else ''
        self.identifier = name + ' [' + code + ']'

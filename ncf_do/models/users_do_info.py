# -*- coding: utf-8 -*-

# This is temporarily here but it will probably need to be moved to it's own module

from openerp import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class DO_UserInfo(models.Model):
    #_name = 'res.partner'
    _inherit = 'res.partner'

    rnc = fields.Char()

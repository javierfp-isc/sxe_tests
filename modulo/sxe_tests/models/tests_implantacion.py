# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class TestsImplantacion(models.Model):
    _name = 'tests.implantacion'
    _description = 'Tests de Implantación'

    @api.model
    def test_modulo_instalado(self, params):
        #Ventas: sale_management
        #CRM: crm
        #Website: website
        #ETC...
        nombreModulo = params['modulo']
        num = self.env['ir.module.module'].search(['&',('name','ilike',nombreModulo),('state','=','installed')], count=True)
        
        if num > 0:
            _logger.info("Módulo: %s instalado" % (nombreModulo))
            return True

        return False
    

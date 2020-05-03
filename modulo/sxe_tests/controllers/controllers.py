# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)

class SxeTests(http.Controller):    
    @http.route('/sxe_tests/implantacion/', auth='public')
    def call(self, **kw):
        try:
            if not 'login_success' in request.params:
                request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
                request.params['login_success'] = True
            #Tomo método a invocar de la request
            metodo = request.params['metodo']
            #Recuperamos el modelo
            modelo = request.env['tests.implantacion']
            #Invoco el método del modelo
            res = getattr(modelo, metodo)(request.params)

            assert res, "Test no pasado"

            return "EXITO"
        except AssertionError:
            return "FALLO"
        except:
            return "ERROR"
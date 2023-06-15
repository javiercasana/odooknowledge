# -*- coding: utf-8 -*-


from odoo import http, models
from odoo.http import request


class okwfunctionejemplo(http.Controller):
    @http.route("/okw/function", type='http', auth="public", website=True)
    def website_okw_function(self, **kwargs):
        Function = request.env["odooknowledge.okw.function"].sudo()
        f = Function.search([])
        values = {
            'variable1': "variable1",
            'variable2': 100,
            'function_ids': f,
        }
        return request.render('odooknowledge.website_function', values)

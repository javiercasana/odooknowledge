
# -*- coding: utf-8 -*-


from odoo import http, models
from odoo.http import request


class okwfunction_form(http.Controller):
    @http.route("/okw/function/form", type='http',methods=['GET'], auth="public", website=True)
    def website_okw_function(self,id,**kwargs):
        function_form = request.env["odooknowledge.okw.function"].sudo()
        identificador = function_form.search([("id","=",id )])
        values = {
            'function_id': identificador,
        }
        return request.render('odooknowledge.website_function_list_form',values)

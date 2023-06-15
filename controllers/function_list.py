
# -*- coding: utf-8 -*-


from odoo import http, models
from odoo.http import request


class okwfunction_list(http.Controller):
    @http.route("/okw/function/list", type='http', auth="public", website=True)
    def website_okw_function(self, **kwargs):
        Function = request.env["odooknowledge.okw.function"].sudo()
       
        parents = []
        functions = []

        for f in Function.search([], order='parent_id desc'):
            if f.parent_id:
                functions.append(f)
            else:
                parents.append(f)

        values = {
            'function_ids': functions,
            'parent_ids' : parents,

        }


  

        return request.render('odooknowledge.website_function_list', values)



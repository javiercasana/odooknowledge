
# -*- coding: utf-8 -*-


from odoo import http, models
from odoo.http import request


class okfunction_edit(http.Controller):
    @http.route("/okw/function/edit", type='http',methods=['GET'], auth="public", website=True)
    def website_okw_edit(self,**kwargs):
        return request.render('odooknowledge.website_function_list_edit',{})

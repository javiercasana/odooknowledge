# -*- coding: utf-8 -*-


from odoo import http, models
from odoo.http import request


class okwmodelejemplo1(http.Controller):
    @http.route("/okw/model", type='http', auth="public", website=True)
    def website_okw_model(self, **kwargs):
        model = request.env["odooknowledge.okw.model"].sudo()
        f = model.search([])
        values = {
            'model_ids': f,
        }
        return request.render('odooknowledge.website_model', values)

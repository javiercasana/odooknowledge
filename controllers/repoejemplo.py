# -*- coding: utf-8 -*-


from odoo import http, models
from odoo.http import request


class okwrepoejemplo1(http.Controller):
    @http.route("/okw/repo", type='http', auth="public", website=True)
    def website_okw_repo(self, **kwargs):
        repo = request.env["odooknowledge.okw.repo"].sudo()
        f = repo.search([])
        values = {
            'repo_ids': f,
        }
        return request.render('odooknowledge.website_repo', values)

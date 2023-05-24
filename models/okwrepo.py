# -*- coding: utf-8 -*-

from odoo import models, fields


class okwrepo(models.Model):
    _name =  "odooknowledge.okw.repo"
    _description = "Modelo que representa distintas versiones de Odoo"

    name = fields.Char()
    url = fields.Char()  

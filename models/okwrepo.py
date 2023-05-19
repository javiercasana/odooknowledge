# -*- coding: utf-8 -*-

from odoo import models, fields


class okwrepo(models.Model):
    _name =  "odooknowledge.okwrepo"
    _description = "Modelo que representa distintas versiones de Odoo"

    name = fields.Char()
    url = fields.Char()  

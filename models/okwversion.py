from odoo import models, fields


class okwversion(models.Model):
    _name =  "odooknowledge.okw.version"
    _description = "Modelo que representa distintas versiones de Odoo"

    name = fields.Char()


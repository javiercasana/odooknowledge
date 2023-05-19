from odoo import models, fields


class okwversion(models.Model):
    _name =  "odooknowledge.okwversion"
    _description = "Modelo que representa distintas versiones de Odoo"

    name = fields.Char()


# -*- coding: utf-8 -*-

from odoo import models, fields


class okwfunction(models.Model):
    _name =  "odooknowledge.okwfunction"
    _description = "Modelo que representa distintas versiones de Odoo"

    name = fields.Char()
    description = fields.Text()
    parent_id = fields.Many2one("odooknowledge.okwfunction", index=True, ondelete='cascade')
    model_ids = fields.Many2many('odooknowledge.okwmodel', 'model_model_ids_default_rel','function_ids', 'model_id', string=' Modelos')
    active = fields.Boolean(default=True)
    website_published = fields.Boolean(default = True)
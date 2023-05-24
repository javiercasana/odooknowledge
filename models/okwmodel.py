# -*- coding: utf-8 -*-

from odoo import models, fields


class okwmodel(models.Model):
    _name =  "odooknowledge.okw.model"
    _description = "Modelo que representa distintas versiones de Odoo"

    name = fields.Char()
    technical_name = fields.Char()
    description = fields.Text()
    active = fields.Boolean(default=True)
    license = fields.Char()
    repo_id = fields.Many2one('odooknowledge.okw.repo',string='okw.repo')
    function_ids = fields.Many2many('odooknowledge.okw.function', 'function_function_ids_default_rel','modules_ids', 'function_id', string=' Funciones')
    version_ids = fields.Many2many('odooknowledge.okw.version', 'version_version_ids_default_rel','modules_ids', 'version_id', string=' version')



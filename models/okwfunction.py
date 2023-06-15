# -*- coding: utf-8 -*-

from odoo import models, fields, api
#from odoo.addons.http_routing.models.ir_http import slug



class okwfunction(models.Model):
    _name =  "odooknowledge.okw.function"
    _description = "Modelo que representa distintas versiones de Odoo"

    name = fields.Char()
    description = fields.Text(string="Description")
    parent_id = fields.Many2one("odooknowledge.okw.function", index=True, ondelete='cascade')
    modules_ids = fields.Many2many('odooknowledge.okw.model', 'model_modules_ids_default_rel','function_ids', 'model_id', string=' Módulos')
    active = fields.Boolean(default=True)
    website_published = fields.Boolean(default = True)
  

    @api.depends("parent_id.name", "name")
    def _compute_display_name(self):
        for record in self: 
            if record.parent_id:
                record.display_name = "{} / {}".format(record.parent_id.name, record.name)
            else: 
                record.display_name = record.name
 

    display_name = fields.Char(compute='_compute_display_name')


"""

    def _function_website_url(self):
        super(function, self)._function_website_url()
        for function in self:
            function.website_url = "/function/%s/%s" % (slug(function.name), slug(function))    

"""

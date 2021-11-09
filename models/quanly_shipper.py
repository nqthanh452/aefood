# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class SaleOrderInherit(models.Model):
    _inherit = "hr.employee"


    tiemchung = fields.Boolean(string="Tiêm chủng")

# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class SaleOrderInherit(models.Model):
    _inherit = "hr.employee"

    shippername = fields.Many2one('res.partner', string="Tên người giao hàng")
    CCCD = fields.Char("Căn cước công dân")
    tiemchung = fields.Boolean(string="Tiêm chung" )

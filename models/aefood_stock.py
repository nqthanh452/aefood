# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class StockPickingInherit(models.Model):
    _inherit = "stock.picking"

    shippername = fields.Many2one('hr.employee', string="Tên người giao hàng", store=True, readonly=False,
                                  tracking=True)

    delivery = fields.Many2one('delivery.carrier', string="Chọn hình thức giao hàng", readonly=False)
    address = fields.Char('Địa chỉ giao hàng')
    phone = fields.Char("Số điện thoại nhận hàng")

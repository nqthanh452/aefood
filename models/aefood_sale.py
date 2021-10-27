# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class SaleOrderInherit(models.Model):
    _inherit = "sale.order"

    shippername = fields.Char("Tên người giao hàng")
    deliverydate = fields.Date(string="Thời gian giao hàng dự kiến")
    delivery = fields.Selection([
        ('giao hàng tiết kiệm', 'Giao hàng tiết kiệm'),
        ('giao hàng nhanh', 'Giao hàng nhanh')
    ], string='Chọn hình thức giao hàng', default='giao hàng tiết kiệm')
    status = fields.Char("tình trạng đơn hàng")

class aefoodSale(models.Model):
    _name = "aefood.sale"
    _inherit = ['mail.thread',
                'mail.activity.mixin']
    _description = "AEfood Sale Company"
    _rec_name = "shippername"


    shippername = fields.Char("Tên người giao hàng")
    deliverydate = fields.Date(string="Thời gian giao hàng dự kiến")
    delivery = fields.Selection([
        ('giao hàng tiết kiệm', 'Giao hàng tiết kiệm'),
        ('giao hàng nhanh', 'Giao hàng nhanh')
    ], string='Chọn hình thức giao hàng', default='giao hàng tiết kiệm')
    status = fields.Char("tình trạng đơn hàng")
    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):

            vals['name'] = self.env['ir.sequence'].next_by_code('aefood.manageshipper.sequense') or _('New')
        result = super(aefoodSale, self).create(vals)
        return result
#quản lý thông tin shipper
    shipperage = fields.Date(string="Năm sinh người giao hàng")
    shippergender= fields.Selection([
        ('nam', 'Nam'),
        ('nu', 'Nu')
    ], string='Giới tính', default='nam')

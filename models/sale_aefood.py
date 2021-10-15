# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

class aefood(models.Model):
    _name = "sale.aefood" 
    _inherit = "sale.order" # 
    _description = "Prototype inheritance"

    # add new field
    
    status = fields.Char("tình trạng đơn hàng")
    
    # avoid error: Many2many fields sale.aefood.transaction_ids and sale.order.transaction_ids use the same table and columns
    transaction_ids = fields.Many2many('sale.order.transaction','aefood_transaction_rel','sale_id','transaction_id',string='Tags')
   #Many2many fields sale.aefood.tag_ids and sale.order.tag_ids use the same table and columns
    tag_ids = fields.Many2many('sale.order.tag','aefood_tag_rel','sale_id','tag_id',string='Tags')
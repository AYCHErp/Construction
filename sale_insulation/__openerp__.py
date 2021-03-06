# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

{
    "name" : "Sale Insulation",
    "version" : "0.1",
    "author" : "Savoir-faire Linux,Odoo Community Association (OCA)",
    "website" : "http://www.savoirfairelinux.com",
    "license" : "AGPL-3",
    "category" : "Sales Management",
    "description" : """
This module allows you  to generate sale orders that calculates the right price 
for insulation products.
    """,
    "depends" : [
        "sale", 
        "product_insulation",
        "procurement_insulation",
        "stock_picking_delivery_insulation",
        "account_invoice_insulation",
    ],
    "images" : [],
    "test" : [],
    "demo" : [],
    "data" : [
	"report/sale_insulation_report.xml",
	"sale_insulation_view.xml",
	],
    "installable": True,
    "complexity": "normal",
}

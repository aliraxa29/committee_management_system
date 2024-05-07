# Copyright (c) 2024, Ali Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import cint


class Committee(Document):
    def validate(self):
        self.validate_from_to_date()
        self.validate_amount()
    
    
    def validate_from_to_date(self):
        if self.from_date > self.to_date:
            frappe.throw(_("From Date cannot be greater than to date"))
            
    def validate_amount(self):
        if cint(self.amount) <= 0:
            frappe.throw(_('Amount should be greater than zero'))
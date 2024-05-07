# Copyright (c) 2024, Ali Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import cint
from frappe import _


class CollectCommittee(Document):
    def before_submit(self):
        if cint(self.amount) <= 0:
            frappe.throw(_('Amount should be greater than zero'))

# Copyright (c) 2024, Ali Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class CommitteeMember(Document):
    def before_save(self):
        if not self.first_name and not self.last_name:
            frappe.throw(_('First Name or Last name are required'))
        self.full_name = f'{self.first_name} {self.last_name or ""}'

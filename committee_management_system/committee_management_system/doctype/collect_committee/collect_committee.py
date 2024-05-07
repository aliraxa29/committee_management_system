# Copyright (c) 2024, Ali Raza and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import cint, now
from frappe import _


class CollectCommittee(Document):
    
    def before_submit(self):
        if cint(self.amount) <= 0:
            frappe.throw(_('Amount should be greater than zero'))
            
        exists = frappe.db.sql("""SELECT COUNT(*) FROM `tabCollect Committee` WHERE member = %s AND committee = %s AND month = %s""", (self.member, self.committee, self.month))[0][0]
        if exists:
            frappe.throw(
                            title= "Exists",
                            msg= _("Committee Collection for member {0} against committee {1} for month {2} is already collected").format(self.member, self.committee, self.month),
                        )

            
    def on_submit(self):
        gl = frappe.new_doc('Committee Ledger')
        gl.docstatus = 1
        gl.posting_date = now()
        gl.transaction_date = now()
        gl.committee_member = self.member
        gl.committee = self.committee
        gl.debit = self.amount
        gl.credit = 0
        gl.remarks = f'Cash {self.amount} Received from {self.member} on {now()} against Committee {self.committee}'
        gl.is_cancelled = 0
        gl.insert()
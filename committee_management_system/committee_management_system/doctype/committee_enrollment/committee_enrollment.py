# Copyright (c) 2024, Ali Raza and contributors
# For license information, please see license.txt
# 

import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import cint, now
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar


class CommitteeEnrollment(Document):
    
    def before_submit(self):
        self.check_enrollment()
        
    def on_submit(self):
        if self.create_cc:
            c_detail = frappe.get_doc('Committee', self.committee)
            months = self.months_between_dates(str(c_detail.from_date), str(c_detail.to_date))
            for i in months:
                current_month = cint(datetime.now().strftime("%m"))
                if cint(i) <= current_month:    
                    cc = frappe.new_doc('Collect Committee')
                    cc.docstatus = 0
                    cc.member = self.committee_member
                    cc.committee = self.committee
                    cc.amount = c_detail.amount
                    cc.month = self.get_month_name(cint(i))
                    cc.insert()
    
    
    def check_enrollment(self):
        enrollment_count = frappe.db.sql("""
            SELECT COUNT(*) 
            FROM `tabCommittee Enrollment`
            WHERE committee_member = %s 
            AND committee = %s 
            AND docstatus = 1
        """, (self.committee_member, self.committee))[0][0]
        
        if cint(enrollment_count) > 0:
            frappe.throw(_('Enrollment of member {0} already exists.').format(self.committee_member))
            
            
    def months_between_dates(self, from_date, to_date):
        start_date = datetime.strptime(from_date, "%Y-%m-%d")
        end_date = datetime.strptime(to_date, "%Y-%m-%d")

        months = []
        while start_date <= end_date:
            months.append(start_date.strftime("%m"))
            start_date += relativedelta(months=1)
        return months
    
    def get_month_name(self, month_number):
        return datetime.strptime(str(month_number), "%m").strftime("%b")
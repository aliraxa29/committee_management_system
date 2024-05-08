// Copyright (c) 2024, Ali Raza and contributors
// For license information, please see license.txt

frappe.ui.form.on("Committee Disbursement", {
    refresh(frm) {
        frm.set_query('committee_member', () => {
            return {
                filters: {
                    enabled: 1
                }
            }
        });
        frm.set_query('committee', () => {
            return {
                filters: {
                    status: 'Ongoing'
                }
            }
        });
        frm.set_value('handed_over_by', frappe.session.user);
        if (frm.doc.__islocal) {
            frm.set_value('disbursement_date', frappe.datetime.now_datetime());
            frm.set_value('posting_date', frappe.datetime.now_datetime());
        }
    },
});

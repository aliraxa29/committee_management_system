// Copyright (c) 2024, Ali Raza and contributors
// For license information, please see license.txt

frappe.ui.form.on("Collect Committee", {
	refresh(frm) {
        frm.set_query('member', () => {
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
            };
        });
	},
});

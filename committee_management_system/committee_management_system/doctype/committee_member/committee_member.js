// Copyright (c) 2024, Ali Raza and contributors
// For license information, please see license.txt

frappe.ui.form.on("Committee Member", {
    refresh: (frm) => {
        frm.set_query('committee', () => {
            return {
                filters: {
                    status: ['in', ['Ongoing', 'To Start']]
                }
            };
        });
    }
});
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
    },
    
    onload: (frm) => {
        frm.get_field("committees").grid.cannot_add_rows = true;
        frm.get_field("committees").grid.only_sortable();
    }
});
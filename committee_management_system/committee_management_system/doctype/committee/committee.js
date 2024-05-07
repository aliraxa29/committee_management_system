// Copyright (c) 2024, Ali Raza and contributors
// For license information, please see license.txt

frappe.ui.form.on("Committee", {
    refresh(frm) {
        frm.add_custom_button('Closed', () => {
            frm.set_value('status',"Ongoing")
            frm.save();
            func()
        }, 'Set Status');
    }
});
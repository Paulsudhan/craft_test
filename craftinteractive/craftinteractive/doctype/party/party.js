// Copyright (c) 2024, craftinteractive and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Party", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Party', {
    onload: function(frm) {
        frm.set_value('posting_date', frappe.datetime.nowdate());
        frm.set_query('employee', function() {
            return {
                filters: {
                    employment_type: 'Full-time'
                }
            };
        });
    },
    refresh: function(frm) {
        if (!frm.doc.__islocal) {
            frm.add_custom_button(__("Go to Attendance"), function(){
                frappe.set_route('List', 'Attendance',{
                    employee:frm.doc.employee
                })
            });
        }
    }
});

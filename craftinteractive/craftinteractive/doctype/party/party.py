# Copyright (c) 2024, craftinteractive and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from hrms.hr.doctype.appraisal_cycle.appraisal_cycle import AppraisalCycle



class Party(Document):
	pass

class AppraisalCycle(AppraisalCycle):
	def get_employees_for_appraisal(self):
			filters = {
				"status": "Active",
				"company": self.company,
			}
			if self.department:
				filters["department"] = self.department
			if self.branch:
				filters["branch"] = self.branch
			if self.designation:
				filters["designation"] = self.designation

			employees = frappe.db.get_all(
				"Employee",
				filters={"employment_type": "Full-time"},
				fields=[
					"name",
					"employee_name",
					"branch",
					"designation",
					"department",
				],
			)

			return employees

 
	
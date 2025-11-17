"""
 Xử lý XML File
"""

from xml.dom import minidom


def parse_employees(xml_path: str):
	"""Parse an XML of employees and return list of (id, name)."""
	try:
		dom = minidom.parse(xml_path)
	except Exception as e:
		print(f"Không thể mở file XML: {e}")
		return []

	collection = dom.documentElement
	employees = collection.getElementsByTagName("employee")
	result = []
	for employee in employees:
		try:
			tag_id = employee.getElementsByTagName('id')[0]
			id_val = tag_id.childNodes[0].data.strip()
		except Exception:
			id_val = ""
		try:
			tag_name = employee.getElementsByTagName('name')[0]
			name = tag_name.childNodes[0].data.strip()
		except Exception:
			name = ""
		result.append((id_val, name))
	return result


def main():
	xml_path = "employees.xml"
	employees = parse_employees(xml_path)
	if not employees:
		print("Không tìm thấy employee nào hoặc file rỗng.")
		return

	for emp_id, emp_name in employees:
		print(emp_id, '\t', emp_name)


if __name__ == "__main__":
	main()
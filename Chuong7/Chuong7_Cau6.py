"""
Xử lý CSV File
"""
import csv


def read_csv(path: str):
	rows = []
	try:
		with open(path, newline='', encoding='utf-8') as f:
			reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
			for row in reader:
				if not row:
					continue
				rows.append(row)
	except FileNotFoundError:
		print(f"File không tồn tại: {path}")
	return rows


def main():
	path = 'datacsv.csv'
	rows = read_csv(path)
	for row in rows:
		# safeguard indexing
		a = row[0] if len(row) > 0 else ''
		b = row[1] if len(row) > 1 else ''
		print(a, '\t', b)


if __name__ == "__main__":
	main()
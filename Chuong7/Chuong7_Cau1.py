"""
Viết chương trình nhập vào thông tin của một sản phẩm:
Mã: Chuỗi
Tên: Chuỗi
Đơn Giá: Số
Mỗi một Sản phẩm sau khi nhập thành công sẽ lưu nối đuôi vào File theo quy tắc:
MSSP;Tên Sản phẩm; Đơn giá
Mẫu Dữ liệu lưu nối đuôi vào file tương tự như dưới đây:
sv1;Cocacolala;15.5
sp2;Bưởi 5 Roi;18.0
sp3;Bia 333;14.5
Sau đó thực hiện 2 chức năng chính:
a) xuất danh sách sản phẩm từ File
b) Sắp xếp Sản phẩm theo đơn giá giảm dần

"""
from typing import List


def LuuFile(path: str, data: str) -> None:
	"""Append a product line to the file (UTF-8)."""
	with open(path, 'a', encoding='utf-8') as f:
		f.write(data + "\n")


def DocFile(path: str) -> List[List]:
	"""Read products from file and parse into [code, name, price].

	Price is converted to float when possible; malformed lines are skipped.
	"""
	arrProduct: List[List] = []
	try:
		with open(path, 'r', encoding='utf-8') as f:
			for line in f:
				data = line.strip()
				if not data:
					continue
				parts = data.split(';')
				if len(parts) < 3:
					continue
				code = parts[0]
				name = parts[1]
				try:
					price = float(parts[2])
				except ValueError:
					continue
				arrProduct.append([code, name, price])
	except FileNotFoundError:
		pass
	return arrProduct


def XuatSanPham(dssp: List[List]) -> None:
	for row in dssp:
		print(f"{row[0]}\t{row[1]}\t{row[2]}")
	print()


def SortSp(dssp: List[List]) -> None:
	"""Sort products in-place by price descending."""
	dssp.sort(key=lambda r: r[2], reverse=True)


def main():
	db_path = "database.txt"

	print("Nhập thông tin sản phẩm mới (bỏ trống mã để bỏ qua):")
	masp = input("nhập mã SP: ").strip()
	if masp:
		tensp = input("nhập tên sp: ").strip()
		try:
			dongia = float(input("nhập giá: "))
		except ValueError:
			print("Giá không hợp lệ, bỏ qua lưu.")
		else:
			line = f"{masp};{tensp};{dongia}"
			LuuFile(db_path, line)

	dssp = DocFile(db_path)
	if not dssp:
		print("Không có sản phẩm trong file.")
		return

	print("Danh sách sản phẩm (từ file):")
	XuatSanPham(dssp)

	SortSp(dssp)
	print("Sản phẩm sau khi sắp xếp theo đơn giá giảm dần:")
	XuatSanPham(dssp)


if __name__ == "__main__":
	main()
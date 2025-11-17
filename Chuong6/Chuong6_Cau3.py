"""
Viết chương trình cho phép:
- Khởi tạo và nhập vào ma trận MxN phần tử ngẫu nhiên
- Xuất dòng bất kỳ nhập từ bàn phím
Trang 52/84
- Xuất cột bất kỳ từ bàn phím
- Xuất số MAX trong ma trận
"""
from random import randrange
def TaoMaTran(m,n):
	D = []
	for i in range(m):
		row = []
		for j in range(n):
			row.append(randrange(100))
		D.append(row)
	return D
def XuatMaTran(D):
	for row in D:
		for element in row:
			print(element, end='\t')
		print()
def LayDong(D, r):
	return D[r]


def XuatList1Chieu(R):
	for element in R:
		print(element, end='\t')
	print()


def LayCot(D, c):
	C = []
	for i in range(len(D)):
		C.append(D[i][c])
	return C


def MAX_D(D):
	max_val = D[0][0]
	for i in range(len(D)):
		for j in range(len(D[i])):
			if max_val < D[i][j]:
				max_val = D[i][j]
	return max_val


def main():
	print("Nhập số dòng:")
	m = int(input())
	print("Nhập số cột:")
	n = int(input())

	D = TaoMaTran(m, n)
	XuatMaTran(D)

	print("Mời bạn nhập dòng muốn xuất (0-based index):")
	r = int(input())
	XuatList1Chieu(LayDong(D, r))

	print("Mời bạn nhập cột muốn xuất (0-based index):")
	c = int(input())
	XuatList1Chieu(LayCot(D, c))

	max_value = MAX_D(D)
	print("Số lớn nhất trong ma trận =", max_value)


if __name__ == "__main__":
	main()
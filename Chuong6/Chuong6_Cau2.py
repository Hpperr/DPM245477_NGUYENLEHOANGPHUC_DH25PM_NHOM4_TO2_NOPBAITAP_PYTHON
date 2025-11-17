"""
Viết chương trình cho phép:
- Viết lệnh khởi tạo ngẫu nhiên n phần tử cho list
- Gọi k là một số nhập từ bàn phím, hãy xóa tất cả các phần tử có giá trị k tồn tại
trong list
- Kiểm tra list có đối xứng hay không
"""
from random import randrange


def CheckDoiXung(lst):
	for i in range(len(lst)):
		if lst[i] != lst[len(lst) - i - 1]:
			return False
	return True


def main():
	lst = []
	n = int(input("Nhập số phần tử: "))
	for _ in range(n):
		lst.append(randrange(0, 100))

	print("List sau khi tạo ngẫu nhiên là:")
	print(lst)

	x = int(input("Mời bạn chèn thêm số mới: "))
	lst.append(x)
	print("List sau khi chèn:")
	print(lst)

	k = int(input("Mời nhập số để xóa: "))
	while k in lst:
		lst.remove(k)

	print("List sau khi xóa:")
	print(lst)

	kt = CheckDoiXung(lst)
	if kt:
		print("List đối xứng")
	else:
		print("List không đối xứng")


if __name__ == "__main__":
	main()
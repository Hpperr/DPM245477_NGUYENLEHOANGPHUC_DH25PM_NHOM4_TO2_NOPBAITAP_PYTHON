"""
Viết chương trình cho phép:
- Khởi tạo list
- Thêm phần tử vào list
- Nhập k, kiểm tra k xuất hiện bao nhiêu lần trong list
- Tính tổng các số nguyên tố trong list
- Sắp xếp
- Xóa list

"""
from random import randrange


def CheckPrime(n):
  if n < 2:
    return False
  limit = int(n ** 0.5) + 1
  for i in range(2, limit):
    if n % i == 0:
      return False
  return True


def main():
  print("Chương trình xử lý List")
  n = int(input("Nhập số phần tử: "))
  lst = [randrange(-100, 100) for _ in range(n)]

  print("List ngẫu nhiên là:")
  print(lst)

  value = int(input("Mời bạn thêm số mới: "))
  lst.append(value)
  print(lst)

  k = int(input("Bạn muốn đếm số nào: "))
  dem = lst.count(k)
  print(k, "xuất hiện", dem, "trong list")

  demnt = 0
  tongnt = 0
  for x in lst:
    if CheckPrime(x):
      demnt += 1
      tongnt += x

  print("Có", demnt, "số nguyên tố trong list")
  print("Tổng =", tongnt)

  lst.sort()
  print("List sau khi sort:")
  print(lst)

  lst.clear()
  print("List sau khi xóa:")
  print(lst)


if __name__ == "__main__":
  main()

"""
Cho một tập tin có dữ liệu trên mỗi dòng như dưới đây:
5,6,8,9,-5
-9,5,4,7,8
6,7,8,3,6,46,7,2,-6,-7
a) Viết hàm đọc file, mỗi dòng khởi tạo thành 1 list và xuất ra màn hình
b) Xuất các số âm trên mỗi dòng ra màn hình
"""
def LuuFile(path,data):
  with open(path, 'a', encoding='utf-8') as file:
    file.write(data + "\n")
def DocFile(path):
  arrSo = []
  with open(path, 'r', encoding='utf-8') as file:
    for line in file:
      data = line.strip()
      if not data:
        continue
      arr = [x.strip() for x in data.split(',') if x.strip()]
      arrSo.append(arr)
  return arrSo


def XuatSoAmTrenMoiDong(arrSo):
  for row in arrSo:
    for element in row:
      number = int(element)
      if number < 0:
        print(number, end='\t')
    print()


def main():
  # tạo dữ liệu mẫu (nối vào file)
  LuuFile("csdl_so.txt", "-5,4,7,9,3,20")
  LuuFile("csdl_so.txt", "5,-4,37,-19,24,-21")
  LuuFile("csdl_so.txt", "15,9,0,-38,-3,15")
  LuuFile("csdl_so.txt", "5,-4,77,-9,3,-7")
  LuuFile("csdl_so.txt", "55,44,27")
  LuuFile("csdl_so.txt", "-50,26")

  arrSo = DocFile("csdl_so.txt")
  print(arrSo)

  print("Các số âm trên mỗi dòng:")
  XuatSoAmTrenMoiDong(arrSo)


if __name__ == "__main__":
  main()


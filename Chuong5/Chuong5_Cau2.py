"""
Một Chuỗi được gọi là tối ưu khi: Không chứa các khoảng trắng dư thừa, các từ cách
nhau bởi một khoảng trắng
"""
def ToiUuChuoi(s):
	s2 = s
	s2 = s2.strip()
	arr = s2.split(' ')
	s2 = ""
	for x in arr:
		word = x
		if len(word.strip()) != 0:
			s2 = s2 + word + " "
	return s2.strip()


def main():
	s = " Trần Duy Thanh "
	print(s, "=>", len(s))
	s = ToiUuChuoi(s)
	print(s, "=>", len(s))


if __name__ == "__main__":
	main()

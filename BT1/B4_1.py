s = input("Nhập chuỗi s: ")

# Câu a: Độ dài của chuỗi s
print("Độ dài của chuỗi s:", len(s))

# Câu b: Xóa bỏ khoảng trắng thừa của chuỗi s
xoa_khoang_trang = s.replace("  "," ")
print("\nChuỗi s sau khi xóa khoảng trắng thừa:", xoa_khoang_trang)
print("Độ dài của chuỗi s:", len(xoa_khoang_trang))

# Câu c: Đếm số từ của chuỗi s và xuất mỗi từ nằm trên 1 dòng
ds = s.split(" ")
print("\nSố từ trong chuỗi s:", len(ds))
print("Các từ trong chuỗi s:")
for tu in ds:
    print(tu)

# Câu d: Nhập số tự nhiên k, xuất k ký tự bên trái của s, k ký tự bên phải của s
k = int(input("\nNhập số tự nhiên k: "))
print("Ký tự bên trái của s:", s[:k])
print("Ký tự bên phải của s:", s[-k:])

# Câu e: Nhập số tự nhiên k, n. Xuất n ký tự của s, bắt đầu từ vị trí k
k = int(input("\nNhập số tự nhiên k: "))
n = int(input("Nhập số tự nhiên n: "))
print("N ký tự của s, kể từ vị trí k:", s[k:k+n])
def kiemtra_songuyento_mang(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True  

a = [10, 3, 5, 7, 8, 9, 15]

# Câu a: Xuất các phần tử trong mảng và tính tổng các phần tử trong mảng
sum = 0
ds_tam = []
sx_mang = sorted(a)
for i in sx_mang:
    ds_tam.append(str(i))
    sum += i
print("Các phần tử trong mảng là: " + ", ".join(ds_tam))
print(f"Tổng các phần tử trong mảng là: {sum}")

# Câu b: Các phần tử là số nguyên tố trong mảng
ds_tam = []
for i in sx_mang:
    if kiemtra_songuyento_mang(i):
        ds_tam.append(str(i))
print("\nCác phần tử nguyên tố trong mảng là: " + ", ".join(ds_tam))

# Câu c: Thêm một phần tử z vào mảng
z = int(input("\nNhập phần tử z cần thêm vào mảng: "))
a.append(z)
sx_mang = sorted(a)
ds_tam = []
for i in sx_mang:
    ds_tam.append(str(i))
print("Các phần tử trong mảng là: " + ", ".join(ds_tam))

# Câu d: Xóa một phần tử k khỏi mảng
k = int(input("\nNhập phần tử k cần xóa khỏi mảng: "))
if k in a:
    a.remove(k)
    print(f"Phần tử {k} đã được xóa khỏi mảng.")
else:
    print(f"Phần tử {k} không có trong mảng.")
sx_mang = sorted(a)
ds_tam = []
for i in sx_mang:
    ds_tam.append(str(i))
print("Các phần tử trong mảng là: " + ", ".join(ds_tam))

# Câu e: Nhập 1 số x, kiểm tra xem x có trong mảng không? Nếu có thì xuất vị trí của x trong mảng, nếu không thì xuất thông báo không tìm thấy
x = int(input("\nNhập số x cần kiểm tra: "))
if x in a:
    print(f"Số {x} có trong mảng tại vị trí: {a.index(x)}")
else:
    print(f"Số {x} không có trong mảng.")

# Câu f: Xóa phần tử có giá trị x trong mảng a
x = int(input("\nNhập số x cần xóa khỏi mảng: "))
if x in a:
    while x in a:
        a.remove(x)
    print(f"Số {x} đã được xóa khỏi mảng.")
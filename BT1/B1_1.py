a = input("Nhập vào số thứ 1: ")
b = input("Nhập vào số thứ 2: ")

tong = float(a) + float(b)
print("Tổng của hai số là: ", tong)
hieu = float(a) - float(b)
print("Hiệu của hai số là: ", hieu)
tich = float(a) * float(b)
print("Tích của hai số là: ", tich)

# Kiểm tra b có khác 0 không trước khi chia
if float(b) == 0:
    print("Không thể chia cho 0!")
else:
    thuong = float(a) / float(b)
    print("Thương của hai số là: ", thuong)
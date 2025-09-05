import math
def kiemtra_songuyento(n):
    if n < 2:
        return False
    for i in range(2, math.sqrt(n) + 1):
        if n % i == 0:
            return False
        
    return True

n = int(input("Nhập một số nguyên dương N: "))

# Câu a: Kiểm tra N có phải số nguyên tố không?
if kiemtra_songuyento(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
    
# Câu b: Xuất các số nguyên từ 1->N và Tính tổng các chữ số của N
print(f"\nCác số nguyên từ 1 đến {n}:")
for i in range(1, n + 1):
    print(i, end=' ')
tong_chu_so = sum(range(1, n + 1))
print(f"\nTổng các chữ số của {n} là: {tong_chu_so}")

# Câu c: Xuất các số nguyên tố từ 1->N
print(f"\nCác số nguyên tố từ 1 đến {n}:")
for i in range(1, n + 1):
    if kiemtra_songuyento(i):
        print(i, end=' ')

# Câu d: Xuất N số nguyên tố đầu tiên
print(f"\n\n{n} số nguyên tố đầu tiên là:")
count = 0
i = 2
while count < n:
    if kiemtra_songuyento(i):
        print(i, end=' ')
        count += 1
    i += 1
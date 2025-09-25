class SinhVien:
    def __init__(self, ma_sv, ten, tuoi, diem_tb):
        self.ma_sv = ma_sv
        self.ten = ten
        self.tuoi = tuoi
        self.diem_tb = diem_tb

    def hien_thi_thong_tin(self):
        print(f"Mã SV: {self.ma_sv}")
        print(f"Tên: {self.ten}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Điểm TB: {self.diem_tb}")
    
    
class QuanLySinhVien:
    def __init__(self):
        self.danh_sach_sv = []

    def them_sinh_vien(self, sv):
        self.danh_sach_sv.append(sv)
        print(f"Đã thêm sinh viên {sv.ten}.")

    def hien_thi_danh_sach(self):
        if not self.danh_sach_sv:
            print("Danh sách sinh viên trống.")
            return
        print("\n--- DANH SÁCH SINH VIÊN ---")
        for sv in self.danh_sach_sv:
            sv.hien_thi_thong_tin()
        print("-" * 25)
        
    def sua_sinh_vien(self, ma_sv, ten_moi, tuoi_moi, diem_tb_moi):
        for sv in self.danh_sach_sv:
            if sv.ma_sv == ma_sv:
                sv.ten = ten_moi
                sv.tuoi = tuoi_moi
                sv.diem_tb = diem_tb_moi
                print(f"Đã cập nhật thông tin cho SV có mã {ma_sv}.")
                return
        print(f"Không tìm thấy sinh viên có mã {ma_sv}.")
    
    def xoa_sinh_vien(self, ma_sv):
        initial_len = len(self.danh_sach_sv)
        self.danh_sach_sv = [sv for sv in self.danh_sach_sv if sv.ma_sv != ma_sv]
        if len(self.danh_sach_sv) < initial_len:
            print(f"Đã xóa sinh viên có mã {ma_sv}.")
        else:
            print(f"Không tìm thấy sinh viên có mã {ma_sv}.")
            
    def tim_kiem_sinh_vien(self, tu_khoa):
        ket_qua = []
        for sv in self.danh_sach_sv:
            if tu_khoa.lower() in sv.ten.lower() or \
               tu_khoa.lower() == sv.ma_sv.lower():
                ket_qua.append(sv)
        if ket_qua:
            print(f"\n--- KẾT QUẢ TÌM KIẾM cho '{tu_khoa}' ---")
            for sv in ket_qua:
                sv.hien_thi_thong_tin()
                print("-" * 25)
        else:
            print(f"Không tìm thấy sinh viên nào với từ khóa '{tu_khoa}'.")

# def nhap_sinh_vien():
#     ma_sv = input("Nhập mã sinh viên: ")
#     ten = input("Nhập tên sinh viên: ")
#     tuoi = int(input("Nhập tuổi: "))
#     diem_tb = float(input("Nhập điểm trung bình: "))
#     return SinhVien(ma_sv, ten, tuoi, diem_tb)

def menu():
    qlsv = QuanLySinhVien()
    while True:
        print("\n--- MENU QUẢN LÝ SINH VIÊN ---")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách sinh viên")
        print("3. Sửa thông tin sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")
        if chon == "1":
            sv = nhap_sinh_vien()
            qlsv.them_sinh_vien(sv)
        elif chon == "2":
            qlsv.hien_thi_danh_sach()
        elif chon == "3":
            ma_sv = input("Nhập mã sinh viên cần sửa: ")
            print("Nhập thông tin mới:")
            ten = input("Tên mới: ")
            tuoi = int(input("Tuổi mới: "))
            diem_tb = float(input("Điểm TB mới: "))
            qlsv.sua_sinh_vien(ma_sv, ten, tuoi, diem_tb)
        elif chon == "4":
            ma_sv = input("Nhập mã sinh viên cần xóa: ")
            qlsv.xoa_sinh_vien(ma_sv)
        elif chon == "5":
            tu_khoa = input("Nhập từ khóa tìm kiếm: ")
            qlsv.tim_kiem_sinh_vien(tu_khoa)
        elif chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# if __name__ == "__main__":
#     menu()

# Sử dụng
qlsv = QuanLySinhVien()
sv1 = SinhVien("SV001", "Nguyễn Văn A", 20, 8.5)
sv2 = SinhVien("SV002", "Trần Thị B", 21, 7.8)

qlsv.them_sinh_vien(sv1)
qlsv.them_sinh_vien(sv2)
qlsv.hien_thi_danh_sach()

qlsv.sua_sinh_vien("SV001", "Nguyễn Văn L", 22, 9.0)
qlsv.hien_thi_danh_sach()

qlsv.tim_kiem_sinh_vien("Nguyễn")
qlsv.tim_kiem_sinh_vien("SV003")

qlsv.xoa_sinh_vien("SV002")
qlsv.hien_thi_danh_sach()
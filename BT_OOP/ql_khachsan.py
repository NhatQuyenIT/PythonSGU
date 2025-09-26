# Hệ thống quản lý khách sạn
from datetime import datetime

class Phong:
    def __init__(self, so_phong, loai_phong, gia_phong):
        self.so_phong = so_phong
        self.loai_phong = loai_phong
        self.gia_phong = gia_phong
        self.trang_thai = "Trống"  # Trạng thái ban đầu là "Trống"
        self.ten_khach = None
        self.ngay_dat = None
        self.so_dem = 0

    def hien_thi_thong_tin(self):
        thong_tin = f"Số phòng: {self.so_phong}, Loại phòng: {self.loai_phong}, Giá phòng: {self.gia_phong:,.0f} VND, Trạng thái: {self.trang_thai}"
        if self.ten_khach:
            thong_tin += f", Khách: {self.ten_khach}, Ngày đặt: {self.ngay_dat}, Số đêm: {self.so_dem}"
        print(thong_tin)
        print("-" * 50)
        
class QuanLyKhachSan:
    def __init__(self):
        self.danh_sach_phong = []

    def them_phong(self, phong):
        self.danh_sach_phong.append(phong)
        print(f"Đã thêm phòng số: {phong.so_phong}")

    def cap_nhat_trang_thai_phong(self, so_phong, trang_thai_moi):
        for phong in self.danh_sach_phong:
            if phong.so_phong == so_phong:
                phong.trang_thai = trang_thai_moi
                print(f"Đã cập nhật trạng thái phòng '{so_phong}' thành '{trang_thai_moi}'.")
                return
        print(f"Không tìm thấy phòng có số {so_phong}.")

    def xoa_phong(self, so_phong):
        for phong in self.danh_sach_phong:
            if phong.so_phong == so_phong:
                self.danh_sach_phong.remove(phong)
                print(f"Đã xóa phòng có số {so_phong}.")
                return
        print(f"Không tìm thấy phòng có số {so_phong}.")

    def tim_kiem_phong_theo_loai(self, loai_phong):
        ket_qua = [phong for phong in self.danh_sach_phong if loai_phong.lower() in phong.loai_phong.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} phòng có chứa từ khóa '{loai_phong}':")
            for phong in ket_qua:
                phong.hien_thi_thong_tin()
        else:
            print(f"Không tìm thấy phòng nào có chứa từ khóa '{loai_phong}'.")

    def in_tat_ca_phong(self):
        if not self.danh_sach_phong:
            print("Chưa có phòng nào được thêm.")
            return
        print("Danh sách tất cả các phòng:")
        for phong in self.danh_sach_phong:
            phong.hien_thi_thong_tin()

    def dat_phong(self, so_phong, ten_khach, so_dem):
        for phong in self.danh_sach_phong:
            if phong.so_phong == so_phong:
                if phong.trang_thai == "Trống":
                    phong.trang_thai = "Đã đặt"
                    phong.ten_khach = ten_khach
                    phong.ngay_dat = datetime.now().strftime("%d/%m/%Y")
                    phong.so_dem = so_dem
                    print(f"Đã đặt phòng {so_phong} cho khách {ten_khach}, {so_dem} đêm.")
                    return True
                else:
                    print(f"Phòng {so_phong} đã được đặt.")
                    return False
        print(f"Không tìm thấy phòng số {so_phong}.")
        return False

    def tra_phong(self, so_phong):
        for phong in self.danh_sach_phong:
            if phong.so_phong == so_phong:
                if phong.trang_thai == "Đã đặt":
                    tong_tien = phong.gia_phong * phong.so_dem
                    print(f"Khách {phong.ten_khach} trả phòng {so_phong}")
                    print(f"Số đêm: {phong.so_dem}, Tổng tiền: {tong_tien:,.0f} VND")
                    
                    # Reset thông tin phòng
                    phong.trang_thai = "Trống"
                    phong.ten_khach = None
                    phong.ngay_dat = None
                    phong.so_dem = 0
                    return tong_tien
                else:
                    print(f"Phòng {so_phong} chưa được đặt.")
                    return 0
        print(f"Không tìm thấy phòng số {so_phong}.")
        return 0

    def thong_ke_doanh_thu(self):
        tong_doanh_thu = 0
        phong_da_dat = 0
        
        for phong in self.danh_sach_phong:
            if phong.trang_thai == "Đã đặt":
                phong_da_dat += 1
                tong_doanh_thu += phong.gia_phong * phong.so_dem
        
        print(f"Tổng số phòng: {len(self.danh_sach_phong)}")
        print(f"Số phòng đã đặt: {phong_da_dat}")
        print(f"Số phòng trống: {len(self.danh_sach_phong) - phong_da_dat}")
        print(f"Doanh thu hiện tại: {tong_doanh_thu:,.0f} VND")
        return tong_doanh_thu

    def tim_phong_trong(self):
        phong_trong = [phong for phong in self.danh_sach_phong if phong.trang_thai == "Trống"]
        if phong_trong:
            print(f"Có {len(phong_trong)} phòng trống:")
            for phong in phong_trong:
                phong.hien_thi_thong_tin()
        else:
            print("Không có phòng trống.")
        return phong_trong

    def nhap_phong(self):
        so_phong = input("Nhập số phòng: ")
        loai_phong = input("Nhập loại phòng (ví dụ: Phòng đơn, Phòng đôi, Suite): ")
        while True:
            try:
                gia_phong = float(input("Nhập giá phòng (VND/đêm): "))
                if gia_phong < 0:
                    print("Giá phòng không được âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Giá phòng không hợp lệ. Vui lòng nhập lại.")
        return Phong(so_phong, loai_phong, gia_phong)
    
def menu():
    qlks = QuanLyKhachSan()
    # Thêm một số phòng mẫu
    qlks.them_phong(Phong("101", "Phòng đơn", 500000))
    qlks.them_phong(Phong("102", "Phòng đôi", 800000))
    qlks.them_phong(Phong("201", "Suite", 1500000))
    
    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ KHÁCH SẠN ---")
        print("1. Thêm phòng")
        print("2. Xóa phòng")
        print("3. Cập nhật trạng thái phòng")
        print("4. Đặt phòng")
        print("5. Trả phòng")
        print("6. Tìm phòng trống")
        print("7. Tìm kiếm phòng theo loại")
        print("8. In tất cả phòng")
        print("9. Thống kê doanh thu")
        print("10. Thoát")
        choice = input("Chọn chức năng (1-10): ")

        if choice == '1':
            phong_moi = qlks.nhap_phong()
            qlks.them_phong(phong_moi)
        elif choice == '2':
            so_phong = input("Nhập số phòng cần xóa: ")
            qlks.xoa_phong(so_phong)
        elif choice == '3':
            so_phong = input("Nhập số phòng cần cập nhật: ")
            trang_thai = input("Nhập trạng thái mới (Trống/Đã đặt/Đang sửa chữa): ")
            qlks.cap_nhat_trang_thai_phong(so_phong, trang_thai)
        elif choice == '4':
            so_phong = input("Nhập số phòng cần đặt: ")
            ten_khach = input("Nhập tên khách hàng: ")
            while True:
                try:
                    so_dem = int(input("Nhập số đêm: "))
                    if so_dem <= 0:
                        print("Số đêm phải lớn hơn 0. Vui lòng nhập lại.")
                        continue
                    break
                except ValueError:
                    print("Số đêm không hợp lệ. Vui lòng nhập lại.")
            qlks.dat_phong(so_phong, ten_khach, so_dem)
        elif choice == '5':
            so_phong = input("Nhập số phòng cần trả: ")
            qlks.tra_phong(so_phong)
        elif choice == '6':
            qlks.tim_phong_trong()
        elif choice == '7':
            loai_phong = input("Nhập loại phòng cần tìm: ")
            qlks.tim_kiem_phong_theo_loai(loai_phong)
        elif choice == '8':
            qlks.in_tat_ca_phong()
        elif choice == '9':
            qlks.thong_ke_doanh_thu()
        elif choice == '10':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    menu()
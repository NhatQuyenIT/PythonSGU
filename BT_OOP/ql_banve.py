# Quản lý bán vé máy bay/ tàu hỏa / xem phim
# Lưu trữ thông tin khách hàng, chuyến đi, vé đã bán
# Thêm, sửa, xóa thông tin khách hàng, chuyến đi, vé đã bán
# Tìm kiếm vé theo khách hàng, chuyến đi, vé đã bán
# In vé cho khách hàng
# Thống kê doanh thu theo ngày, tháng, năm

# Hệ thống quản lý bán vé máy bay
class Ve:
    def __init__(self, ma_ve, ten_khach_hang, chuyen_di, gia_ve):
        self.ma_ve = ma_ve
        self.ten_khach_hang = ten_khach_hang
        self.chuyen_di = chuyen_di
        self.gia_ve = gia_ve

    def hien_thi_thong_tin(self):
        print(f"Mã vé: {self.ma_ve}, Khách hàng: {self.ten_khach_hang}, Chuyến đi: {self.chuyen_di}, Giá vé: {self.gia_ve:,.0f} VND")
        print("-" * 50)
        
class QuanLyVe:
    def __init__(self):
        self.danh_sach_ve = []

    def them_ve(self, ve):
        self.danh_sach_ve.append(ve)
        print(f"Đã thêm vé cho khách hàng: {ve.ten_khach_hang}")

    def cap_nhat_ve(self, ma_ve, ten_khach_hang_moi=None, chuyen_di_moi=None, gia_ve_moi=None):
        for ve in self.danh_sach_ve:
            if ve.ma_ve == ma_ve:
                if ten_khach_hang_moi is not None:
                    ve.ten_khach_hang = ten_khach_hang_moi
                if chuyen_di_moi is not None:
                    ve.chuyen_di = chuyen_di_moi
                if gia_ve_moi is not None:
                    ve.gia_ve = gia_ve_moi
                print(f"Đã cập nhật thông tin vé '{ma_ve}'.")
                return
        print(f"Không tìm thấy vé có mã {ma_ve}.")

    def xoa_ve(self, ma_ve):
        for ve in self.danh_sach_ve:
            if ve.ma_ve == ma_ve:
                self.danh_sach_ve.remove(ve)
                print(f"Đã xóa vé có mã {ma_ve}.")
                return
        print(f"Không tìm thấy vé có mã {ma_ve}.")

    def tim_kiem_ve_theo_khach_hang(self, ten_khach_hang):
        ket_qua = [ve for ve in self.danh_sach_ve if ten_khach_hang.lower() in ve.ten_khach_hang.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} vé có chứa từ khóa '{ten_khach_hang}':")
            for ve in ket_qua:
                ve.hien_thi_thong_tin()
        else:
            print(f"Không tìm thấy vé nào có chứa từ khóa '{ten_khach_hang}'.")

    def in_tat_ca_ve(self):
        if not self.danh_sach_ve:
            print("Chưa có vé nào được bán.")
            return
        print("Danh sách tất cả vé đã bán:")
        for ve in self.danh_sach_ve:
            ve.hien_thi_thong_tin()
    def thong_ke_doanh_thu(self):
        tong_doanh_thu = sum(ve.gia_ve for ve in self.danh_sach_ve)
        print(f"Tổng doanh thu từ vé đã bán: {tong_doanh_thu:,.0f} VND")
        return tong_doanh_thu
    def nhap_ve(self):
        ma_ve = input("Nhập mã vé: ")
        ten_khach_hang = input("Nhập tên khách hàng: ")
        chuyen_di = input("Nhập chuyến đi (ví dụ: Hà Nội - Sài Gòn): ")
        while True:
            try:
                gia_ve = float(input("Nhập giá vé (VND): "))
                if gia_ve < 0:
                    print("Giá vé không được âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Giá vé không hợp lệ. Vui lòng nhập lại.")
        return Ve(ma_ve, ten_khach_hang, chuyen_di, gia_ve)

def menu():
    ql_ve = QuanLyVe()
    while True:
        print("\n--- HỆ THỐNG QUẢN LÝ BÁN VÉ ---")
        print("1. Thêm vé")
        print("2. Cập nhật vé")
        print("3. Xóa vé")
        print("4. Tìm kiếm vé theo khách hàng")
        print("5. In tất cả vé đã bán")
        print("6. Thống kê doanh thu")
        print("7. Thoát")
        choice = input("Chọn chức năng (1-7): ")

        if choice == '1':
            ve_moi = ql_ve.nhap_ve()
            ql_ve.them_ve(ve_moi)
        elif choice == '2':
            ma_ve = input("Nhập mã vé cần cập nhật: ")
            ten_khach_hang_moi = input("Nhập tên khách hàng mới (hoặc để trống nếu không đổi): ")
            chuyen_di_moi = input("Nhập chuyến đi mới (hoặc để trống nếu không đổi): ")
            gia_ve_moi_input = input("Nhập giá vé mới (hoặc để trống nếu không đổi): ")
            gia_ve_moi = float(gia_ve_moi_input) if gia_ve_moi_input else None
            ql_ve.cap_nhat_ve(ma_ve, ten_khach_hang_moi or None, chuyen_di_moi or None, gia_ve_moi)
        elif choice == '3':
            ma_ve = input("Nhập mã vé cần xóa: ")
            ql_ve.xoa_ve(ma_ve)
        elif choice == '4':
            ten_khach_hang = input("Nhập tên khách hàng cần tìm kiếm: ")
            ql_ve.tim_kiem_ve_theo_khach_hang(ten_khach_hang)
        elif choice == '5':
            ql_ve.in_tat_ca_ve()
        elif choice == '6':
            ql_ve.thong_ke_doanh_thu()
        elif choice == '7':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    menu()
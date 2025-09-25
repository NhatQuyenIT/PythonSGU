# Hệ thống quản lý thư viện sách

class Sach:
    def __init__(self, ma_sach, ten_sach, tac_gia, gia_bia, so_luong_ton):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.gia_bia = gia_bia
        self.so_luong_ton = so_luong_ton

    def hien_thi_thong_tin(self):
        print(f"Mã Sách: {self.ma_sach} - Tên cuốn sách: {self.ten_sach} - Tác giả: {self.tac_gia}")
        print(f"Giá bìa: {self.gia_bia:,.0f} VND - Tồn kho: {self.so_luong_ton}")

class ThuVien:
    def __init__(self):
        self.danh_sach_sach = []

    def them_sach(self, sach):
        self.danh_sach_sach.append(sach)

    def hien_thi_danh_sach(self):
        for sach in self.danh_sach_sach:
            sach.hien_thi_thong_tin()
            print("-" * 30)
        else:
            print("Danh sách sách trống.")
            
    def tim_kiem_sach(self, tu_khoa):
        ket_qua = []
        for sach in self.danh_sach_sach:
            if tu_khoa.lower() in sach.ten_sach.lower() or \
                tu_khoa.lower() == sach.ma_sach.lower():
                 ket_qua.append(sach)
        if ket_qua:
            print(f"\n--- KẾT QUẢ TÌM KIẾM cho '{tu_khoa}' ---")
            for sach in ket_qua:
                sach.hien_thi_thong_tin()
                print("-" * 30)
        else:
            print(f"Không tìm thấy sách nào với từ khóa '{tu_khoa}'.")
    
    def cap_nhat_sach(self, ma_sach, ten_moi=None, tac_gia_moi=None, gia_moi=None, so_luong_moi=None):
        for sach in self.danh_sach_sach:
            if sach.ma_sach == ma_sach:
                if ten_moi is not None:
                    sach.ten_sach = ten_moi
                if tac_gia_moi is not None:
                    sach.tac_gia = tac_gia_moi
                if gia_moi is not None:
                    sach.gia_bia = gia_moi
                if so_luong_moi is not None:
                    sach.so_luong_ton = so_luong_moi
                print(f"Đã cập nhật thông tin cho sách '{sach.ten_sach}' (Mã: {ma_sach}).")
                return
        print(f"Không tìm thấy sách có mã {ma_sach}.")
    
    def xoa_sach(self, ma_sach):
        initial_len = len(self.danh_sach_sach)
        self.danh_sach_sach = [sach for sach in self.danh_sach_sach if sach.ma_sach != ma_sach]
        if len(self.danh_sach_sach) < initial_len:
            print(f"Đã xóa sách có mã {ma_sach}.")
        else:
            print(f"Không tìm thấy sách có mã {ma_sach}.")
    
    def nhap_sach(self):
        ma_sach = input("Nhập mã sách: ")
        ten_sach = input("Nhập tên cuốn sách: ")
        tac_gia = input("Nhập tác giả: ")
        gia_bia = float(input("Nhập giá bìa: "))
        so_luong_ton = int(input("Nhập số lượng tồn kho: "))
        return Sach(ma_sach, ten_sach, tac_gia, gia_bia, so_luong_ton)
    
def menu():
    ql_thuvien = ThuVien()
    while True:
        print("\n--- QUẢN LÝ THƯ VIỆN SÁCH ---")
        print("1. Thêm sách mới")
        print("2. Cập nhật thông tin sách")
        print("3. Xóa sách")
        print("4. Tìm kiếm sách")
        print("5. Hiển thị danh sách sách")
        print("6. Thoát")
        choice = input("Chọn một tùy chọn (1-6): ")
        if choice == '1':
            sach_moi = ql_thuvien.nhap_sach()
            ql_thuvien.them_sach(sach_moi)
            print(f"Đã thêm sách: {sach_moi.ten_sach}")
        elif choice == '2':
            ma_sach = input("Nhập mã sách cần cập nhật: ")
            ten_moi = input("Nhập tên sách mới (hoặc để trống để giữ nguyên): ")
            tac_gia_moi = input("Nhập tác giả mới (hoặc để trống để giữ nguyên): ")
            gia_moi_input = input("Nhập giá bìa mới (hoặc để trống để giữ nguyên): ")
            so_luong_moi_input = input("Nhập số lượng tồn kho mới (hoặc để trống để giữ nguyên): ")
            gia_moi = float(gia_moi_input) if gia_moi_input else None
            so_luong_moi = int(so_luong_moi_input) if so_luong_moi_input else None
            ql_thuvien.cap_nhat_sach(ma_sach, ten_moi or None, tac_gia_moi or None, gia_moi, so_luong_moi)
        elif choice == '3':
            ma_sach = input("Nhập mã sách cần xóa: ")
            ql_thuvien.xoa_sach(ma_sach)
        elif choice == '4':
            tu_khoa = input("Nhập từ khóa tìm kiếm (mã sách hoặc tên sách): ")
            ql_thuvien.tim_kiem_sach(tu_khoa)
        elif choice == '5':
            ql_thuvien.hien_thi_danh_sach()
        elif choice == '6':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    menu()    
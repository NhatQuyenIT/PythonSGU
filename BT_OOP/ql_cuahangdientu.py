# Quản lý bán điện thoại / máy tính / văn phòng phẩm
# Lưu trữ thông tin sản phẩm, khách hàng, đơn hàng
# Thêm, sửa, xóa thông tin sản phẩm, khách hàng, đơn hàng
# Tìm kiếm sản phẩm theo tên, loại, giá
# Thống kê doanh thu theo ngày, tháng, năm

class SanPham:
    def __init__(self, ma_sp, ten_sp, loai_sp, gia_sp, so_luong):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.loai_sp = loai_sp
        self.gia_sp = gia_sp
        self.so_luong = so_luong

    def hien_thi_thong_tin(self):
        print(f"Mã SP: {self.ma_sp}, Tên SP: {self.ten_sp}, Loại SP: {self.loai_sp}, Giá SP: {self.gia_sp:,.0f} VND, Số lượng: {self.so_luong}")
        print("-" * 50)
        
class QuanLyCuaHang:
    def __init__(self):
        self.danh_sach_san_pham = []

    def them_san_pham(self, san_pham):
        self.danh_sach_san_pham.append(san_pham)
        print(f"Đã thêm sản phẩm: {san_pham.ten_sp}")

    def cap_nhat_san_pham(self, ma_sp, ten_sp_moi=None, loai_sp_moi=None, gia_sp_moi=None, so_luong_moi=None):
        for sp in self.danh_sach_san_pham:
            if sp.ma_sp == ma_sp:
                if ten_sp_moi is not None:
                    sp.ten_sp = ten_sp_moi
                if loai_sp_moi is not None:
                    sp.loai_sp = loai_sp_moi
                if gia_sp_moi is not None:
                    sp.gia_sp = gia_sp_moi
                if so_luong_moi is not None:
                    sp.so_luong = so_luong_moi
                print(f"Đã cập nhật thông tin sản phẩm '{ma_sp}'.")
                return
        print(f"Không tìm thấy sản phẩm có mã {ma_sp}.")

    def xoa_san_pham(self, ma_sp):
        for sp in self.danh_sach_san_pham:
            if sp.ma_sp == ma_sp:
                self.danh_sach_san_pham.remove(sp)
                print(f"Đã xóa sản phẩm có mã {ma_sp}.")
                return
        print(f"Không tìm thấy sản phẩm có mã {ma_sp}.")

    def tim_kiem_san_pham_theo_ten(self, ten_sp):
        ket_qua = [sp for sp in self.danh_sach_san_pham if ten_sp.lower() in sp.ten_sp.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} sản phẩm có chứa từ khóa '{ten_sp}':")
            for sp in ket_qua:
                sp.hien_thi_thong_tin()
        else:
            print(f"Không tìm thấy sản phẩm nào có chứa từ khóa '{ten_sp}'.")

    def in_tat_ca_san_pham(self):
        if not self.danh_sach_san_pham:
            print("Chưa có sản phẩm nào được thêm.")
            return
        print("Danh sách tất cả các sản phẩm:")
        for sp in self.danh_sach_san_pham:
            sp.hien_thi_thong_tin()
    def thong_ke_tong_gia_tri_kho(self):
        tong_gia_tri = sum(sp.gia_sp * sp.so_luong for sp in self.danh_sach_san_pham)
        print(f"Tổng giá trị kho hàng: {tong_gia_tri:,.0f} VND")
        return tong_gia_tri
    def thong_ke_so_luong_theo_loai(self):
        loai_dict = {}
        for sp in self.danh_sach_san_pham:
            if sp.loai_sp in loai_dict:
                loai_dict[sp.loai_sp] += sp.so_luong
            else:
                loai_dict[sp.loai_sp] = sp.so_luong
        print("Thống kê số lượng sản phẩm theo loại:")
        for loai, so_luong in loai_dict.items():
            print(f"Loại: {loai}, Số lượng: {so_luong}")
        return loai_dict
    def thong_ke_san_pham_gia_cao_nhat(self):
        if not self.danh_sach_san_pham:
            print("Chưa có sản phẩm nào được thêm.")
            return None
        sp_gia_cao_nhat = max(self.danh_sach_san_pham, key=lambda sp: sp.gia_sp)
        print("Sản phẩm có giá cao nhất:")
        sp_gia_cao_nhat.hien_thi_thong_tin()
        return sp_gia_cao_nhat
    def thong_ke_san_pham_gia_thap_nhat(self):
        if not self.danh_sach_san_pham:
            print("Chưa có sản phẩm nào được thêm.")
            return None
        sp_gia_thap_nhat = min(self.danh_sach_san_pham, key=lambda sp: sp.gia_sp)
        print("Sản phẩm có giá thấp nhất:")
        sp_gia_thap_nhat.hien_thi_thong_tin()
        return sp_gia_thap_nhat
    def thong_ke_so_luong_tong(self):
        tong_so_luong = sum(sp.so_luong for sp in self.danh_sach_san_pham)
        print(f"Tổng số lượng sản phẩm trong kho: {tong_so_luong}")
        return tong_so_luong
    def thong_ke_so_luong_hethang(self):
        hethang_list = [sp for sp in self.danh_sach_san_pham if sp.so_luong == 0]
        if hethang_list:
            print(f"Có {len(hethang_list)} sản phẩm hết hàng:")
            for sp in hethang_list:
                sp.hien_thi_thong_tin()
        else:
            print("Không có sản phẩm nào hết hàng.")
        return hethang_list
    
    def nhap_san_pham(self):
        ma_sp = input("Nhập mã sản phẩm: ")
        ten_sp = input("Nhập tên sản phẩm: ")
        loai_sp = input("Nhập loại sản phẩm (ví dụ: Điện thoại, Máy tính, Văn phòng phẩm): ")
        while True:
            try:
                gia_sp = float(input("Nhập giá sản phẩm (VND): "))
                if gia_sp < 0:
                    print("Giá sản phẩm không được âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Giá sản phẩm không hợp lệ. Vui lòng nhập lại.")
        while True:
            try:
                so_luong = int(input("Nhập số lượng sản phẩm: "))
                if so_luong < 0:
                    print("Số lượng không được âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Số lượng không hợp lệ. Vui lòng nhập lại.")
        return SanPham(ma_sp, ten_sp, loai_sp, gia_sp, so_luong)
    
    
if __name__ == "__main__":
    ql_ch = QuanLyCuaHang()
    
    while True:
        print("\n--- Quản Lý Cửa Hàng Điện Tử ---")
        print("1. Thêm sản phẩm")
        print("2. Cập nhật sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Tìm kiếm sản phẩm theo tên")
        print("5. In tất cả sản phẩm")
        print("6. Thống kê tổng giá trị kho hàng")
        print("7. Thống kê số lượng theo loại")
        print("8. Thống kê sản phẩm giá cao nhất")
        print("9. Thống kê sản phẩm giá thấp nhất")
        print("10. Thống kê tổng số lượng sản phẩm")
        print("11. Thống kê sản phẩm hết hàng")
        print("0. Thoát")
        
        choice = input("Chọn chức năng (0-11): ")
        
        if choice == '1':
            sp = ql_ch.nhap_san_pham()
            ql_ch.them_san_pham(sp)
        elif choice == '2':
            ma_sp = input("Nhập mã sản phẩm cần cập nhật: ")
            ten_sp_moi = input("Nhập tên sản phẩm mới (hoặc để trống nếu không đổi): ") or None
            loai_sp_moi = input("Nhập loại sản phẩm mới (hoặc để trống nếu không đổi): ") or None
            gia_sp_moi = input("Nhập giá sản phẩm mới (hoặc để trống nếu không đổi): ")
            gia_sp_moi = float(gia_sp_moi) if gia_sp_moi else None
            so_luong_moi = input("Nhập số lượng mới (hoặc để trống nếu không đổi): ")
            so_luong_moi = int(so_luong_moi) if so_luong_moi else None
            ql_ch.cap_nhat_san_pham(ma_sp, ten_sp_moi, loai_sp_moi, gia_sp_moi, so_luong_moi)
        elif choice == '3':
            ma_sp = input("Nhập mã sản phẩm cần xóa: ")
            ql_ch.xoa_san_pham(ma_sp)
        elif choice == '4':
            ten_sp = input("Nhập tên sản phẩm cần tìm kiếm: ")
            ql_ch.tim_kiem_san_pham(ten_sp)
        elif choice == '5':
            ql_ch.in_tat_ca_san_pham()
        elif choice == '6':
            ql_ch.thong_ke_tong_gia_tri_kho()
        elif choice == '7':
            ql_ch.thong_ke_so_luong_theo_loai()
        elif choice == '8':
            ql_ch.thong_ke_san_pham_gia_cao_nhat()
        elif choice == '9':
            ql_ch.thong_ke_san_pham_gia_thap_nhat()
        elif choice == '10':
            ql_ch.thong_ke_so_luong_tong()
        elif choice == '11':
            ql_ch.thong_ke_so_luong_hethang()
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

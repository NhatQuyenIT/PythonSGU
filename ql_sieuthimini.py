# Hệ thống Quản lý Siêu thị Mini

class SanPham:
    def __init__(self, ma_sp, ten_sp, gia, so_luong_ton):
        self.ma_sp = ma_sp
        self.ten_sp = ten_sp
        self.gia = gia
        self.so_luong_ton = so_luong_ton

    def hien_thi_thong_tin(self):
        print(f"Mã SP: {self.ma_sp} - Tên: {self.ten_sp}")
        print(f"Giá: {self.gia:,.0f} VND - Tồn kho: {self.so_luong_ton}")
        
class SanPhamDienTu(SanPham):
    def __init__(self, ma_sp, ten_sp, gia, so_luong_ton, bao_hanh):
        super().__init__(ma_sp, ten_sp, gia, so_luong_ton)
        self.bao_hanh = bao_hanh         

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"Bảo hành: {self.bao_hanh} tháng")

class ThucPham(SanPham):
    def __init__(self, ma_sp, ten_sp, gia, so_luong_ton, ngay_het_han):
        super().__init__(ma_sp, ten_sp, gia, so_luong_ton)
        self.ngay_het_han = ngay_het_han

    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin()
        print(f"Hạn sử dụng: {self.ngay_het_han}")

class KhoHang:
    def __init__(self):
        self.danh_sach_san_pham = []

    def them_san_pham(self, san_pham):
        self.danh_sach_san_pham.append(san_pham)
        print(f"Đã thêm sản phẩm: {san_pham.ten_sp}")
    
    def cap_nhat_san_pham(self, ma_sp, ten_moi=None, gia_moi=None, so_luong_moi=None, bao_hanh_moi=None, ngay_het_han_moi=None):
        for sp in self.danh_sach_san_pham:
            if sp.ma_sp == ma_sp:
                if ten_moi is not None:
                    sp.ten_sp = ten_moi
                if gia_moi is not None:
                    sp.gia = gia_moi
                if so_luong_moi is not None:
                    sp.so_luong_ton = so_luong_moi

                # Nếu sản phẩm là điện tử
                if isinstance(sp, SanPhamDienTu) and bao_hanh_moi is not None:
                    sp.bao_hanh = bao_hanh_moi

                # Nếu sản phẩm là thực phẩm
                if isinstance(sp, ThucPham) and ngay_het_han_moi is not None:
                    sp.ngay_het_han = ngay_het_han_moi

                print(f"Đã cập nhật thông tin cho sản phẩm '{sp.ten_sp}' (Mã: {ma_sp}).")
                return
        print(f"Không tìm thấy sản phẩm có mã {ma_sp}.")

    
    def xoa_san_pham(self, ma_sp):
        initial_len = len(self.danh_sach_san_pham)
        self.danh_sach_san_pham = [sp for sp in self.danh_sach_san_pham if sp.ma_sp != ma_sp]
        if len(self.danh_sach_san_pham) < initial_len:
            print(f"Đã xóa sản phẩm có mã {ma_sp}.")
        else:
            print(f"Không tìm thấy sản phẩm có mã {ma_sp}.")
    
    def tim_kiem_san_pham(self, tu_khoa):
        ket_qua = []
        for sp in self.danh_sach_san_pham:
            if tu_khoa.lower() in sp.ten_sp.lower() or \
               tu_khoa.lower() == sp.ma_sp.lower():
                ket_qua.append(sp)
        if ket_qua:
            print(f"\n--- KẾT QUẢ TÌM KIẾM cho '{tu_khoa}' ---")
            for sp in ket_qua:
                sp.hien_thi_thong_tin() # Tính đa hình
                print("-" * 30)
        else:
            print(f"Không tìm thấy sản phẩm nào với từ khóa '{tu_khoa}'.")
            
    def nhap_san_pham(self):
        print("Chọn loại sản phẩm:")
        print("1. Sản phẩm thường")
        print("2. Sản phẩm điện tử")
        print("3. Thực phẩm")
        loai = input("Nhập lựa chọn: ")

        ma_sp = input("Nhập mã sản phẩm: ")
        ten_sp = input("Nhập tên sản phẩm: ")
        gia = float(input("Nhập giá sản phẩm: "))
        so_luong_ton = int(input("Nhập số lượng tồn kho: "))

        if loai == "2":
            bao_hanh = int(input("Nhập thời gian bảo hành (tháng): "))
            return SanPhamDienTu(ma_sp, ten_sp, gia, so_luong_ton, bao_hanh)
        elif loai == "3":
            ngay_het_han = input("Nhập ngày hết hạn (dd/mm/yyyy): ")
            return ThucPham(ma_sp, ten_sp, gia, so_luong_ton, ngay_het_han)
        else:
            return SanPham(ma_sp, ten_sp, gia, so_luong_ton)

    
    def hien_thi_danh_sach(self):
        if not self.danh_sach_san_pham:
            print("Danh sách sản phẩm trống.")
            return
        print("\n--- DANH SÁCH SẢN PHẨM ---")
        for sp in self.danh_sach_san_pham:
            sp.hien_thi_thong_tin()
            print("-" * 30)
    def muahang(self, ma_sp, so_luong):
        for sp in self.danh_sach_san_pham:
            if sp.ma_sp == ma_sp:
                if sp.so_luong_ton >= so_luong:
                    sp.so_luong_ton -= so_luong
                    tong_tien = so_luong * sp.gia
                    print(f"Đã mua {so_luong} của '{sp.ten_sp}'. Tổng tiền: {tong_tien:,.0f} VND.")
                else:
                    print(f"Số lượng tồn kho không đủ. Hiện có: {sp.so_luong_ton}.")
                return
        print(f"Không tìm thấy sản phẩm có mã {ma_sp}.")
        
    def tinh_tong_tien_cac_sp(self, danh_sach_mua):
        tong_tien_all = 0
        for ma_sp, so_luong in danh_sach_mua:
            for sp in self.danh_sach_san_pham:
                if sp.ma_sp == ma_sp:
                    if sp.so_luong_ton >= so_luong:
                        sp.so_luong_ton -= so_luong
                        tong_tien = so_luong * sp.gia
                        tong_tien_all += tong_tien
                        print(f"Đã mua {so_luong} của '{sp.ten_sp}'. Tổng tiền: {tong_tien:,.0f} VND.")
                    else:
                        print(f"Số lượng tồn kho không đủ cho '{sp.ten_sp}'. Hiện có: {sp.so_luong_ton}.")
                    break
            else:
                print(f"Không tìm thấy sản phẩm có mã {ma_sp}.")
        print(f"\nTổng tiền tất cả sản phẩm đã mua: {tong_tien_all:,.0f} VND.")
    

def menu():
    ql_sieuthimini = KhoHang()
    while True:
        print("\n--- QUẢN LÝ SIÊU THỊ MINI ---")
        print("1. Thêm sản phẩm")
        print("2. Cập nhật sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Tìm kiếm thông tin chi tiết sản phẩm")
        print("5. Hiển thị danh sách sản phẩm")
        print("6. Mua hàng")
        print("0. Thoát")
        lua_chon = input("Nhập lựa chọn của bạn: ")
        if lua_chon == "1":
            san_pham_moi = ql_sieuthimini.nhap_san_pham()
            ql_sieuthimini.them_san_pham(san_pham_moi)
        elif lua_chon == "2":
            ma_sp = input("Nhập mã sản phẩm cần cập nhật: ")
            ten_moi = input("Nhập tên mới (hoặc để trống nếu không đổi): ")
            gia_moi = input("Nhập giá mới (hoặc để trống nếu không đổi): ")
            so_luong_moi = input("Nhập số lượng tồn kho mới (hoặc để trống nếu không đổi): ")

            bao_hanh_moi = input("Nhập số tháng bảo hành (chỉ cho sản phẩm điện tử, để trống nếu không đổi): ")
            ngay_het_han_moi = input("Nhập hạn sử dụng (chỉ cho thực phẩm, để trống nếu không đổi): ")

            # Xử lý kiểu dữ liệu
            ten_moi = ten_moi if ten_moi else None
            gia_moi = float(gia_moi) if gia_moi else None
            so_luong_moi = int(so_luong_moi) if so_luong_moi else None
            bao_hanh_moi = int(bao_hanh_moi) if bao_hanh_moi else None
            ngay_het_han_moi = ngay_het_han_moi if ngay_het_han_moi else None

            ql_sieuthimini.cap_nhat_san_pham(ma_sp, ten_moi, gia_moi, so_luong_moi, bao_hanh_moi, ngay_het_han_moi)
        elif lua_chon == "3":
            ma_sp = input("Nhập mã sản phẩm cần xóa: ")
            ql_sieuthimini.xoa_san_pham(ma_sp)
        elif lua_chon == "4":
            tu_khoa = input("Nhập từ khóa tìm kiếm: ")
            ql_sieuthimini.tim_kiem_san_pham(tu_khoa)
        elif lua_chon == "5":
            ql_sieuthimini.hien_thi_danh_sach()
        elif lua_chon == "6":
            print("Nhập thông tin các sản phẩm muốn mua (để trống mã sản phẩm hoặc nhập '0' để kết thúc)")
            danh_sach_mua = []
            while True:
                ma_sp = input("Nhập mã sản phẩm muốn mua: ")
                if not ma_sp or ma_sp == "0":
                    break
                try:
                    so_luong = int(input("Nhập số lượng muốn mua: "))
                except ValueError:
                    print("Số lượng không hợp lệ. Vui lòng nhập lại.")
                    continue
                danh_sach_mua.append((ma_sp, so_luong))
            if danh_sach_mua:
                ql_sieuthimini.tinh_tong_tien_cac_sp(danh_sach_mua)
            else:
                print("Không có sản phẩm nào được mua.")
        elif lua_chon == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    menu()
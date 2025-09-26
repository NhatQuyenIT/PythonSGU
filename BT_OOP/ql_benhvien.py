# Quản lý phòng khám bệnh / khu vực lấy thuốc y tế
# Lưu trữ thông tin bệnh nhân, bác sĩ, lịch hẹn
# Thêm, sửa, xóa thông tin bệnh nhân, bác sĩ, lịch hẹn
# Tìm kiếm bệnh nhân theo tên, mã bệnh nhân
# Thống kê doanh thu theo ngày, tháng, năm

# Hệ thống quản lý bệnh viện
from datetime import datetime

class BenhNhan:
    def __init__(self, ma_benh_nhan, ten_benh_nhan, tuoi, gioi_tinh, dia_chi="", so_dien_thoai=""):
        self.ma_benh_nhan = ma_benh_nhan
        self.ten_benh_nhan = ten_benh_nhan
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.so_dien_thoai = so_dien_thoai

    def hien_thi_thong_tin(self):
        thong_tin = f"Mã BN: {self.ma_benh_nhan}, Tên: {self.ten_benh_nhan}, Tuổi: {self.tuoi}, Giới tính: {self.gioi_tinh}"
        if self.dia_chi:
            thong_tin += f", Địa chỉ: {self.dia_chi}"
        if self.so_dien_thoai:
            thong_tin += f", SĐT: {self.so_dien_thoai}"
        print(thong_tin)
        print("-" * 50)

class BacSi:
    def __init__(self, ma_bac_si, ten_bac_si, chuyen_khoa, gia_kham):
        self.ma_bac_si = ma_bac_si
        self.ten_bac_si = ten_bac_si
        self.chuyen_khoa = chuyen_khoa
        self.gia_kham = gia_kham

    def hien_thi_thong_tin(self):
        print(f"Mã BS: {self.ma_bac_si}, Tên: {self.ten_bac_si}, Chuyên khoa: {self.chuyen_khoa}, Giá khám: {self.gia_kham:,.0f} VND")
        print("-" * 50)

class LichHen:
    def __init__(self, ma_lich_hen, ma_benh_nhan, ma_bac_si, ngay_gio, ly_do_kham):
        self.ma_lich_hen = ma_lich_hen
        self.ma_benh_nhan = ma_benh_nhan
        self.ma_bac_si = ma_bac_si
        self.ngay_gio = ngay_gio
        self.ly_do_kham = ly_do_kham
        self.trang_thai = "Đã đặt"  # Đã đặt, Đã khám, Hủy

    def hien_thi_thong_tin(self):
        print(f"Mã lịch hẹn: {self.ma_lich_hen}, BN: {self.ma_benh_nhan}, BS: {self.ma_bac_si}")
        print(f"Ngày giờ: {self.ngay_gio}, Lý do: {self.ly_do_kham}, Trạng thái: {self.trang_thai}")
        print("-" * 50)

class Thuoc:
    def __init__(self, ma_thuoc, ten_thuoc, don_vi, gia_ban, so_luong_ton, mo_ta="", cong_dung=""):
        self.ma_thuoc = ma_thuoc
        self.ten_thuoc = ten_thuoc
        self.don_vi = don_vi  # viên, lọ, túi, v.v.
        self.gia_ban = gia_ban
        self.so_luong_ton = so_luong_ton
        self.mo_ta = mo_ta
        self.cong_dung = cong_dung

    def hien_thi_thong_tin(self):
        print(f"Mã thuốc: {self.ma_thuoc}, Tên: {self.ten_thuoc}, Đơn vị: {self.don_vi}")
        print(f"Giá bán: {self.gia_ban:,.0f} VND/{self.don_vi}, Tồn kho: {self.so_luong_ton}")
        if self.mo_ta:
            print(f"Mô tả: {self.mo_ta}")
        if self.cong_dung:
            print(f"Công dụng: {self.cong_dung}")
        print("-" * 50)

class ChiTietDonThuoc:
    def __init__(self, ma_thuoc, so_luong, cach_dung, ghi_chu=""):
        self.ma_thuoc = ma_thuoc
        self.so_luong = so_luong
        self.cach_dung = cach_dung  # VD: "Sáng 1 viên, chiều 1 viên, sau ăn"
        self.ghi_chu = ghi_chu

    def hien_thi_thong_tin(self):
        print(f"  - Mã thuốc: {self.ma_thuoc}, Số lượng: {self.so_luong}")
        print(f"    Cách dùng: {self.cach_dung}")
        if self.ghi_chu:
            print(f"    Ghi chú: {self.ghi_chu}")

class DonThuoc:
    def __init__(self, ma_don_thuoc, ma_lich_hen, ma_benh_nhan, ma_bac_si, ngay_ke):
        self.ma_don_thuoc = ma_don_thuoc
        self.ma_lich_hen = ma_lich_hen
        self.ma_benh_nhan = ma_benh_nhan
        self.ma_bac_si = ma_bac_si
        self.ngay_ke = ngay_ke
        self.danh_sach_thuoc = []  # Danh sách ChiTietDonThuoc
        self.trang_thai = "Chờ lấy thuốc"  # Chờ lấy thuốc, Đã lấy thuốc, Hủy
        self.tong_tien = 0

    def them_thuoc(self, chi_tiet_thuoc):
        self.danh_sach_thuoc.append(chi_tiet_thuoc)

    def tinh_tong_tien(self, danh_sach_thuoc_he_thong):
        self.tong_tien = 0
        for chi_tiet in self.danh_sach_thuoc:
            for thuoc in danh_sach_thuoc_he_thong:
                if thuoc.ma_thuoc == chi_tiet.ma_thuoc:
                    self.tong_tien += thuoc.gia_ban * chi_tiet.so_luong
                    break

    def hien_thi_thong_tin(self, danh_sach_thuoc_he_thong):
        print(f"Đơn thuốc: {self.ma_don_thuoc} | BN: {self.ma_benh_nhan} | BS: {self.ma_bac_si}")
        print(f"Ngày kê: {self.ngay_ke} | Trạng thái: {self.trang_thai}")
        print("Chi tiết thuốc:")
        for chi_tiet in self.danh_sach_thuoc:
            # Tìm thông tin thuốc
            ten_thuoc = "Không tìm thấy"
            gia_thuoc = 0
            for thuoc in danh_sach_thuoc_he_thong:
                if thuoc.ma_thuoc == chi_tiet.ma_thuoc:
                    ten_thuoc = thuoc.ten_thuoc
                    gia_thuoc = thuoc.gia_ban
                    break
            print(f"  - {ten_thuoc} x{chi_tiet.so_luong} = {gia_thuoc * chi_tiet.so_luong:,.0f} VND")
            print(f"    Cách dùng: {chi_tiet.cach_dung}")
            if chi_tiet.ghi_chu:
                print(f"    Ghi chú: {chi_tiet.ghi_chu}")
        print(f"Tổng tiền: {self.tong_tien:,.0f} VND")
        print("-" * 50)
        
class QuanLyBenhVien:
    def __init__(self):
        self.danh_sach_benh_nhan = []
        self.danh_sach_bac_si = []
        self.danh_sach_lich_hen = []
        self.danh_sach_thuoc = []
        self.danh_sach_don_thuoc = []
    def them_benh_nhan(self, benh_nhan):
        self.danh_sach_benh_nhan.append(benh_nhan)
        print(f"Đã thêm bệnh nhân: {benh_nhan.ten_benh_nhan}")
    def cap_nhat_benh_nhan(self, ma_benh_nhan, ten_benh_nhan_moi=None, tuoi_moi=None, gioi_tinh_moi=None):
        for benh_nhan in self.danh_sach_benh_nhan:
            if benh_nhan.ma_benh_nhan == ma_benh_nhan:
                if ten_benh_nhan_moi is not None:
                    benh_nhan.ten_benh_nhan = ten_benh_nhan_moi
                if tuoi_moi is not None:
                    benh_nhan.tuoi = tuoi_moi
                if gioi_tinh_moi is not None:
                    benh_nhan.gioi_tinh = gioi_tinh_moi
                print(f"Đã cập nhật thông tin bệnh nhân '{ma_benh_nhan}'.")
                return
        print(f"Không tìm thấy bệnh nhân có mã {ma_benh_nhan}.")
    def xoa_benh_nhan(self, ma_benh_nhan):
        for benh_nhan in self.danh_sach_benh_nhan:
            if benh_nhan.ma_benh_nhan == ma_benh_nhan:
                self.danh_sach_benh_nhan.remove(benh_nhan)
                print(f"Đã xóa bệnh nhân có mã {ma_benh_nhan}.")
                return
        print(f"Không tìm thấy bệnh nhân có mã {ma_benh_nhan}.")
    def tim_kiem_benh_nhan_theo_ten(self, ten_benh_nhan):
        ket_qua = [benh_nhan for benh_nhan in self.danh_sach_benh_nhan if ten_benh_nhan.lower() in benh_nhan.ten_benh_nhan.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} bệnh nhân có chứa từ khóa '{ten_benh_nhan}':")
            for benh_nhan in ket_qua:
                benh_nhan.hien_thi_thong_tin()
        else:
            print(f"Không tìm thấy bệnh nhân nào có chứa từ khóa '{ten_benh_nhan}'.")
    def in_tat_ca_benh_nhan(self):
        if not self.danh_sach_benh_nhan:
            print("Chưa có bệnh nhân nào được thêm.")
            return
        print("Danh sách tất cả các bệnh nhân:")
        for benh_nhan in self.danh_sach_benh_nhan:
            benh_nhan.hien_thi_thong_tin()

    # Quản lý bác sĩ
    def them_bac_si(self, bac_si):
        self.danh_sach_bac_si.append(bac_si)
        print(f"Đã thêm bác sĩ: {bac_si.ten_bac_si}")

    def cap_nhat_bac_si(self, ma_bac_si, ten_bac_si_moi=None, chuyen_khoa_moi=None, gia_kham_moi=None):
        for bac_si in self.danh_sach_bac_si:
            if bac_si.ma_bac_si == ma_bac_si:
                if ten_bac_si_moi is not None:
                    bac_si.ten_bac_si = ten_bac_si_moi
                if chuyen_khoa_moi is not None:
                    bac_si.chuyen_khoa = chuyen_khoa_moi
                if gia_kham_moi is not None:
                    bac_si.gia_kham = gia_kham_moi
                print(f"Đã cập nhật thông tin bác sĩ '{ma_bac_si}'.")
                return
        print(f"Không tìm thấy bác sĩ có mã {ma_bac_si}.")

    def xoa_bac_si(self, ma_bac_si):
        for bac_si in self.danh_sach_bac_si:
            if bac_si.ma_bac_si == ma_bac_si:
                self.danh_sach_bac_si.remove(bac_si)
                print(f"Đã xóa bác sĩ có mã {ma_bac_si}.")
                return
        print(f"Không tìm thấy bác sĩ có mã {ma_bac_si}.")

    def tim_kiem_bac_si_theo_chuyen_khoa(self, chuyen_khoa):
        ket_qua = [bac_si for bac_si in self.danh_sach_bac_si if chuyen_khoa.lower() in bac_si.chuyen_khoa.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} bác sĩ chuyên khoa '{chuyen_khoa}':")
            for bac_si in ket_qua:
                bac_si.hien_thi_thong_tin()
        else:
            print(f"Không tìm thấy bác sĩ chuyên khoa '{chuyen_khoa}'.")

    def in_tat_ca_bac_si(self):
        if not self.danh_sach_bac_si:
            print("Chưa có bác sĩ nào được thêm.")
            return
        print("Danh sách tất cả các bác sĩ:")
        for bac_si in self.danh_sach_bac_si:
            bac_si.hien_thi_thong_tin()

    # Quản lý lịch hẹn
    def dat_lich_hen(self, lich_hen):
        # Kiểm tra bệnh nhân và bác sĩ có tồn tại không
        benh_nhan_ton_tai = any(bn.ma_benh_nhan == lich_hen.ma_benh_nhan for bn in self.danh_sach_benh_nhan)
        bac_si_ton_tai = any(bs.ma_bac_si == lich_hen.ma_bac_si for bs in self.danh_sach_bac_si)
        
        if not benh_nhan_ton_tai:
            print(f"Không tìm thấy bệnh nhân có mã {lich_hen.ma_benh_nhan}.")
            return False
        if not bac_si_ton_tai:
            print(f"Không tìm thấy bác sĩ có mã {lich_hen.ma_bac_si}.")
            return False
            
        self.danh_sach_lich_hen.append(lich_hen)
        print(f"Đã đặt lịch hẹn {lich_hen.ma_lich_hen} thành công.")
        return True

    def cap_nhat_trang_thai_lich_hen(self, ma_lich_hen, trang_thai_moi):
        for lich_hen in self.danh_sach_lich_hen:
            if lich_hen.ma_lich_hen == ma_lich_hen:
                lich_hen.trang_thai = trang_thai_moi
                print(f"Đã cập nhật trạng thái lịch hẹn '{ma_lich_hen}' thành '{trang_thai_moi}'.")
                return
        print(f"Không tìm thấy lịch hẹn có mã {ma_lich_hen}.")

    def huy_lich_hen(self, ma_lich_hen):
        for lich_hen in self.danh_sach_lich_hen:
            if lich_hen.ma_lich_hen == ma_lich_hen:
                lich_hen.trang_thai = "Hủy"
                print(f"Đã hủy lịch hẹn {ma_lich_hen}.")
                return
        print(f"Không tìm thấy lịch hẹn có mã {ma_lich_hen}.")

    def in_lich_hen_theo_benh_nhan(self, ma_benh_nhan):
        ket_qua = [lh for lh in self.danh_sach_lich_hen if lh.ma_benh_nhan == ma_benh_nhan]
        if ket_qua:
            print(f"Lịch hẹn của bệnh nhân {ma_benh_nhan}:")
            for lich_hen in ket_qua:
                lich_hen.hien_thi_thong_tin()
        else:
            print(f"Không có lịch hẹn nào cho bệnh nhân {ma_benh_nhan}.")

    def in_tat_ca_lich_hen(self):
        if not self.danh_sach_lich_hen:
            print("Chưa có lịch hẹn nào.")
            return
        print("Danh sách tất cả lịch hẹn:")
        for lich_hen in self.danh_sach_lich_hen:
            lich_hen.hien_thi_thong_tin()

    # Quản lý thuốc
    def them_thuoc(self, thuoc):
        self.danh_sach_thuoc.append(thuoc)
        print(f"Đã thêm thuốc: {thuoc.ten_thuoc}")

    def cap_nhat_thuoc(self, ma_thuoc, ten_thuoc_moi=None, gia_ban_moi=None, so_luong_ton_moi=None, mo_ta_moi=None):
        for thuoc in self.danh_sach_thuoc:
            if thuoc.ma_thuoc == ma_thuoc:
                if ten_thuoc_moi is not None:
                    thuoc.ten_thuoc = ten_thuoc_moi
                if gia_ban_moi is not None:
                    thuoc.gia_ban = gia_ban_moi
                if so_luong_ton_moi is not None:
                    thuoc.so_luong_ton = so_luong_ton_moi
                if mo_ta_moi is not None:
                    thuoc.mo_ta = mo_ta_moi
                print(f"Đã cập nhật thông tin thuốc '{ma_thuoc}'.")
                return
        print(f"Không tìm thấy thuốc có mã {ma_thuoc}.")

    def xoa_thuoc(self, ma_thuoc):
        for thuoc in self.danh_sach_thuoc:
            if thuoc.ma_thuoc == ma_thuoc:
                self.danh_sach_thuoc.remove(thuoc)
                print(f"Đã xóa thuốc có mã {ma_thuoc}.")
                return
        print(f"Không tìm thấy thuốc có mã {ma_thuoc}.")

    def tim_kiem_thuoc_theo_ten(self, ten_thuoc):
        ket_qua = [thuoc for thuoc in self.danh_sach_thuoc if ten_thuoc.lower() in thuoc.ten_thuoc.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} thuốc có chứa từ khóa '{ten_thuoc}':")
            for thuoc in ket_qua:
                thuoc.hien_thi_thong_tin()
        else:
            print(f"Không tìm thấy thuốc nào có chứa từ khóa '{ten_thuoc}'.")

    def in_tat_ca_thuoc(self):
        if not self.danh_sach_thuoc:
            print("Chưa có thuốc nào trong kho.")
            return
        print("Danh sách tất cả thuốc:")
        for thuoc in self.danh_sach_thuoc:
            thuoc.hien_thi_thong_tin()

    def kiem_tra_ton_kho(self, ma_thuoc, so_luong_can):
        for thuoc in self.danh_sach_thuoc:
            if thuoc.ma_thuoc == ma_thuoc:
                if thuoc.so_luong_ton >= so_luong_can:
                    return True
                else:
                    print(f"Thuốc {thuoc.ten_thuoc} chỉ còn {thuoc.so_luong_ton} {thuoc.don_vi}, không đủ {so_luong_can} {thuoc.don_vi}")
                    return False
        print(f"Không tìm thấy thuốc có mã {ma_thuoc}.")
        return False

    # Quản lý đơn thuốc
    def ke_don_thuoc(self, don_thuoc):
        # Kiểm tra lịch hẹn, bệnh nhân, bác sĩ có tồn tại
        lich_hen_ton_tai = any(lh.ma_lich_hen == don_thuoc.ma_lich_hen for lh in self.danh_sach_lich_hen)
        benh_nhan_ton_tai = any(bn.ma_benh_nhan == don_thuoc.ma_benh_nhan for bn in self.danh_sach_benh_nhan)
        bac_si_ton_tai = any(bs.ma_bac_si == don_thuoc.ma_bac_si for bs in self.danh_sach_bac_si)
        
        if not lich_hen_ton_tai:
            print(f"Không tìm thấy lịch hẹn có mã {don_thuoc.ma_lich_hen}.")
            return False
        if not benh_nhan_ton_tai:
            print(f"Không tìm thấy bệnh nhân có mã {don_thuoc.ma_benh_nhan}.")
            return False
        if not bac_si_ton_tai:
            print(f"Không tìm thấy bác sĩ có mã {don_thuoc.ma_bac_si}.")
            return False
            
        # Tính tổng tiền
        don_thuoc.tinh_tong_tien(self.danh_sach_thuoc)
        self.danh_sach_don_thuoc.append(don_thuoc)
        print(f"Đã kê đơn thuốc {don_thuoc.ma_don_thuoc} thành công.")
        return True

    def lay_thuoc(self, ma_don_thuoc):
        for don_thuoc in self.danh_sach_don_thuoc:
            if don_thuoc.ma_don_thuoc == ma_don_thuoc:
                if don_thuoc.trang_thai != "Chờ lấy thuốc":
                    print(f"Đơn thuốc {ma_don_thuoc} đã được xử lý hoặc đã hủy.")
                    return False
                
                # Kiểm tra tồn kho và trừ thuốc
                co_the_lay = True
                for chi_tiet in don_thuoc.danh_sach_thuoc:
                    if not self.kiem_tra_ton_kho(chi_tiet.ma_thuoc, chi_tiet.so_luong):
                        co_the_lay = False
                
                if not co_the_lay:
                    print("Không thể lấy thuốc do không đủ tồn kho.")
                    return False
                
                # Trừ thuốc trong kho
                for chi_tiet in don_thuoc.danh_sach_thuoc:
                    for thuoc in self.danh_sach_thuoc:
                        if thuoc.ma_thuoc == chi_tiet.ma_thuoc:
                            thuoc.so_luong_ton -= chi_tiet.so_luong
                            break
                
                don_thuoc.trang_thai = "Đã lấy thuốc"
                print(f"Đã lấy thuốc cho đơn {ma_don_thuoc} thành công.")
                print(f"Tổng tiền: {don_thuoc.tong_tien:,.0f} VND")
                return True
        
        print(f"Không tìm thấy đơn thuốc có mã {ma_don_thuoc}.")
        return False

    def huy_don_thuoc(self, ma_don_thuoc):
        for don_thuoc in self.danh_sach_don_thuoc:
            if don_thuoc.ma_don_thuoc == ma_don_thuoc:
                don_thuoc.trang_thai = "Hủy"
                print(f"Đã hủy đơn thuốc {ma_don_thuoc}.")
                return
        print(f"Không tìm thấy đơn thuốc có mã {ma_don_thuoc}.")

    def in_don_thuoc_theo_benh_nhan(self, ma_benh_nhan):
        ket_qua = [dt for dt in self.danh_sach_don_thuoc if dt.ma_benh_nhan == ma_benh_nhan]
        if ket_qua:
            print(f"Đơn thuốc của bệnh nhân {ma_benh_nhan}:")
            for don_thuoc in ket_qua:
                don_thuoc.hien_thi_thong_tin(self.danh_sach_thuoc)
        else:
            print(f"Không có đơn thuốc nào cho bệnh nhân {ma_benh_nhan}.")

    def in_tat_ca_don_thuoc(self):
        if not self.danh_sach_don_thuoc:
            print("Chưa có đơn thuốc nào.")
            return
        print("Danh sách tất cả đơn thuốc:")
        for don_thuoc in self.danh_sach_don_thuoc:
            don_thuoc.hien_thi_thong_tin(self.danh_sach_thuoc)

    # Thống kê doanh thu
    def thong_ke_doanh_thu(self):
        # Doanh thu từ khám bệnh
        doanh_thu_kham = 0
        lich_hen_da_kham = [lh for lh in self.danh_sach_lich_hen if lh.trang_thai == "Đã khám"]
        
        for lich_hen in lich_hen_da_kham:
            for bac_si in self.danh_sach_bac_si:
                if bac_si.ma_bac_si == lich_hen.ma_bac_si:
                    doanh_thu_kham += bac_si.gia_kham
                    break
        
        # Doanh thu từ bán thuốc
        doanh_thu_thuoc = 0
        don_thuoc_da_lay = [dt for dt in self.danh_sach_don_thuoc if dt.trang_thai == "Đã lấy thuốc"]
        for don_thuoc in don_thuoc_da_lay:
            doanh_thu_thuoc += don_thuoc.tong_tien
        
        tong_doanh_thu = doanh_thu_kham + doanh_thu_thuoc
        
        print(f"=== THỐNG KÊ DOANH THU ===")
        print(f"Tổng số lịch hẹn: {len(self.danh_sach_lich_hen)}")
        print(f"Số lịch đã khám: {len(lich_hen_da_kham)}")
        print(f"Doanh thu khám bệnh: {doanh_thu_kham:,.0f} VND")
        print(f"Tổng số đơn thuốc: {len(self.danh_sach_don_thuoc)}")
        print(f"Số đơn đã lấy thuốc: {len(don_thuoc_da_lay)}")
        print(f"Doanh thu bán thuốc: {doanh_thu_thuoc:,.0f} VND")
        print(f"TỔNG DOANH THU: {tong_doanh_thu:,.0f} VND")
        return tong_doanh_thu

    # Nhập dữ liệu
    def nhap_benh_nhan(self):
        ma_benh_nhan = input("Nhập mã bệnh nhân: ")
        ten_benh_nhan = input("Nhập tên bệnh nhân: ")
        while True:
            try:
                tuoi = int(input("Nhập tuổi: "))
                if tuoi <= 0:
                    print("Tuổi phải lớn hơn 0. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Tuổi không hợp lệ. Vui lòng nhập lại.")
        gioi_tinh = input("Nhập giới tính (Nam/Nữ): ")
        dia_chi = input("Nhập địa chỉ (có thể để trống): ")
        so_dien_thoai = input("Nhập số điện thoại (có thể để trống): ")
        return BenhNhan(ma_benh_nhan, ten_benh_nhan, tuoi, gioi_tinh, dia_chi, so_dien_thoai)

    def nhap_bac_si(self):
        ma_bac_si = input("Nhập mã bác sĩ: ")
        ten_bac_si = input("Nhập tên bác sĩ: ")
        chuyen_khoa = input("Nhập chuyên khoa: ")
        while True:
            try:
                gia_kham = float(input("Nhập giá khám (VND): "))
                if gia_kham < 0:
                    print("Giá khám không được âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Giá khám không hợp lệ. Vui lòng nhập lại.")
        return BacSi(ma_bac_si, ten_bac_si, chuyen_khoa, gia_kham)

    def nhap_lich_hen(self):
        ma_lich_hen = input("Nhập mã lịch hẹn: ")
        ma_benh_nhan = input("Nhập mã bệnh nhân: ")
        ma_bac_si = input("Nhập mã bác sĩ: ")
        ngay_gio = input("Nhập ngày giờ hẹn (dd/mm/yyyy hh:mm): ")
        ly_do_kham = input("Nhập lý do khám: ")
        return LichHen(ma_lich_hen, ma_benh_nhan, ma_bac_si, ngay_gio, ly_do_kham)

    def nhap_thuoc(self):
        ma_thuoc = input("Nhập mã thuốc: ")
        ten_thuoc = input("Nhập tên thuốc: ")
        don_vi = input("Nhập đơn vị (viên, lọ, túi, v.v.): ")
        while True:
            try:
                gia_ban = float(input("Nhập giá bán (VND): "))
                if gia_ban < 0:
                    print("Giá bán không được âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Giá bán không hợp lệ. Vui lòng nhập lại.")
        
        while True:
            try:
                so_luong_ton = int(input("Nhập số lượng tồn kho: "))
                if so_luong_ton < 0:
                    print("Số lượng tồn không được âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Số lượng tồn không hợp lệ. Vui lòng nhập lại.")
        
        mo_ta = input("Nhập mô tả (có thể để trống): ")
        cong_dung = input("Nhập công dụng (có thể để trống): ")
        return Thuoc(ma_thuoc, ten_thuoc, don_vi, gia_ban, so_luong_ton, mo_ta, cong_dung)

    def nhap_don_thuoc(self):
        ma_don_thuoc = input("Nhập mã đơn thuốc: ")
        ma_lich_hen = input("Nhập mã lịch hẹn: ")
        ma_benh_nhan = input("Nhập mã bệnh nhân: ")
        ma_bac_si = input("Nhập mã bác sĩ: ")
        ngay_ke = input("Nhập ngày kê đơn (dd/mm/yyyy): ")
        
        don_thuoc = DonThuoc(ma_don_thuoc, ma_lich_hen, ma_benh_nhan, ma_bac_si, ngay_ke)
        
        print("Nhập danh sách thuốc trong đơn:")
        while True:
            ma_thuoc = input("Nhập mã thuốc (hoặc 'xong' để kết thúc): ")
            if ma_thuoc.lower() == 'xong':
                break
            
            while True:
                try:
                    so_luong = int(input("Nhập số lượng: "))
                    if so_luong <= 0:
                        print("Số lượng phải lớn hơn 0.")
                        continue
                    break
                except ValueError:
                    print("Số lượng không hợp lệ.")
            
            cach_dung = input("Nhập cách dùng (VD: Sáng 1 viên, tối 1 viên, sau ăn): ")
            ghi_chu = input("Nhập ghi chú (có thể để trống): ")
            
            chi_tiet = ChiTietDonThuoc(ma_thuoc, so_luong, cach_dung, ghi_chu)
            don_thuoc.them_thuoc(chi_tiet)
            print("Đã thêm thuốc vào đơn.")
        
        return don_thuoc
def menu():
    ql_benh_vien = QuanLyBenhVien()
    
    # Thêm dữ liệu mẫu
    ql_benh_vien.them_benh_nhan(BenhNhan("BN001", "Nguyễn Văn A", 30, "Nam", "Hà Nội", "0123456789"))
    ql_benh_vien.them_benh_nhan(BenhNhan("BN002", "Trần Thị B", 25, "Nữ", "TP.HCM", "0987654321"))
    ql_benh_vien.them_bac_si(BacSi("BS001", "BS. Nguyễn Văn C", "Tim mạch", 500000))
    ql_benh_vien.them_bac_si(BacSi("BS002", "BS. Lê Thị D", "Nhi khoa", 400000))
    
    # Thêm thuốc mẫu
    ql_benh_vien.them_thuoc(Thuoc("T001", "Paracetamol", "viên", 2000, 1000, "Thuốc giảm đau, hạ sốt", "Giảm đau đầu, sốt"))
    ql_benh_vien.them_thuoc(Thuoc("T002", "Amoxicillin", "viên", 5000, 500, "Kháng sinh", "Điều trị nhiễm khuẩn"))
    ql_benh_vien.them_thuoc(Thuoc("T003", "Vitamin C", "viên", 1500, 2000, "Vitamin tổng hợp", "Tăng cường sức đề kháng"))
    
    while True:
        print("\n" + "="*50)
        print("HỆ THỐNG QUẢN LÝ BỆNH VIỆN".center(50))
        print("="*50)
        print("=== QUẢN LÝ BỆNH NHÂN ===")
        print("1. Thêm bệnh nhân")
        print("2. Cập nhật bệnh nhân")
        print("3. Xóa bệnh nhân")
        print("4. Tìm kiếm bệnh nhân theo tên")
        print("5. In tất cả bệnh nhân")
        print("\n=== QUẢN LÝ BÁC SĨ ===")
        print("6. Thêm bác sĩ")
        print("7. Cập nhật bác sĩ")
        print("8. Xóa bác sĩ")
        print("9. Tìm bác sĩ theo chuyên khoa")
        print("10. In tất cả bác sĩ")
        print("\n=== QUẢN LÝ LỊCH HẸN ===")
        print("11. Đặt lịch hẹn")
        print("12. Cập nhật trạng thái lịch hẹn")
        print("13. Hủy lịch hẹn")
        print("14. Xem lịch hẹn theo bệnh nhân")
        print("15. In tất cả lịch hẹn")
        print("\n=== QUẢN LÝ THUỐC ===")
        print("16. Thêm thuốc")
        print("17. Cập nhật thuốc")
        print("18. Xóa thuốc")
        print("19. Tìm kiếm thuốc theo tên")
        print("20. In tất cả thuốc")
        print("\n=== QUẢN LÝ ĐÔN THUỐC ===")
        print("21. Kê đơn thuốc")
        print("22. Lấy thuốc")
        print("23. Hủy đơn thuốc")
        print("24. Xem đơn thuốc theo bệnh nhân")
        print("25. In tất cả đơn thuốc")
        print("\n=== THỐNG KÊ ===")
        print("26. Thống kê doanh thu")
        print("27. Thoát")
        
        choice = input("Chọn chức năng (1-27): ")

        if choice == '1':
            benh_nhan_moi = ql_benh_vien.nhap_benh_nhan()
            ql_benh_vien.them_benh_nhan(benh_nhan_moi)
        elif choice == '2':
            ma_benh_nhan = input("Nhập mã bệnh nhân cần cập nhật: ")
            ten_moi = input("Nhập tên mới (để trống nếu không đổi): ")
            tuoi_moi_input = input("Nhập tuổi mới (để trống nếu không đổi): ")
            gioi_tinh_moi = input("Nhập giới tính mới (để trống nếu không đổi): ")
            tuoi_moi = int(tuoi_moi_input) if tuoi_moi_input else None
            ql_benh_vien.cap_nhat_benh_nhan(ma_benh_nhan, ten_moi or None, tuoi_moi, gioi_tinh_moi or None)
        elif choice == '3':
            ma_benh_nhan = input("Nhập mã bệnh nhân cần xóa: ")
            ql_benh_vien.xoa_benh_nhan(ma_benh_nhan)
        elif choice == '4':
            ten_benh_nhan = input("Nhập tên bệnh nhân cần tìm: ")
            ql_benh_vien.tim_kiem_benh_nhan_theo_ten(ten_benh_nhan)
        elif choice == '5':
            ql_benh_vien.in_tat_ca_benh_nhan()
        elif choice == '6':
            bac_si_moi = ql_benh_vien.nhap_bac_si()
            ql_benh_vien.them_bac_si(bac_si_moi)
        elif choice == '7':
            ma_bac_si = input("Nhập mã bác sĩ cần cập nhật: ")
            ten_moi = input("Nhập tên mới (để trống nếu không đổi): ")
            chuyen_khoa_moi = input("Nhập chuyên khoa mới (để trống nếu không đổi): ")
            gia_kham_moi_input = input("Nhập giá khám mới (để trống nếu không đổi): ")
            gia_kham_moi = float(gia_kham_moi_input) if gia_kham_moi_input else None
            ql_benh_vien.cap_nhat_bac_si(ma_bac_si, ten_moi or None, chuyen_khoa_moi or None, gia_kham_moi)
        elif choice == '8':
            ma_bac_si = input("Nhập mã bác sĩ cần xóa: ")
            ql_benh_vien.xoa_bac_si(ma_bac_si)
        elif choice == '9':
            chuyen_khoa = input("Nhập chuyên khoa cần tìm: ")
            ql_benh_vien.tim_kiem_bac_si_theo_chuyen_khoa(chuyen_khoa)
        elif choice == '10':
            ql_benh_vien.in_tat_ca_bac_si()
        elif choice == '11':
            lich_hen_moi = ql_benh_vien.nhap_lich_hen()
            ql_benh_vien.dat_lich_hen(lich_hen_moi)
        elif choice == '12':
            ma_lich_hen = input("Nhập mã lịch hẹn: ")
            trang_thai = input("Nhập trạng thái mới (Đã đặt/Đã khám/Hủy): ")
            ql_benh_vien.cap_nhat_trang_thai_lich_hen(ma_lich_hen, trang_thai)
        elif choice == '13':
            ma_lich_hen = input("Nhập mã lịch hẹn cần hủy: ")
            ql_benh_vien.huy_lich_hen(ma_lich_hen)
        elif choice == '14':
            ma_benh_nhan = input("Nhập mã bệnh nhân: ")
            ql_benh_vien.in_lich_hen_theo_benh_nhan(ma_benh_nhan)
        elif choice == '15':
            ql_benh_vien.in_tat_ca_lich_hen()
        elif choice == '16':
            thuoc_moi = ql_benh_vien.nhap_thuoc()
            ql_benh_vien.them_thuoc(thuoc_moi)
        elif choice == '17':
            ma_thuoc = input("Nhập mã thuốc cần cập nhật: ")
            ten_moi = input("Nhập tên thuốc mới (để trống nếu không đổi): ")
            gia_ban_moi_input = input("Nhập giá bán mới (để trống nếu không đổi): ")
            so_luong_moi_input = input("Nhập số lượng tồn mới (để trống nếu không đổi): ")
            mo_ta_moi = input("Nhập mô tả mới (để trống nếu không đổi): ")
            gia_ban_moi = float(gia_ban_moi_input) if gia_ban_moi_input else None
            so_luong_moi = int(so_luong_moi_input) if so_luong_moi_input else None
            ql_benh_vien.cap_nhat_thuoc(ma_thuoc, ten_moi or None, gia_ban_moi, so_luong_moi, mo_ta_moi or None)
        elif choice == '18':
            ma_thuoc = input("Nhập mã thuốc cần xóa: ")
            ql_benh_vien.xoa_thuoc(ma_thuoc)
        elif choice == '19':
            ten_thuoc = input("Nhập tên thuốc cần tìm: ")
            ql_benh_vien.tim_kiem_thuoc_theo_ten(ten_thuoc)
        elif choice == '20':
            ql_benh_vien.in_tat_ca_thuoc()
        elif choice == '21':
            don_thuoc_moi = ql_benh_vien.nhap_don_thuoc()
            ql_benh_vien.ke_don_thuoc(don_thuoc_moi)
        elif choice == '22':
            ma_don_thuoc = input("Nhập mã đơn thuốc cần lấy: ")
            ql_benh_vien.lay_thuoc(ma_don_thuoc)
        elif choice == '23':
            ma_don_thuoc = input("Nhập mã đơn thuốc cần hủy: ")
            ql_benh_vien.huy_don_thuoc(ma_don_thuoc)
        elif choice == '24':
            ma_benh_nhan = input("Nhập mã bệnh nhân: ")
            ql_benh_vien.in_don_thuoc_theo_benh_nhan(ma_benh_nhan)
        elif choice == '25':
            ql_benh_vien.in_tat_ca_don_thuoc()
        elif choice == '26':
            ql_benh_vien.thong_ke_doanh_thu()
        elif choice == '27':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    menu()

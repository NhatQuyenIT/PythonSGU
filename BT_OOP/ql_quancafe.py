# Quản lý quán cafe / nhà hàng / cửa hàng thức ăn nhanh / quán ăn vặt / quán trà chanh
# / quán ăn nhỏ / quán trà sữa 
# / quán bar / karaoke / pub / club 
# / lẩu nướng / tiệc cưới / tiệc sinh nhật / tiệc liên hoan / tiệc tất niên / tiệc họp mặt / tiệc kỷ niệm 
# / tiệc ngoài trời / tiệc trong nhà / tiệc buffet / tiệc set menu / tiệc finger food / tiệc cocktail / tiệc trà...
# Lưu trữ thông tin khách hàng, đơn hàng, món ăn, bàn

# Hệ thống quản lý quán cafe
class KhachHang:
    def __init__(self, ma_khach_hang, ten_khach_hang, so_dien_thoai):
        self.ma_khach_hang = ma_khach_hang
        self.ten_khach_hang = ten_khach_hang
        self.so_dien_thoai = so_dien_thoai

class MonAn:
    def __init__(self, ma_mon_an, ten_mon_an, gia):
        self.ma_mon_an = ma_mon_an
        self.ten_mon_an = ten_mon_an
        self.gia = gia

class DonHang:
    def __init__(self, ma_don_hang, khach_hang, danh_sach_mon_an):
        self.ma_don_hang = ma_don_hang
        self.khach_hang = khach_hang
        self.danh_sach_mon_an = danh_sach_mon_an

class QuanLyCafe:
    def __init__(self):
        self.danh_sach_khach_hang = []
        self.danh_sach_mon_an = []
        self.danh_sach_don_hang = []

    def them_khach_hang(self, khach_hang):
        self.danh_sach_khach_hang.append(khach_hang)

    def them_mon_an(self, mon_an):
        self.danh_sach_mon_an.append(mon_an)

    def tao_don_hang(self, don_hang):
        self.danh_sach_don_hang.append(don_hang)
        print(f"Đã tạo đơn hàng cho khách hàng: {don_hang.khach_hang.ten_khach_hang}")
    def in_don_hang(self, ma_don_hang):
        for don_hang in self.danh_sach_don_hang:
            if don_hang.ma_don_hang == ma_don_hang:
                print(f"Đơn hàng mã: {don_hang.ma_don_hang}")
                print(f"Khách hàng: {don_hang.khach_hang.ten_khach_hang}")
                print("Danh sách món ăn:")
                for mon_an in don_hang.danh_sach_mon_an:
                    print(f"- {mon_an.ten_mon_an}: {mon_an.gia:,.0f} VND")
                tong_tien = sum(mon_an.gia for mon_an in don_hang.danh_sach_mon_an)
                print(f"Tổng tiền: {tong_tien:,.0f} VND")
                return
        print(f"Không tìm thấy đơn hàng có mã {ma_don_hang}.")
    def thong_ke_doanh_thu(self):
        tong_doanh_thu = 0
        for don_hang in self.danh_sach_don_hang:
            tong_doanh_thu += sum(mon_an.gia for mon_an in don_hang.danh_sach_mon_an)
        print(f"Tổng doanh thu: {tong_doanh_thu:,.0f} VND")
        return tong_doanh_thu
    
    def tim_kiem_khach_hang(self, ten_khach_hang):
        ket_qua = [kh for kh in self.danh_sach_khach_hang if ten_khach_hang.lower() in kh.ten_khach_hang.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} khách hàng có chứa từ khóa '{ten_khach_hang}':")
            for kh in ket_qua:
                print(f"- Mã KH: {kh.ma_khach_hang}, Tên: {kh.ten_khach_hang}, SĐT: {kh.so_dien_thoai}")
        else:
            print(f"Không tìm thấy khách hàng nào có chứa từ khóa '{ten_khach_hang}'.")
    def in_tat_ca_khach_hang(self):
        if not self.danh_sach_khach_hang:
            print("Chưa có khách hàng nào.")
            return
        print("Danh sách tất cả khách hàng:")
        for kh in self.danh_sach_khach_hang:
            print(f"- Mã KH: {kh.ma_khach_hang}, Tên: {kh.ten_khach_hang}, SĐT: {kh.so_dien_thoai}")
    def in_tat_ca_mon_an(self):
        if not self.danh_sach_mon_an:
            print("Chưa có món ăn nào.")
            return
        print("Danh sách tất cả món ăn:")
        for ma in self.danh_sach_mon_an:
            print(f"- Mã món: {ma.ma_mon_an}, Tên: {ma.ten_mon_an}, Giá: {ma.gia:,.0f} VND")
    def in_tat_ca_don_hang(self):
        if not self.danh_sach_don_hang:
            print("Chưa có đơn hàng nào.")
            return
        print("Danh sách tất cả đơn hàng:")
        for dh in self.danh_sach_don_hang:
            print(f"- Mã đơn hàng: {dh.ma_don_hang}, Khách hàng: {dh.khach_hang.ten_khach_hang}, Số món: {len(dh.danh_sach_mon_an)}")
    def xoa_khach_hang(self, ma_khach_hang):
        for kh in self.danh_sach_khach_hang:
            if kh.ma_khach_hang == ma_khach_hang:
                self.danh_sach_khach_hang.remove(kh)
                print(f"Đã xóa khách hàng có mã {ma_khach_hang}.")
                return
        print(f"Không tìm thấy khách hàng có mã {ma_khach_hang}.")
    def xoa_mon_an(self, ma_mon_an):
        for ma in self.danh_sach_mon_an:
            if ma.ma_mon_an == ma_mon_an:
                self.danh_sach_mon_an.remove(ma)
                print(f"Đã xóa món ăn có mã {ma_mon_an}.")
                return
        print(f"Không tìm thấy món ăn có mã {ma_mon_an}.")
    def xoa_don_hang(self, ma_don_hang):
        for dh in self.danh_sach_don_hang:
            if dh.ma_don_hang == ma_don_hang:
                self.danh_sach_don_hang.remove(dh)
                print(f"Đã xóa đơn hàng có mã {ma_don_hang}.")
                return
        print(f"Không tìm thấy đơn hàng có mã {ma_don_hang}.")
    def cap_nhat_khach_hang(self, ma_khach_hang, ten_khach_hang_moi=None, so_dien_thoai_moi=None):
        for kh in self.danh_sach_khach_hang:
            if kh.ma_khach_hang == ma_khach_hang:
                if ten_khach_hang_moi is not None:
                    kh.ten_khach_hang = ten_khach_hang_moi
                if so_dien_thoai_moi is not None:
                    kh.so_dien_thoai = so_dien_thoai_moi
                print(f"Đã cập nhật thông tin khách hàng '{ma_khach_hang}'.")
                return
        print(f"Không tìm thấy khách hàng có mã {ma_khach_hang}.")
    def cap_nhat_mon_an(self, ma_mon_an, ten_mon_an_moi=None, gia_moi=None):
        for ma in self.danh_sach_mon_an:
            if ma.ma_mon_an == ma_mon_an:
                if ten_mon_an_moi is not None:
                    ma.ten_mon_an = ten_mon_an_moi
                if gia_moi is not None:
                    ma.gia = gia_moi
                print(f"Đã cập nhật thông tin món ăn '{ma_mon_an}'.")
                return
        print(f"Không tìm thấy món ăn có mã {ma_mon_an}.")
    def cap_nhat_don_hang(self, ma_don_hang, danh_sach_mon_an_moi=None):
        for dh in self.danh_sach_don_hang:
            if dh.ma_don_hang == ma_don_hang:
                if danh_sach_mon_an_moi is not None:
                    dh.danh_sach_mon_an = danh_sach_mon_an_moi
                print(f"Đã cập nhật thông tin đơn hàng '{ma_don_hang}'.")
                return
        print(f"Không tìm thấy đơn hàng có mã {ma_don_hang}.")
    def thong_ke_so_luong_khach_hang(self):
        so_luong = len(self.danh_sach_khach_hang)
        print(f"Tổng số lượng khách hàng: {so_luong}")
        return so_luong
    def thong_ke_so_luong_mon_an(self):
        so_luong = len(self.danh_sach_mon_an)
        print(f"Tổng số lượng món ăn: {so_luong}")
        return so_luong
    def thong_ke_so_luong_don_hang(self):
        so_luong = len(self.danh_sach_don_hang)
        print(f"Tổng số lượng đơn hàng: {so_luong}")
        return so_luong
    def thong_ke_don_hang_theo_khach_hang(self, ten_khach_hang):
        ket_qua = [dh for dh in self.danh_sach_don_hang if ten_khach_hang.lower() in dh.khach_hang.ten_khach_hang.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} đơn hàng của khách hàng có chứa từ khóa '{ten_khach_hang}':")
            for dh in ket_qua:
                print(f"- Mã đơn hàng: {dh.ma_don_hang}, Số món: {len(dh.danh_sach_mon_an)}")
        else:
            print(f"Không tìm thấy đơn hàng nào của khách hàng có chứa từ khóa '{ten_khach_hang}'.")
    def thong_ke_don_hang_theo_mon_an(self, ten_mon_an):
        ket_qua = []
        for dh in self.danh_sach_don_hang:
            for ma in dh.danh_sach_mon_an:
                if ten_mon_an.lower() in ma.ten_mon_an.lower():
                    ket_qua.append(dh)
                    break
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} đơn hàng có chứa món ăn với từ khóa '{ten_mon_an}':")
            for dh in ket_qua:
                print(f"- Mã đơn hàng: {dh.ma_don_hang}, Khách hàng: {dh.khach_hang.ten_khach_hang}")
        else:
            print(f"Không tìm thấy đơn hàng nào có chứa món ăn với từ khóa '{ten_mon_an}'.")
    def thong_ke_doanh_thu_theo_khach_hang(self, ten_khach_hang):
        tong_doanh_thu = 0
        for dh in self.danh_sach_don_hang:
            if ten_khach_hang.lower() in dh.khach_hang.ten_khach_hang.lower():
                tong_doanh_thu += sum(ma.gia for ma in dh.danh_sach_mon_an)
        print(f"Tổng doanh thu từ khách hàng có chứa từ khóa '{ten_khach_hang}': {tong_doanh_thu:,.0f} VND")
        return tong_doanh_thu
    def thong_ke_doanh_thu_theo_mon_an(self, ten_mon_an):
        tong_doanh_thu = 0
        for dh in self.danh_sach_don_hang:
            for ma in dh.danh_sach_mon_an:
                if ten_mon_an.lower() in ma.ten_mon_an.lower():
                    tong_doanh_thu += ma.gia
        print(f"Tổng doanh thu từ món ăn có chứa từ khóa '{ten_mon_an}': {tong_doanh_thu:,.0f} VND")
        return tong_doanh_thu
    def thong_ke_doanh_thu_theo_ngay(self, ngay):
        # Giả sử mỗi đơn hàng có thuộc tính 'ngay' (kiểu str) để lưu ngày tạo đơn hàng
        tong_doanh_thu = 0
        for dh in self.danh_sach_don_hang:
            if hasattr(dh, 'ngay') and dh.ngay == ngay:
                tong_doanh_thu += sum(ma.gia for ma in dh.danh_sach_mon_an)
        print(f"Tổng doanh thu trong ngày '{ngay}': {tong_doanh_thu:,.0f} VND")
        return tong_doanh_thu
    def thong_ke_doanh_thu_theo_thang(self, thang):
        # Giả sử mỗi đơn hàng có thuộc tính 'ngay' (kiểu str) để lưu ngày tạo đơn hàng theo định dạng 'YYYY-MM-DD'
        tong_doanh_thu = 0
        for dh in self.danh_sach_don_hang:
            if hasattr(dh, 'ngay') and dh.ngay.startswith(thang):
                tong_doanh_thu += sum(ma.gia for ma in dh.danh_sach_mon_an)
        print(f"Tổng doanh thu trong tháng '{thang}': {tong_doanh_thu:,.0f} VND")
        return tong_doanh_thu
    def thong_ke_doanh_thu_theo_nam(self, nam):
        # Giả sử mỗi đơn hàng có thuộc tính 'ngay' (kiểu str) để lưu ngày tạo đơn hàng theo định dạng 'YYYY-MM-DD'
        tong_doanh_thu = 0
        for dh in self.danh_sach_don_hang:
            if hasattr(dh, 'ngay') and dh.ngay.startswith(nam):
                tong_doanh_thu += sum(ma.gia for ma in dh.danh_sach_mon_an)
        print(f"Tổng doanh thu trong năm '{nam}': {tong_doanh_thu:,.0f} VND")
        return tong_doanh_thu
    def thong_ke_mon_an_ban_chay(self):
        thong_ke = {}
        for dh in self.danh_sach_don_hang:
            for ma in dh.danh_sach_mon_an:
                if ma.ten_mon_an in thong_ke:
                    thong_ke[ma.ten_mon_an] += 1
                else:
                    thong_ke[ma.ten_mon_an] = 1
        danh_sach_ban_chay = sorted(thong_ke.items(), key=lambda x: x[1], reverse=True)
        print("Thống kê món ăn bán chạy:")
        for ten_mon_an, so_luong in danh_sach_ban_chay:
            print(f"- {ten_mon_an}: {so_luong} lần")
        return danh_sach_ban_chay
    def thong_ke_khach_hang_than_thiet(self):
        thong_ke = {}
        for dh in self.danh_sach_don_hang:
            ten_khach_hang = dh.khach_hang.ten_khach_hang
            if ten_khach_hang in thong_ke:
                thong_ke[ten_khach_hang] += 1
            else:
                thong_ke[ten_khach_hang] = 1
        danh_sach_than_thiet = sorted(thong_ke.items(), key=lambda x: x[1], reverse=True)
        print("Thống kê khách hàng thân thiết:")
        for ten_khach_hang, so_luong in danh_sach_than_thiet:
            print(f"- {ten_khach_hang}: {so_luong} đơn hàng")
        return danh_sach_than_thiet

    def nhap_khach_hang(self):
        ma_khach_hang = input("Nhập mã khách hàng: ")
        ten_khach_hang = input("Nhập tên khách hàng: ")
        so_dien_thoai = input("Nhập số điện thoại: ")
        return KhachHang(ma_khach_hang, ten_khach_hang, so_dien_thoai)
    def nhap_mon_an(self):
        ma_mon_an = input("Nhập mã món ăn: ")
        ten_mon_an = input("Nhập tên món ăn: ")
        while True:
            try:
                gia = float(input("Nhập giá món ăn (VND): "))
                if gia < 0:
                    print("Giá món ăn không được âm. Vui lòng nhập lại.")
                    continue
                break
            except ValueError:
                print("Giá món ăn không hợp lệ. Vui lòng nhập lại.")
        return MonAn(ma_mon_an, ten_mon_an, gia)
    def nhap_don_hang(self):
        ma_don_hang = input("Nhập mã đơn hàng: ")
        print("Nhập thông tin khách hàng cho đơn hàng:")
        khach_hang = self.nhap_khach_hang()
        danh_sach_mon_an = []
        while True:
            print("Nhập món ăn cho đơn hàng (hoặc nhập 'x' để kết thúc):")
            mon_an = self.nhap_mon_an()
            danh_sach_mon_an.append(mon_an)
            tiep_tuc = input("Bạn có muốn thêm món ăn khác không? (y/n): ")
            if tiep_tuc.lower() != 'y':
                break
        return DonHang(ma_don_hang, khach_hang, danh_sach_mon_an)

def menu():
    quan_ly = QuanLyCafe()
    while True:
        print("\n===== Quản Lý Quán Cafe =====")
        print("1. Thêm khách hàng")
        print("2. Thêm món ăn")
        print("3. Tạo đơn hàng")
        print("4. In đơn hàng")
        print("5. In tất cả khách hàng")
        print("6. In tất cả món ăn")
        print("7. In tất cả đơn hàng")
        print("8. Tìm kiếm khách hàng")
        print("9. Thống kê doanh thu")
        print("10. Thống kê số lượng khách hàng")
        print("11. Thống kê số lượng món ăn")
        print("12. Thống kê số lượng đơn hàng")
        print("13. Xóa khách hàng")
        print("14. Xóa món ăn")
        print("15. Xóa đơn hàng")
        print("16. Cập nhật khách hàng")
        print("17. Cập nhật món ăn")
        print("18. Cập nhật đơn hàng")
        print("19. Thống kê đơn hàng theo khách hàng")
        print("20. Thống kê đơn hàng theo món ăn")
        print("21. Thống kê doanh thu theo khách hàng")
        print("22. Thống kê doanh thu theo món ăn")
        print("23. Thống kê doanh thu theo ngày")
        print("24. Thống kê doanh thu theo tháng")
        print("25. Thống kê doanh thu theo năm")
        print("26. Thống kê món ăn bán chạy")
        print("27. Thống kê khách hàng thân thiết")
        print("0. Thoát chương trình")
        choice = input("Chọn chức năng (0-27): ")
        
        if choice == '1':
            khach_hang = quan_ly.nhap_khach_hang()
            quan_ly.them_khach_hang(khach_hang)
        elif choice == '2':
            mon_an = quan_ly.nhap_mon_an()
            quan_ly.them_mon_an(mon_an)
        elif choice == '3':
            don_hang = quan_ly.nhap_don_hang()
            quan_ly.tao_don_hang(don_hang)
        elif choice == '4':
            ma_don_hang = input("Nhập mã đơn hàng cần in: ")
            quan_ly.in_don_hang(ma_don_hang)
        elif choice == '5':
            quan_ly.in_tat_ca_khach_hang()
        elif choice == '6':
            quan_ly.in_tat_ca_mon_an()
        elif choice == '7':
            quan_ly.in_tat_ca_don_hang()
        elif choice == '8':
            ten_khach_hang = input("Nhập tên khách hàng cần tìm kiếm: ")
            quan_ly.tim_kiem_khach_hang(ten_khach_hang)
        elif choice == '9':
            quan_ly.thong_ke_doanh_thu()
        elif choice == '10':
            quan_ly.thong_ke_so_luong_khach_hang()
        elif choice == '11':
            quan_ly.thong_ke_so_luong_mon_an()
        elif choice == '12':
            quan_ly.thong_ke_so_luong_don_hang()
        elif choice == '13':
            ma_khach_hang = input("Nhập mã khách hàng cần xóa: ")
            quan_ly.xoa_khach_hang(ma_khach_hang)
        elif choice == '14':
            ma_mon_an = input("Nhập mã món ăn cần xóa: ")
            quan_ly.xoa_mon_an(ma_mon_an)
        elif choice == '15':
            ma_don_hang = input("Nhập mã đơn hàng cần xóa: ")
            quan_ly.xoa_don_hang(ma_don_hang)
        elif choice == '16':
            ma_khach_hang = input("Nhập mã khách hàng cần cập nhật: ")
            ten_khach_hang_moi = input("Nhập tên khách hàng mới (hoặc để trống nếu không đổi): ")
            so_dien_thoai_moi = input("Nhập số điện thoại mới (hoặc để trống nếu không đổi): ")
            quan_ly.cap_nhat_khach_hang(ma_khach_hang, ten_khach_hang_moi or None, so_dien_thoai_moi or None)
        elif choice == '17':
            ma_mon_an = input("Nhập mã món ăn cần cập nhật: ")
            ten_mon_an_moi = input("Nhập tên món ăn mới (hoặc để trống nếu không đổi): ")
            gia_moi_input = input("Nhập giá món ăn mới (hoặc để trống nếu không đổi): ")
            gia_moi = float(gia_moi_input) if gia_moi_input else None
            quan_ly.cap_nhat_mon_an(ma_mon_an, ten_mon_an_moi or None, gia_moi)
        elif choice == '18':
            ma_don_hang = input("Nhập mã đơn hàng cần cập nhật: ")
            print("Nhập lại danh sách món ăn cho đơn hàng (hoặc để trống nếu không đổi):")
            danh_sach_mon_an_moi = []
            while True:
                mon_an = quan_ly.nhap_mon_an()
                danh_sach_mon_an_moi.append(mon_an)
                tiep_tuc = input("Bạn có muốn thêm món ăn khác không? (y/n): ")
                if tiep_tuc.lower() != 'y':
                    break
            quan_ly.cap_nhat_don_hang(ma_don_hang, danh_sach_mon_an_moi or None)
        elif choice == '19':
            ten_khach_hang = input("Nhập tên khách hàng để thống kê đơn hàng: ")
            quan_ly.thong_ke_don_hang_theo_khach_hang(ten_khach_hang)
        elif choice == '20':
            ten_mon_an = input("Nhập tên món ăn để thống kê đơn hàng: ")
            quan_ly.thong_ke_don_hang_theo_mon_an(ten_mon_an)
        elif choice == '21':
            ten_khach_hang = input("Nhập tên khách hàng để thống kê doanh thu: ")
            quan_ly.thong_ke_doanh_thu_theo_khach_hang(ten_khach_hang)
        elif choice == '22':
            ten_mon_an = input("Nhập tên món ăn để thống kê doanh thu: ")
            quan_ly.thong_ke_doanh_thu_theo_mon_an(ten_mon_an)
        elif choice == '23':
            ngay = input("Nhập ngày (YYYY-MM-DD) để thống kê doanh thu: ")
            quan_ly.thong_ke_doanh_thu_theo_ngay(ngay)
        elif choice == '24':
            thang = input("Nhập tháng (YYYY-MM) để thống kê doanh thu: ")
            quan_ly.thong_ke_doanh_thu_theo_thang(thang)
        elif choice == '25':
            nam = input("Nhập năm (YYYY) để thống kê doanh thu: ")
            quan_ly.thong_ke_doanh_thu_theo_nam(nam)
        elif choice == '26':
            quan_ly.thong_ke_mon_an_ban_chay()
        elif choice == '27':
            quan_ly.thong_ke_khach_hang_than_thiet()
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            
if __name__ == "__main__":
    menu()

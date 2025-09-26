# Quản lý trang trại chăn nuôi
# Lưu trữ thông tin vật nuôi, chuồng trại, thức ăn
# Thêm, sửa, xóa thông tin vật nuôi, chuồng trại, thức ăn
# Tìm kiếm vật nuôi theo loại, chuồng trại theo vị trí
# Thống kê số lượng vật nuôi theo loại, chuồng trại theo tình trạng
# Thống kê lượng thức ăn đã sử dụng

class VatNuoi:
    def __init__(self, id_vat_nuoi, loai, tuoi, suc_khoe, id_chuong):
        self.id_vat_nuoi = id_vat_nuoi
        self.loai = loai
        self.tuoi = tuoi
        self.suc_khoe = suc_khoe
        self.id_chuong = id_chuong

    def hien_thi_thong_tin(self):
        print(f"ID: {self.id_vat_nuoi}, Loại: {self.loai}, Tuổi: {self.tuoi}, Sức khỏe: {self.suc_khoe}, Chuồng: {self.id_chuong}")
        print("-" * 50)
        
class Chuong:
    def __init__(self, id_chuong, vi_tri, tinh_trang):
        self.id_chuong = id_chuong
        self.vi_tri = vi_tri
        self.tinh_trang = tinh_trang

    def hien_thi_thong_tin(self):
        print(f"ID: {self.id_chuong}, Vị trí: {self.vi_tri}, Tình trạng: {self.tinh_trang}")
        print("-" * 50)
        
class ThucAn:
    def __init__(self, id_thuc_an, ten_thuc_an, so_luong):
        self.id_thuc_an = id_thuc_an
        self.ten_thuc_an = ten_thuc_an
        self.so_luong = so_luong

    def hien_thi_thong_tin(self):
        print(f"ID: {self.id_thuc_an}, Tên: {self.ten_thuc_an}, Số lượng: {self.so_luong}")
        print("-" * 50)
        
class QuanLyTrangTrai:
    def __init__(self):
        self.danh_sach_vat_nuoi = []
        self.danh_sach_chuong = []
        self.danh_sach_thuc_an = []
        self.luong_thuc_an_da_su_dung = 0
    def them_vat_nuoi(self, vat_nuoi):
        self.danh_sach_vat_nuoi.append(vat_nuoi)
        print(f"Đã thêm vật nuôi ID: {vat_nuoi.id_vat_nuoi}")
    def cap_nhat_vat_nuoi(self, id_vat_nuoi, loai_moi=None, tuoi_moi=None, suc_khoe_moi=None, id_chuong_moi=None):
        for vat_nuoi in self.danh_sach_vat_nuoi:
            if vat_nuoi.id_vat_nuoi == id_vat_nuoi:
                if loai_moi is not None:
                    vat_nuoi.loai = loai_moi
                if tuoi_moi is not None:
                    vat_nuoi.tuoi = tuoi_moi
                if suc_khoe_moi is not None:
                    vat_nuoi.suc_khoe = suc_khoe_moi
                if id_chuong_moi is not None:
                    vat_nuoi.id_chuong = id_chuong_moi
                print(f"Đã cập nhật thông tin vật nuôi ID '{id_vat_nuoi}'.")
                return
        print(f"Không tìm thấy vật nuôi có ID {id_vat_nuoi}.")
    def xoa_vat_nuoi(self, id_vat_nuoi):
        for vat_nuoi in self.danh_sach_vat_nuoi:
            if vat_nuoi.id_vat_nuoi == id_vat_nuoi:
                self.danh_sach_vat_nuoi.remove(vat_nuoi)
                print(f"Đã xóa vật nuôi có ID {id_vat_nuoi}.")
                return
        print(f"Không tìm thấy vật nuôi có ID {id_vat_nuoi}.")
    def tim_kiem_vat_nuoi_theo_loai(self, loai):
        ket_qua = [vn for vn in self.danh_sach_vat_nuoi if loai.lower() in vn.loai.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} vật nuôi có chứa từ khóa '{loai}':")
            for vn in ket_qua:
                vn.hien_thi_thong_tin()
        else:
            print(f"Không tìm thấy vật nuôi nào có chứa từ khóa '{loai}'.")
    def in_tat_ca_vat_nuoi(self):
        if not self.danh_sach_vat_nuoi:
            print("Chưa có vật nuôi nào được thêm.")
            return
        print("Danh sách tất cả vật nuôi:")
        for vn in self.danh_sach_vat_nuoi:
            vn.hien_thi_thong_tin()
    def them_chuong(self, chuong):
        self.danh_sach_chuong.append(chuong)
        print(f"Đã thêm chuồng ID: {chuong.id_chuong}")
    def cap_nhat_chuong(self, id_chuong, vi_tri_moi=None, tinh_trang_moi=None):
        for chuong in self.danh_sach_chuong:
            if chuong.id_chuong == id_chuong:
                if vi_tri_moi is not None:
                    chuong.vi_tri = vi_tri_moi
                if tinh_trang_moi is not None:
                    chuong.tinh_trang = tinh_trang_moi
                print(f"Đã cập nhật thông tin chuồng ID '{id_chuong}'.")
                return
        print(f"Không tìm thấy chuồng có ID {id_chuong}.")
    def xoa_chuong(self, id_chuong):
        for chuong in self.danh_sach_chuong:
            if chuong.id_chuong == id_chuong:
                self.danh_sach_chuong.remove(chuong)
                print(f"Đã xóa chuồng có ID {id_chuong}.")
                return
        print(f"Không tìm thấy chuồng có ID {id_chuong}.")
    def tim_kiem_chuong_theo_vi_tri(self, vi_tri):
        ket_qua = [ch for ch in self.danh_sach_chuong if vi_tri.lower() in ch.vi_tri.lower()]
        if ket_qua:
            print(f"Tìm thấy {len(ket_qua)} chuồng có chứa từ khóa '{vi_tri}':")
            for ch in ket_qua:
                ch.hien_thi_thong_tin()
        else:
            print(f"Không tìm thấy chuồng nào có chứa từ khóa '{vi_tri}'.")
    def in_tat_ca_chuong(self):
        if not self.danh_sach_chuong:
            print("Chưa có chuồng nào được thêm.")
            return
        print("Danh sách tất cả chuồng:")
        for ch in self.danh_sach_chuong:
            ch.hien_thi_thong_tin()
    def them_thuc_an(self, thuc_an):
        self.danh_sach_thuc_an.append(thuc_an)
        print(f"Đã thêm thức ăn ID: {thuc_an.id_thuc_an}")
    def cap_nhat_thuc_an(self, id_thuc_an, ten_thuc_an_moi=None, so_luong_moi=None):
        for thuc_an in self.danh_sach_thuc_an:
            if thuc_an.id_thuc_an == id_thuc_an:
                if ten_thuc_an_moi is not None:
                    thuc_an.ten_thuc_an = ten_thuc_an_moi
                if so_luong_moi is not None:
                    thuc_an.so_luong = so_luong_moi
                print(f"Đã cập nhật thông tin thức ăn ID '{id_thuc_an}'.")
                return
        print(f"Không tìm thấy thức ăn có ID {id_thuc_an}.")
    def xoa_thuc_an(self, id_thuc_an):
        for thuc_an in self.danh_sach_thuc_an:
            if thuc_an.id_thuc_an == id_thuc_an:
                self.danh_sach_thuc_an.remove(thuc_an)
                print(f"Đã xóa thức ăn có ID {id_thuc_an}.")
                return
        print(f"Không tìm thấy thức ăn có ID {id_thuc_an}.")
    def in_tat_ca_thuc_an(self):
        if not self.danh_sach_thuc_an:
            print("Chưa có thức ăn nào được thêm.")
            return
        print("Danh sách tất cả thức ăn:")
        for ta in self.danh_sach_thuc_an:
            ta.hien_thi_thong_tin()
    def su_dung_thuc_an(self, id_thuc_an, so_luong_su_dung):
        for thuc_an in self.danh_sach_thuc_an:
            if thuc_an.id_thuc_an == id_thuc_an:
                if thuc_an.so_luong >= so_luong_su_dung:
                    thuc_an.so_luong -= so_luong_su_dung
                    self.luong_thuc_an_da_su_dung += so_luong_su_dung
                    print(f"Đã sử dụng {so_luong_su_dung} của thức ăn ID {id_thuc_an}.")
                    return True
                else:
                    print(f"Không đủ lượng thức ăn ID {id_thuc_an} để sử dụng.")
                    return False
        print(f"Không tìm thấy thức ăn có ID {id_thuc_an}.")
        return False
    def thong_ke_so_luong_vat_nuoi_theo_loai(self):
        thong_ke = {}
        for vn in self.danh_sach_vat_nuoi:
            if vn.loai in thong_ke:
                thong_ke[vn.loai] += 1
            else:
                thong_ke[vn.loai] = 1
        print("Thống kê số lượng vật nuôi theo loại:")
        for loai, so_luong in thong_ke.items():
            print(f"{loai}: {so_luong}")
        return thong_ke
    def thong_ke_so_luong_chuong_theo_tinh_trang(self):
        thong_ke = {}
        for ch in self.danh_sach_chuong:
            if ch.tinh_trang in thong_ke:
                thong_ke[ch.tinh_trang] += 1
            else:
                thong_ke[ch.tinh_trang] = 1
        print("Thống kê số lượng chuồng theo tình trạng:")
        for tinh_trang, so_luong in thong_ke.items():
            print(f"{tinh_trang}: {so_luong}")
        return thong_ke
    def thong_ke_luong_thuc_an_da_su_dung(self):
        print(f"Tổng lượng thức ăn đã sử dụng: {self.luong_thuc_an_da_su_dung}")
        return self.luong_thuc_an_da_su_dung
    

def menu():
    ql_trang_trai = QuanLyTrangTrai()
    while True:
        print("\n--- Quản Lý Trang Trại Chăn Nuôi ---")
        print("1. Thêm vật nuôi")
        print("2. Cập nhật vật nuôi")
        print("3. Xóa vật nuôi")
        print("4. Tìm kiếm vật nuôi theo loại")
        print("5. In tất cả vật nuôi")
        print("6. Thêm chuồng")
        print("7. Cập nhật chuồng")
        print("8. Xóa chuồng")
        print("9. Tìm kiếm chuồng theo vị trí")
        print("10. In tất cả chuồng")
        print("11. Thêm thức ăn")
        print("12. Cập nhật thức ăn")
        print("13. Xóa thức ăn")
        print("14. In tất cả thức ăn")
        print("15. Sử dụng thức ăn")
        print("16. Thống kê số lượng vật nuôi theo loại")
        print("17. Thống kê số lượng chuồng theo tình trạng")
        print("18. Thống kê lượng thức ăn đã sử dụng")
        print("0. Thoát")
        choice = input("Chọn chức năng (0-18): ")
        
        if choice == '1':
            id_vat_nuoi = input("Nhập ID vật nuôi: ")
            loai = input("Nhập loại vật nuôi: ")
            tuoi = int(input("Nhập tuổi vật nuôi: "))
            suc_khoe = input("Nhập tình trạng sức khỏe: ")
            id_chuong = input("Nhập ID chuồng: ")
            vat_nuoi_moi = VatNuoi(id_vat_nuoi, loai, tuoi, suc_khoe, id_chuong)
            ql_trang_trai.them_vat_nuoi(vat_nuoi_moi)
        elif choice == '2':
            id_vat_nuoi = input("Nhập ID vật nuôi cần cập nhật: ")
            loai_moi = input("Nhập loại mới (hoặc để trống nếu không đổi): ") or None
            tuoi_moi_input = input("Nhập tuổi mới (hoặc để trống nếu không đổi): ")
            tuoi_moi = int(tuoi_moi_input) if tuoi_moi_input else None
            suc_khoe_moi = input("Nhập tình trạng sức khỏe mới (hoặc để trống nếu không đổi): ") or None
            id_chuong_moi = input("Nhập ID chuồng mới (hoặc để trống nếu không đổi): ") or None
            ql_trang_trai.cap_nhat_vat_nuoi(id_vat_nuoi, loai_moi, tuoi_moi, suc_khoe_moi, id_chuong_moi)
        elif choice == '3':
            id_vat_nuoi = input("Nhập ID vật nuôi cần xóa: ")
            ql_trang_trai.xoa_vat_nuoi(id_vat_nuoi)
        elif choice == '4':
            loai = input("Nhập loại vật nuôi cần tìm kiếm: ")
            ql_trang_trai.tim_kiem_vat_nuoi_theo_loai(loai)
        elif choice == '5':
            ql_trang_trai.in_tat_ca_vat_nuoi()
        elif choice == '6':
            id_chuong = input("Nhập ID chuồng: ")
            vi_tri = input("Nhập vị trí chuồng: ")
            tinh_trang = input("Nhập tình trạng chuồng: ")
            chuong_moi = Chuong(id_chuong, vi_tri, tinh_trang)
            ql_trang_trai.them_chuong(chuong_moi)
        elif choice == '7':
            id_chuong = input("Nhập ID chuồng cần cập nhật: ")
            vi_tri_moi = input("Nhập vị trí mới (hoặc để trống nếu không đổi): ") or None
            tinh_trang_moi = input("Nhập tình trạng mới (hoặc để trống nếu không đổi): ") or None
            ql_trang_trai.cap_nhat_chuong(id_chuong, vi_tri_moi, tinh_trang_moi)
        elif choice == '8':
            id_chuong = input("Nhập ID chuồng cần xóa: ")
            ql_trang_trai.xoa_chuong(id_chuong)
        elif choice == '9':
            vi_tri = input("Nhập vị trí chuồng cần tìm kiếm: ")
            ql_trang_trai.tim_kiem_chuong_theo_vi_tri(vi_tri)
        elif choice == '10':
            ql_trang_trai.in_tat_ca_chuong()
        elif choice == '11':
            id_thuc_an = input("Nhập ID thức ăn: ")
            ten_thuc_an = input("Nhập tên thức ăn: ")
            so_luong = int(input("Nhập số lượng thức ăn: "))
            thuc_an_moi = ThucAn(id_thuc_an, ten_thuc_an, so_luong)
            ql_trang_trai.them_thuc_an(thuc_an_moi)
        elif choice == '12':
            id_thuc_an = input("Nhập ID thức ăn cần cập nhật: ")
            ten_thuc_an_moi = input("Nhập tên mới (hoặc để trống nếu không đổi): ") or None
            so_luong_moi_input = input("Nhập số lượng mới (hoặc để trống nếu không đổi): ")
            so_luong_moi = int(so_luong_moi_input) if so_luong_moi_input else None
            ql_trang_trai.cap_nhat_thuc_an(id_thuc_an, ten_thuc_an_moi, so_luong_moi)
        elif choice == '13':
            id_thuc_an = input("Nhập ID thức ăn cần xóa: ")
            ql_trang_trai.xoa_thuc_an(id_thuc_an)
        elif choice == '14':
            ql_trang_trai.in_tat_ca_thuc_an()
        elif choice == '15':
            id_thuc_an = input("Nhập ID thức ăn cần sử dụng: ")
            so_luong_su_dung = int(input("Nhập số lượng thức ăn cần sử dụng: "))
            ql_trang_trai.su_dung_thuc_an(id_thuc_an, so_luong_su_dung)
        elif choice == '16':
            ql_trang_trai.thong_ke_so_luong_vat_nuoi_theo_loai()
        elif choice == '17':
            ql_trang_trai.thong_ke_so_luong_chuong_theo_tinh_trang()
        elif choice == '18':
            ql_trang_trai.thong_ke_luong_thuc_an_da_su_dung()
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            
if __name__ == "__main__":
    menu()
# pip install bcrypt
# Chạy: python gen_bcrypt_vscode.py --user-id <GUID_tai_khoan>   (tùy chọn)

import argparse
import getpass
import bcrypt
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate bcrypt hash for a new password.")
    parser.add_argument("--cost", type=int, default=10, help="bcrypt work factor (default: 10)")
    parser.add_argument("--user-id", help="Nếu truyền vào, sẽ in sẵn câu lệnh SQL UPDATE với ID này")
    parser.add_argument("--table", default="dbo.KhachHang", help="Tên bảng (mặc định: dbo.KhachHang)")
    parser.add_argument("--column", default="Password", help="Tên cột mật khẩu (mặc định: Password)")
    parser.add_argument("--id-column", default="IDKhachHang", help="Tên cột ID (mặc định: IDKhachHang)")
    args = parser.parse_args()

    try:
        pwd = getpass.getpass("New password: ")
        confirm = getpass.getpass("Confirm password: ")
    except Exception as e:
        print(f"⚠️ getpass lỗi ({e}). Sẽ hiện ký tự khi nhập.")
        pwd = input("New password (visible): ")
        confirm = input("Confirm password (visible): ")

    if pwd != confirm:
        sys.exit("❌ Password nhập lại không khớp. Dừng.")

    # Tạo salt với prefix b"2a" để ra hash dạng $2a$ giống dữ liệu hiện có của bạn
    salt = bcrypt.gensalt(rounds=args.cost, prefix=b"2a")
    h = bcrypt.hashpw(pwd.encode("utf-8"), salt).decode("utf-8")

    print("\n✅ BCrypt hash (lưu vào DB):")
    print(h)

    if args.user_id:
        print("\n-- SQL UPDATE gợi ý:")
        print(f"UPDATE {args.table} SET [{args.column}] = '{h}' WHERE [{args.id_column}] = '{args.user_id}';")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nĐã hủy.")

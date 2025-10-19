import bcrypt

def main():
    new_plain = b'Demo@123'          # mật khẩu mới (bytes)
    new_hash  = bcrypt.hashpw(new_plain, bcrypt.gensalt(rounds=10))
    print("BCrypt hash (lưu vào DB):")
    print(new_hash.decode("utf-8"))

if __name__ == "__main__":
    main()
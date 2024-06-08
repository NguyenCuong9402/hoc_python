import uuid
import json
import os
from datetime import datetime

from tuan_7.fuction_1 import hien_thi_so_nv

with open("baitapvn.json", "r") as f:
    users = json.load(f)
# users = []
while True:
    print("----------------------------------------------------------------------")
    print("1. Thêm User")
    print("2. Xem thông tin User")
    print("3. Sua thong tin nhan vien")
    print("4. Xoa nhan vien")
    print("5. Danh sách các nhân viên ở tỉnh")
    print("6. Hiển thị số nhân viên nam/nữ.")
    print("7. Hiển thị số nhân viên có chuc vu")
    print("8. Thoát")
    lua_chon = int(input("Lựa Chọn Chức Năng: "))

    if lua_chon == 1:
        if len(users) == 20:
            print("Đã đủ nhân viên")
            continue
        email = input("email: ")
        duoi_emails = ['@gmail.com', '@yahoo.com', '@hotmail.com']
        flag = False
        for duoi_email in duoi_emails:
            if email.endswith(duoi_email) and len(email) > len(duoi_email):
                flag = True
                break
        if flag is False:
            print("Email không hợp lệ")
            continue
        ngay_sinh = input("Nhập Ngày Sinh(dd/mm/yy): ")
        try:
            check = datetime.strptime(ngay_sinh, "%d/%m/%Y")
            date_now = datetime.now()
            sotuoi = int(date_now.year) - int(check.year)
        except:
            print("Ngày tháng không hợp lệ")
            continue

        mat_khau = input("Nhập Mật Khẩu: ")
        if len(mat_khau) < 8:
            print("mật khẩu phải lớn hơn 8 ký tự")
            continue
        name = str(input("Họ Và Tên: ")).lower()

        phone_number = input("Số Điện Thoại: ")
        if len(phone_number) != 10:
            print("Số điện thoại không hợp lệ")
            continue
        flag = True
        for number in phone_number:
            if number not in '0123456789':
                flag = False
                break
        if flag is False:
            print("Sđt không hợp lệ")
            continue
        address = input("Địa chỉ: ")

        genderr = input("Giới Tính: ").lower()
        if genderr not in ['nam', 'nữ']:
            print("giới tính Không Hợp Lệ")
            continue
        chuc_vu = input("Chức Vụ CV: ").lower()
        if chuc_vu == "giám đốc":
            flag_chuc_vu = False
            for user in users:
                if user["chuc_vu"].lower() == "giám đốc":
                    flag_chuc_vu = True
                    break
            if flag_chuc_vu is True:
                print("Đã có giám đốc")
                continue
        date = datetime.now()
        datetimes = f"{date.hour}:{date.minute} {date.day}/{date.month}/{date.year}"
        user = {
            "id": str(uuid.uuid4()),
            "email": email,
            "birthday_date": ngay_sinh,
            "pass": mat_khau,  # Tren 8 ky tu
            "name": name,
            "phone_number": phone_number,
            "address": address,
            "gender": genderr,
            "chuc_vu": chuc_vu,
            "ngay_tao": datetimes
        }
        users.append(user)
        with open("baitapvn.json", "w") as f:
            json.dump(users, f, indent=4)
        continue

    elif lua_chon == 2:
        nhap_user = input("Thông tin nhân viên muốn tìm: ").lower()
        flag = False
        for tim_user in users:
            if tim_user['name'] == nhap_user:
                flag = True
                print(tim_user)
        if flag is False:
            print("Không Có Thông Tin Nhân Viên")
            continue
    elif lua_chon == 3:
        sua_user = input("Nhập Thông Tin Muốn Sửa: ").lower()
        for user in users:
            if user['name'] == sua_user:
                print(user)
                print("-----------------Lựa chọn thông tin muốn sửa--------------------------")
                print("1.email  2.ngày sinh  3.mật khẩu  4.Họ Tên 5.số điện thoại 6.giới tính "
                      "7.nơi ở 8.chức vụ")
                sua_thongtin = int(input("Lựa Chọn Chức Năng: "))
                if sua_thongtin == 1:
                    email = input("email: ")
                    duoi_emails = ['@gmail.com', '@yahoo.com', '@hotmail.com']
                    flag = False
                    for duoi_email in duoi_emails:
                        if email.endswith(duoi_email) and len(email) > len(duoi_email):
                            flag = True
                            user['email'] = email
                            break

                    if flag is False:
                        print("Email không hợp lệ")
                        continue
                if sua_thongtin == 2:
                    ngay_sinh = input("Nhập Ngày Sinh(dd/mm/yy): ")
                    try:
                        check = datetime.strptime(ngay_sinh, "%d/%m/%Y")
                        date_now = datetime.now()
                        sotuoi = int(date_now.year) - int(check.year)
                        user['birthday_date'] = ngay_sinh
                    except:
                        print("Ngày tháng không hợp lệ")
                        continue
                if sua_thongtin == 3:
                    matkhau = input("Nhập Mật Khẩu Muốn Đổi: ")
                    if len(matkhau) < 8:
                        print("mật khẩu phải lớn hơn 8 ký tự")
                        continue
                    user['pass'] = matkhau
                if sua_thongtin == 4:
                    hoten = input("Họ Tên Muốn Đổi: ").lower()
                    user['name'] = hoten
                if sua_thongtin == 5:
                    phone_number = input("Số Điện Thoại: ")
                    if len(phone_number) != 10:
                        print("Số điện thoại không hợp lệ")
                        continue
                    flag = True
                    for number in phone_number:
                        if number not in '0123456789':
                            flag = False
                        else:
                            user['phone_number'] = phone_number
                    if flag is False:
                        print("Sđt không hợp lệ")
                        continue
                if sua_thongtin == 6:
                    gender = input("Giới Tính Muốn Sửa: ")
                    user['gender'] = gender
                if sua_thongtin == 7:
                    address = input("Địa chỉ Muốn Sửa: ")
                    user['address'] = address

                if sua_thongtin == 8:
                    chuc_vu = input("Chức Vụ Muốn Thay: ").lower()
                    if chuc_vu == "giám đốc":
                        flag_chuc_vu = False
                        for user in users:
                            if user["chuc_vu"].lower() == "giám đốc":
                                flag_chuc_vu = True
                                user['chuc_vu'] = chuc_vu
                                break
                        if flag_chuc_vu is True:
                            print("Đã có giám đốc")
                            continue
                with open("baitapvn.json", "w") as f:
                    json.dump(users, f, indent=4)
    elif lua_chon == 4:
        print("Bạn Có Chắc Chắn Mốn Xóa hết Nhân Viên....")
        xoa_nv = input("Nếu có thì nhập nhân viên: ")
        flag = False
        for nguoi_dung in users:
            if nguoi_dung['chuc_vu'] == xoa_nv:
                users.pop(users.index(nguoi_dung))
                flag = True
                print("Đã Xóa Thành Công")
                break
        if flag is False:
            print("Không Thể Xóa không tìm thấy người dùng")
        with open("baitapvn.json", "w") as f:
            json.dump(users, f, indent=4)

    #     print("5. Danh sách các nhân viên ở tỉnh:")
    elif lua_chon == 5:
        # -> Hiển thị thêm các tỉnh có thể chọn.
        dia_chi = input("Nhầm Tỉnh Muốn Tìm : ")
        for user in users:
            if user['address'] == dia_chi:
                print("Các Nhân Viên Thuộc Tỉnh", dia_chi, "Là: ", user)

        continue

    #     print("6. Hiển thị số nhân viên nam/nữ.")
    elif lua_chon == 6:
        print("1.Số Nhân Viên Nam     2. Số Nhân Viên Nữ")
        gioi_tinh = int(input("Số Nhân Viên: "))
        so_nhan_vien_nam = len([gioi_tinh for gioi_tinh in users if gioi_tinh['gender'] == 'nam'])
        so_nhan_vien_nu = len(users) - so_nhan_vien_nam
        if gioi_tinh == 1:
            print("Số Nhân Viên Nam là :", so_nhan_vien_nam)
        else:
            print("Số Nhân Viên Nữ là :", so_nhan_vien_nu)
        continue

    #     print("7. Hiển thị số nhân viên có chuc vu (input)") # GD, TP, NV

    elif lua_chon == 7:
        result = hien_thi_so_nv()
        print(result)
        continue
    else:
        break

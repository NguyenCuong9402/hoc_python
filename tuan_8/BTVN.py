import json
import random
import uuid
# 2. Quản lý điểm sinh viên (Thông tin học sinh: tên,
# Các môn học: toán, văn, lí, hóa, sử, địa, mỹ thuật, âm nhạc, tiếng anh)

# Nhập tên sinh viên và điểm số của các môn học.

# Số học sinh giỏi/ khá / yếu.
# Hiển thị cơ cấu % học sinh yếu, khá, giỏi.  1-4: yếu, 4-8: kha, 8-10: gioi
# Tìm số học sinh có số điểm > số nhập và môn học yêu cầu.
# # ví dụ: môn học hóa, điểm là 6.
# Trả ra tất thông tin học sinh có số điểm hóa > 6
# # In kết quả ra màn hìn cảh.



# 1. Quản lý thư viện sách
# Mô tả: Xây dựng một hệ thống quản lý thư viện sách, cho phép thêm, xóa, sửa thông tin sách. Hệ thống có thể tìm kiếm sách theo tên, tác giả, thể loại, và kiểm tra tình trạng mượn/trả của sách.
# Tính năng:
# Thêm sách mới
# Cập nhật thông tin sách
# Xóa sách
# Tìm kiếm sách
# Quản lý mượn trả sách

def nhap_diem(mon):
    while True:
        try:
            diem = float(input(f"Điểm {mon}: "))
            if 0 <= diem <= 10:
                return diem
            else:
                print("Số nhập sai, vui lòng nhập lại.")

        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

def chon_chuc_nang():
    while True:
        try:
            print("1. Thêm User")
            print("2. Tính điểm trung bình của mỗi sinh viên")
            print("3. Số học sinh giỏi/ khá / yếu")
            print("4. Tăng/ giảm lương người dùng")
            chuc_nang = int(input("Chức năng muốn chọn: "))
            if chuc_nang in [1,2,3,4]:
                return chuc_nang
            else:
                print("Vui lòng nhập một số hợp lệ.")
                print("---------------------------------")


        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")
            print("---------------------------------")


with open("baitapvn.json", "r") as f:
    user = json.load(f)

while True:
    chuc_nang = chon_chuc_nang()

    if chuc_nang == 1:
        if len(user) == 20:
            print("Đã đủ nhân viên")
            continue
        ten = str(input("tên: ")).lower()
        # Validate tên
        for nguoi_dung in user:
            if nguoi_dung["tên"].lower() == ten:
                print("Người dùng đã tồn tại")
                break

        dict_diem_mon_hoc = {}
        list_mon_hoc = ["toán","văn", "lý", "hóa", "sử", "địa", "mỹ thuật", "âm nhạc", "tiếng anh"]
        for mon_hoc in list_mon_hoc:
            dict_diem_mon_hoc[mon_hoc] = nhap_diem(mon_hoc)

        users = {
            "id": str(uuid.uuid4()),
            "tên": ten,
            "ds_mon": dict_diem_mon_hoc
        }
        user.append(users)
        with open("baitapvn.json", "w") as f:
            json.dump(user, f, indent=4)
        enter = input('Enter để tiếp tiếp tục chương trình')
        continue
    # Tính điểm trung bình của mỗi sinh viên.
    elif chuc_nang == 2:
        dsten = input(" Nhầm Tên Muốn Tìm : ").lower()
        for ds_ten in user:
            if ds_ten['tên'] == dsten:
                diem = ds_ten.get("ds_mon")
                tb_mon = ((diem["toán"] + diem["văn"] + diem["lí"] + diem["hóa"] +diem["sử"] +
                     diem["địa"] + diem["mỹ thuật"] + diem["âm nhạc"] + diem["tiếng anh"])) / len(diem)
                print("Điểm Trung Bình Của Sinh Viên",ds_ten['tên'],"là: " ,tb_mon)
                continue
        enter = input('Enter để tiếp tiếp tục chương trình')
        continue

# Số học sinh giỏi/ khá / yếu.
    elif chuc_nang == 3:
        gioi = 0
        kha = 0
        tb = 0
        for ds_hoc_luc in user:
            diem = ds_hoc_luc.get("ds_mon")
            tb_mon = ((diem["toán"] + diem["văn"] + diem["lí"] + diem["hóa"] + diem["sử"] +
                       diem["địa"] + diem["mỹ thuật"] + diem["âm nhạc"] + diem["tiếng anh"])) / len(diem)
            if tb_mon > 8 and tb_mon <= 10:
                gioi += 1
            elif tb_mon > 4 and tb_mon <= 8:
                kha += 1
            elif tb_mon > 1 and tb_mon <= 4:
                tb += 1
        print("học sinh Giỏi:", gioi)
        print("học sinh kha: ", kha)
        print("học sinh Trung Bình: ", tb)
        enter = input('Enter để tiếp tiếp tục chương trình')
        continue
# Hiển thị cơ cấu % học sinh yếu, khá, giỏi.  1-4: yếu, 4-8: kha, 8-10: gioi

# Tìm số học sinh có số điểm > số nhập và môn học yêu cầu.
    elif chuc_nang == 4:
        mon_hoc = input("Môn Học: ")

        so_diem = float(input("Số Điểm: "))
        for kq, ds_hoc_luc in enumerate(user):
            diem = ds_hoc_luc.get("ds_mon")
            for mon, diem in diem.items():
                if mon == mon_hoc and diem > so_diem:
                    print(f' Số Học Sinh Thứ {kq} Là : \n ==> {ds_hoc_luc}')
            else:
                print("Không Có Môn Học Hoặc nhập sai số điểm Trong Danh Sách")
                break
        enter = input('Enter để tiếp tiếp tục chương trình')
        continue
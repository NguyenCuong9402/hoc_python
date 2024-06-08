import json
import random


# {
#     "id": "abc",
#     "email": "....@email.com"
#     "birthday_date": "dd/mm/yy"
#
#     "pass": ........ # Tren 8 ky tu
#     "name ": "Nguyen Van A"
#     "phone_number ": "0123456789"
#     "address": "xa, huyen, tinh"
#     "gender" : "nam/nu"
#     "chuc_vu" : "........."
#     "ngay_tao" : "dd/mm/yy h-m-s"
# }

with open("baitapvn.json", "r") as f:
    user = json.load(f)
# user = []
while True:
    print("---------------------------------------------------------------------------")
    print("1. Thêm User")
    print("2. Thoát")
    danh_sach = int(input("Lựa Chọn Chức Năng: "))

    if danh_sach == 1:
        if len(user) == 4:
            print("Đã đủ nhân viên")
            continue
        ten = str(input("tên: ")).lower()

        tuoi = int(input("Tuổi: "))


        users = {
                "tên": ten,
                "tuổi": tuoi,
        }

        user.append(users)
        print("Thêm ngời dùng thành công")
        with open("baitapvn.json", "w") as f:
            json.dump(user, f, indent=4)
        continue
    else:
        print("Thoát")
        break





result = {
    "find": True ,# false: khong thay, true: thay,
    "data": data_user
}

if result['find'] == True:
    print("tim thay nguoi dung", result["data"])
else:
    print("khong  tim thay")
# {
#     "find": False # false: khong thay, true: thay,
#     "data": []
# }

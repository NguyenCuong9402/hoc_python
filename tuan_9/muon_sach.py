import uuid
import json
from helper import *
from datetime import datetime

database = get_file(file_name="db.json")
list_sach = database.get("list_sach", [])
list_users = database.get("list_users", [])
so_sach_toi_da = database.get("database", 3)

luu_file(list_sach, list_users, so_sach_toi_da)

while True:
    print("1. Thêm User")
    print("2. Thêm sách")
    print("3. Mượn sách")
    print("4. trả sách")
    print("0. Thoát")
    lc = nhap_chuc_nang()
    # lay data
    database = get_file(file_name="db.json")

    list_sach = database.get("list_sach", [])
    list_users = database.get("list_users", [])
    so_sach_toi_da = database.get("database", 5)
    if lc == 1:
        # tao user mới
        list_user_new = them_user(list_users)
        # lưu data
        luu_file(list_sach, list_user_new, so_sach_toi_da)

    elif lc == 2:
        # tao user mới
        list_sach_new = them_sach(list_sach)
        # lưu data
        luu_file(list_sach_new, list_users, so_sach_toi_da)
    elif lc == 3:
        id_user = input("Nhap id_user:")
        id_sach = input("Nhap id_sach:")
        try:
            list_sach_new, list_user_new = chuc_nang_muon_sach(id_user=id_user, id_sach=id_sach, list_sach=list_sach,
                                                               list_users=list_users, so_sach_toi_da=so_sach_toi_da)
            # lưu data
            luu_file(list_sach_new, list_user_new, so_sach_toi_da)
        except Exception as ex:
            print("Mời thức hiện lại")

    elif lc == 4:
        pass
    elif lc == 0:
        break
    else:
        print("-" * 10, "Chức năng không có", "-" * 10)

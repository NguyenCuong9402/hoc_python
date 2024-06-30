import json
import uuid
from datetime import datetime


def luu_file(list_sach, list_users, so_sach_toi_da ):
    database = {"list_sach": list_sach,
                "list_users": list_users,
                "so_sach_toi_da": so_sach_toi_da}
    with open("db.json", "w") as f:
        json.dump(database, f, indent=4)


def get_file(file_name: str):
    with open(file_name, "r") as f:
        database = json.load(f)
    return database


def filter_id_in_list(list_filer: list, id: str):
    for item in list_filer:
        if item["id"] == id:
            return item
    return None


def nhap_chuc_nang():
    while True:
        try:
            lua_chon = int(input("Lựa Chọn Chức Năng: "))
            return lua_chon
        except:
            print("-"*10, "Mời nhập lại", "-"*10)


def them_user(list_users):
    ho_ten = input("Nhap ho ten: ")

    id = str(uuid.uuid4())
    danh_sach_muon = []

    user = {
        "id": id,
        "ho_ten":ho_ten,
        "danh_sach_muon": danh_sach_muon
    }
    list_users.append(user)
    return list_users


def them_sach(list_sach):
    ten_sach = input("Nhap ten sach: ")

    id = str(uuid.uuid4())
    trang_thai = {
        "cho_muon": False,
        "date_time": "",
        "id_user": ""
    }

    sach = {
        "id": id,
        "ten_sach": ten_sach,
        "trang_thai": trang_thai
    }
    list_sach.append(sach)

    return list_sach


def chuc_nang_muon_sach(id_user: str, id_sach: str, list_sach: list,
                        list_users: list, so_sach_toi_da: int):
    try:
        # Bước kiểm tra người dùng, sách có thể mượn được không.

        # check sach -> None/ {}
        check_sach = filter_id_in_list(list_filer=list_sach, id=id_sach)

        if check_sach is None:
            print("Không tìm thấy sách")
            return None

        if check_sach["trang_thai"]["cho_muon"] is True:
            print("Sách đã được mượn trước đó")
            return None


        # check user -> None/ {}
        check_user = filter_id_in_list(list_filer=list_users, id=id_user)

        if check_user is None:
            print("Không Thấy người dùng")
            return None

        if len(check_user["danh_sach_muon"]) >= so_sach_toi_da:
            print("Người dùng đã mượn tối đa sách, cần trả sách cũ.")
            return None


        # Bước hoàn thiện cho mượn
        vi_tri_sach = list_sach.index(check_sach)
        sach_cho_muon = list_sach[vi_tri_sach]

        vi_tri_user = list_users.index(check_user)
        user_muon_sach = list_users[vi_tri_user]

        date_time = str(datetime.now())

        dict_sach = {"id_sach": id_sach, "ngay_muon": date_time }
        user_muon_sach["danh_sach_muon"].append(dict_sach)
        sach_cho_muon["trang_thai"] = {
            "cho_muon": True,
            "date_time": date_time,
            "id_user": id_user
        }

        return list_sach, list_users
    except Exception as ex:
        print("Lỗi:", str(ex))
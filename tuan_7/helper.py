import json
import uuid
from datetime import datetime

# ver 1
def dang_ky(user: str, password: str):
    result = {
        "user": user,
        "password": password,
        "id": str(uuid.uuid4()) ,
        "time": datetime.now()
    }

    return result

# ver 2
def dang_ky_v2():
    list_user = []
    user = input("nhap user:")
    password = input("nhap password:")
    result = {
        "user": user,
        "password": password,
        "id": str(uuid.uuid4()),
        "time": datetime.now()
    }
    list_user.append(result)
    return "Đăngkysy thanh cong"

def hien_thi_so_nv():
    with open("baitapvn.json", "r") as f:
        users = json.load(f)

    chucvu = input("Số Nhân Viên(GD,TP,NV: ").upper()
    so_nhan_nv = len([chuc_vu2 for chuc_vu2 in users if chuc_vu2['chuc_vu'] == 'nhân viên'])
    so_nhan_tp = len([chuc_vu2 for chuc_vu2 in users if chuc_vu2['chuc_vu'] == 'trưởng phòng'])
    so_nhan_gd = len([chuc_vu2 for chuc_vu2 in users if chuc_vu2['chuc_vu'] == 'giám đốc'])
    if chucvu == "NV":
        ket_qua= f"Số nhân viên: {so_nhan_nv}"
    elif chucvu == "TP":
        ket_qua = f"Số trưởng phòng: {so_nhan_tp}"
    elif chucvu == "GD":
        ket_qua = f"Số giám đốc: {so_nhan_gd}"
    return ket_qua


def tim_dia_chia(dia_chi: str, ten: str, password: str, user_name: str, gioi_tinh: int, chuc_vuL: str):

    with open("baitapvn.json", "r") as f:
        users = json.load(f)

    list_result = []
    for user in users:
        if user['address'] == dia_chi:
            list_result.append({
                "user_name": user['name'],
                "dia_chi": user['address']
            })
    return list_result


def sua_email(email: str, user: dict):
    duoi_emails = ['@gmail.com', '@yahoo.com', '@hotmail.com']
    flag = False
    for duoi_email in duoi_emails:
        if email.endswith(duoi_email) and len(email) > len(duoi_email):
            flag = True
            user['email'] = email
            break

    if flag is True:
        result = {
            "da_sua": 1,
            "data": user
        }
    else:
        result = {
            "da_sua": 0,
            "data": user
        }
    return result







# ##########
# result = {
#     "find": True ,# false: khong thay, true: thay,
#     "data": data_user
# }
#
# if result['find'] == True:
#     print("tim thay nguoi dung", result["data"])
# else:
#     print("khong  tim thay")
# # {
# #     "find": False # false: khong thay, true: thay,
# #     "data": []
# # }
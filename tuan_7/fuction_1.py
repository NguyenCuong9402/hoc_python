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
        ket_qua=  f"Số nhân viên: {so_nhan_nv}"
    elif chucvu == "TP":
        ket_qua = f"Số trưởng phòng: {so_nhan_tp}"
    elif chucvu == "GD":
        ket_qua = f"Số giám đốc: {so_nhan_gd}"
    return ket_qua
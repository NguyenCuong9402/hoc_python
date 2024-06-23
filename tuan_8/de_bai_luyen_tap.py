

# 1. Quản lý thư viện sách
# Mô tả: Xây dựng một hệ thống quản lý thư viện sách, cho phép thêm, xóa, sửa thông tin sách.
# Hệ thống có thể tìm kiếm sách theo tên, tác giả, thể loại, và kiểm tra tình trạng mượn/trả của sách.
# Tính năng:
# Thêm sách mới
# Cập nhật thông tin sách :
        #1) Thông tin sách
        #) Thông tin tình trạng: Cho mượn rồi thì người khác mượn thông báo: Đã cho mượn
# Xóa sách
# Tìm kiếm sách
# Quản lý mượn trả sách
# Tìm những người mượn sách trong ngày Nhập.


# Mỗi người dùng chỉ mượn tối đa 3 cuốn sách


### Gợi ý thiết kế lưu data cho Quản lý thư viện sách
##Sach
# [
#     {
#         "id": "",
#         "ten_sach":"",
#         "tac_gia":"",
#         "ngay_xuat_ban":"",
#         "tinh_trang":{
#             "cho_muon": True/False,
#             "ngay_cho_muon":"",
#             "id_nguoi_muon":""
#         }
#     }
# ]
#
# ### User
# {
#     "id": {
#         "ten":"",
#         "ngay_sinh":"",
#         "dia_chi":"",
#         "sach_da_muon":[
#             {"id_sach":"",
#              "ngay_muon":""}
#         ]
#
#     }
# }


# lưu file json



list_sach = []
dict_users = {}
so_sach_toi_da = 5 # Đọc file json , sửa vào file json

database = {"list_sach":list_sach, "dict_users": dict_users, "sach_toi_da": so_sach_toi_da }



# if return "0" thì để bên anh xử lí, khác 0 thì là thành công

def chuc_nang_muon_sach(id_user : str, id_sach: str):
    #check sach
    flag_tim_sach =False
    for sach in list_sach:
        if sach["id"] == id_sach:
            flag_tim_sach = True
            if sach["tinh_trang"]["cho_muon"] == True:
                print("Sách đã cho mượn")
                return "0"
                ## Không cho xuống dưới nữa.
            break
    if flag_tim_sach is False:
        print("Sách không thấy")

    #check user
    user = dict_users.get(id_user, None)  #
    if user is None:
        print("Người dùng không tồn tại")
        return "0"

    # Kiểm tra người dùng đã mượn tối đa sách chưa
    if len(user["sach_da_muon"] >= so_sach_toi_da):
        print("Người dùng đã mượn tối đa số sách cho phép")
        return "0"

    # mượn sách
    date_time_now = "date_time_now"

    infor_sach_muon = {"id_sach":id_sach, "ngay_muon": date_time_now}

    # Điền thông tin user
    user["sach_da_muon"].append(infor_sach_muon)

    # Điền thông tin vào tình trạng sách
    for sach in list_sach:
        if sach["id"] == id_sach:
            sach["tinh_trang"]["cho_muon"] = True
            sach["tinh_trang"]["ngay_cho_muon"] = date_time_now
            sach["tinh_trang"]["id_nguoi_mon"] = id_user

    print("Mượn sách thành công")
    return "1"


# {
#         "ten":"",
#         "ngay_sinh":"",
#         "dia_chi":"",
#         "sach_da_muon":[
#             {"id_sach":"",
#              "ngay_muon":""}
#         ]
#
#     }

def chuc_nang_tra_sach(id_user : str, id_sach: str):

    # check user
    user = dict_users.get(id_user, None)  #
    if user is None:
        print("Người dùng không tồn tại")
        return "0"

    # Giả định vi_tri_tra_sach = -1
    vi_tri_tra_sach = -1
    for index , sach_muon in enumerate(user["sach_da_muon"]):
        if sach_muon["id"] == id_sach:
            # Nếu tìm thấy id sách cần trả có trong user thì gán vị trí tồn tại thật
            vi_tri_tra_sach = index

    # Check nếu khác -1 thì người dùng có mượn sách có id trên.
    if vi_tri_tra_sach != -1 :
        user["sach_da_muon"].pop(vi_tri_tra_sach)
        print("Trả sách thành công")

        # Gán lại tình trạng sách để cho khách khác mượn
        for sach in list_sach:
            if sach["id"] == id_sach:
                sach["tinh_trang"] = {
                    "cho_muon": False,
                    "ngay_cho_muon":"",
                    "id_nguoi_muon":""
                }


        return "1"
    else:
        print("Người dùng không mượn sách trên")
        return "0"




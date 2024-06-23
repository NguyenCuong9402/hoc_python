# 2. Quản lý điểm sinh viên (Thông tin học sinh: tên,
# Các môn học: toán, văn, lí, hóa, sử, địa, mỹ thuật, âm nhạc, tiếng anh)

# Nhập tên sinh viên và điểm số của các môn học.
# Tính điểm trung bình của mỗi sinh viên.
# Số học sinh giỏi/ khá / yếu.
# Hiển thị cơ cấu % học sinh yếu, khá, giỏi.  1-4: yếu, 4-8: kha, 8-10: gioi
# Tìm số học sinh có số điểm > số nhập và môn học yêu cầu.
# ví dụ: môn học hóa, điểm là 6.
# Trả ra tất cả thông tin học sinh có số điểm hóa > 6
# In kết quả ra màn hình.



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

# Mỗi người dùng chỉ mượn tối đa 3 cuốn sách


### Gợi ý thiết kế lưu data cho Quản lý thư viện sách
##Sach
[
    {
        "id": "",
        "ten_sach":"",
        "tac_gia":"",
        "ngay_xuat_ban":"",
        "tinh_trang":{
            "cho_muon": True/False,
            "ngay_cho_muon":"",
            "id_nguoi_muon":""
        }
    }
]

### User
{
    "id": {
        "ten":"",
        "ngay_sinh":"",
        "dia_chi":"",
        "sach_da_muon":[
            {"id_sach":"",
             "ngay_muon":""}
        ]

    }
}




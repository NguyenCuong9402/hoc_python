import uuid

# í dụ 1 người dùng:
# {
#     "tên": "Nguyễn Ngọc Cương",
#     "tuổi": 18,   # Tuyển nhân viên >= 18 tuổi
#     "địa chỉ": "HY", # Giới hạn chỉ chọn HN, HY, HD, QN, HP, LC, YB, BN, HB ( Còn nếu ngoài các tỉnh sau thì print
#                      # Không tuyển người ở {tỉnh nhập}
#
#     "giới tính": True, # True: nam, False: Nữ
#     "chiều cao": 171,   # Yêu cầu chiều cao > 160
#     "vị trí": "Nhân Viên",  # Giám đốc / Trưởng Phòng / Nhân Viên   # Chỉ có 1 giám đốc. Nếu đã có giám đốc thì
#     # không thể thêm user mới và print Đã có giám đốc
#     "tình trạng hôn nhân": False,  #True: đã kết hôn, False: chưa kết hôn.
#     "lương": 100,
#     "tài khoản": "cuong123",
#     "mật khẩu": "1234567"
# }


while True:
    print("1. Thêm User")
    print("2. Xem thông tin User")
    print("3. Danh sách các nhân viên ở tỉnh đã nhập")
    print("4. Tăng/ giảm lương người dùng")
    print("5. Danh sách nhân viên có lương")
    print("6. Hiển thị tổng lương phải trả hàng tháng cho mọi người")
    print("7. Hiển thị tổng số tiền phải trả trong 1 năm cho mọi người")
    print("8. Hiển thị tổng lương phải trả hàng tháng cho Nhân Viên")
    print("9. Hiển thị tổng lương phải trả hàng tháng cho Trưởng Phòng")
    print("10. Hiển thị số nhân viên nam, số nhân viên nữ.")
    print("11. Xoa nhan vien")
    print("12. Thoát")

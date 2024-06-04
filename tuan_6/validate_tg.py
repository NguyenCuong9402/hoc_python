import os

from datetime import datetime

# birth_day = input("date (d/m/Y):")
birth_day = "9/4/2002"
try:
    check = datetime.strptime(birth_day, "%d/%m/%Y")
    date_now = datetime.now()
    sotuoi = int(date_now.year) - int(check.year)
except:
    print("Ngày tháng không hợp lệ")

print("oke")

# Ấn button dang nhap
# an vao vui
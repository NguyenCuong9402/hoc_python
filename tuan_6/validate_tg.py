import os

from datetime import datetime

birth_day = input("date (d/m/Y):")
try:
    hen_gio_date_time = datetime.strptime(birth_day, "%d/%m/%Y")
except:
    print("Ngày tháng không hợp lệ")
print("oke")

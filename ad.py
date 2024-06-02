list_u = [{"gt": 1}, {"gt": 1}, {"gt": 1}, {"gt": 1}]

nhan_vien_nam = len([user for user in list_u if user['gt'] == 1])
print(nhan_vien_nam)
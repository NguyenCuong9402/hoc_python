def sua_phone_number(phone_number: str, user: dict):
    if len(phone_number) != 10:
        result = {
            "da_sua": 0,
            "data": user
        }
        return result
    flag = True
    for number in phone_number:
        if number not in '0123456789':
            flag = False
            break
    if flag is True:
        user['phone_number'] = phone_number
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
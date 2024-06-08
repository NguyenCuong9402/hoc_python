import requests
import base64
import pytesseract
from PIL import Image
import os
import uuid
# Đặt đường dẫn tới tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\test-ocr\tesseract.exe'
def demo_imagetotext(path: str):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    text = text.replace('/', '').replace("\n", '')
    return text[:4]
# URL của API
url = "https://www.8kwin.cc/api/0.0/Home/GetCaptchaForRegister"
response = requests.post(url)
# Kiểm tra xem yêu cầu có thành công hay không
if response.status_code == 200:
    data = response.json()
    image_base64 = data.get("image")
    value_key = data.get("value")

    if image_base64:
        # Giải mã base64 thành nhị phân
        image_data = base64.b64decode(image_base64)

        # Lưu ảnh dưới dạng file với đường dẫn tương đối
        image_path = f"{uuid.uuid4()}.png"
        with open(image_path, "wb") as file:
            file.write(image_data)

        # Chuyển đổi đường dẫn tương đối thành đường dẫn tuyệt đối
        absolute_image_path = os.path.abspath(image_path)

        # OCR
        text = demo_imagetotext(absolute_image_path)
        os.remove(absolute_image_path)

        payload ={
            "moneyPassword": None,
            "dealerAccount": None,
            "parentAccount": None,
            "adInfo": None,
            "email": None,
            "sex": None,
            "idNumber": None,
            "qqAccount": None,
            "groupBank": None,
            "bankName": None,
            "bankProvince": None,
            "bankCity": None,
            "bankAccount": None,
            "account": "huynhdat177",
            "password": "ebuhdfU59$",
            "confirm_Password": "ebuhdfU59$",
            "name": "HUYNH VIET THE DAT",
            "countryCode": "84",
            "mobile": "0703232516",
            "birthday": "2002/04/09",
            "checkCodeEncrypt": value_key,
            "checkCode": text,
            "isRequiredMoneyPassword": False,
            }
        api_login = "https://www.8kwin.cc/api/1.0/member/register"
        response_register = requests.post(api_login, json=payload)
        if response_register.status_code == 200:
            data = response_register.json()
            if data.get('Result') is not None and data.get('Result') != {}:
                print(f"Đăng ký thành công tài khoản")
                print("Data:", response_register.json())
            else:
                print("Đăng ký không thành công thành công")


        else:
            print("Đăng ký không thành công thành công")


    else:
        print("No image data found.")
else:
    print("Failed to retrieve captcha. Status code:", response.status_code)

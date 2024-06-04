import requests
import base64
import pytesseract
from PIL import Image
import os

# URL của API
url = "https://www.8kwin.cc/api/0.0/Home/GetCaptchaForLogin"

# Đặt đường dẫn tới tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\test-ocr\tesseract.exe'

def demo_imagetotext(path: str):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    text = text.replace('/', '').replace("\n", '')
    return text[:4]


# Gửi yêu cầu POST
response = requests.post(url)

# Kiểm tra xem yêu cầu có thành công hay không
if response.status_code == 200:
    data = response.json()
    image_base64 = data.get("image")

    if image_base64:
        # Giải mã base64 thành nhị phân
        image_data = base64.b64decode(image_base64)

        # Lưu ảnh dưới dạng file với đường dẫn tương đối
        image_path = "captcha_image.png"
        with open(image_path, "wb") as file:
            file.write(image_data)

        # Chuyển đổi đường dẫn tương đối thành đường dẫn tuyệt đối
        absolute_image_path = os.path.abspath(image_path)

        # OCR
        text = demo_imagetotext(absolute_image_path)
        print("Recognized text:", text)
    else:
        print("No image data found.")
else:
    print("Failed to retrieve captcha. Status code:", response.status_code)

from urllib import request

import requests

from file_chua_ocr import ocr


user = ""
password = ""

image = request.url("https://web.telegram.org/a/#6269043936")
def fakethietbi():
    pass

result, key_id  = ocr(image)
payload= {
  "account": "trhrthrt",
  "password": "trhrshstrhrth",
  "checkCodeEncrypt": key_id,


    "checkCode": result,
    "fingerprint": fakethietbi()
}


headers ={
'accept': 'application/json, text/plain, */*',    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',    'content-language': 'vi-VN',
    'content-length': '433',    'content-type': 'application/json;charset=UTF-8',
    'cookie': 'NG_TRANSLATE_LANG_KEY=vi; GuestVersion=2156716; MemberVersion=2156716; MarqueeVersion=53; '
              'NeverPopupDatetime=2023-04-10%2009%3A37%3A21; nohostname_ip=3734AB59AG12664276531E; '
              'AWSALB=vgksxRt9FlN6YIOIbTrtlkP1M2x0+/LPsvtE0V9WyVDalz/rv8DZ/ER5dSCfux2SAQ10N3m/t3eLO3l7O5AVBHt'
              'j5rlEYyMrM6WpJr+vYk5jeRENcv6qKKHbUcf8; AWSALBCORS=vgksxRt9FlN6YIOIbTrtlkP1M2x0+/LPsvtE0V9WyVDalz/rv8D'
              'Z/ER5dSCfux2SAQ10N3m/t3eLO3l7O5AVBHtj5rlEYyMrM6WpJr+vYk5jeRENcv6qKKHbUcf8',
    'origin': 'https://m.99win55.com',    'referer': 'https://m.99win55.com/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) ",
                  # "CriOS/104.0.5112."+str(so)+" Mobile/21E"+str(so)+" Safari/"+str(fake3)+".1",
    'x-requested-with': 'XMLHttpRequest'    }




response = requests.post("https://www.8kwin.cc/api/0.0/Home/GetCaptchaForLogin",
                             json=payload, headers=headers)
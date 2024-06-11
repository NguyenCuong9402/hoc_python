import requests
import json

url = "https://app.proxyno1.com/api/edit-key"

payload = json.dumps({
  "token": "LPDPnUVgdHRqEKtTEwL33cPgQpShwWou",
  "key": "YOUR_KEY_HERE",
  "allowip": "1.2.3.4",
  "authen": "username:password",
  "note": "",
  "auto_renew": True
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
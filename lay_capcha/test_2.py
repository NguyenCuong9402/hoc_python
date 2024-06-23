import requests
import json

def read_proxies_from_file(filename):
    proxies = []
    with open(filename, 'r') as file:
        for line in file:
            proxies.append(line.strip())
    return proxies

proxies = read_proxies_from_file('filtered_proxies.txt')

def check_ip(proxy):
    try:
        response = requests.get("https://api.ipify.org?format=json", proxies={'http': proxy, 'https': proxy}, timeout=5)
        if response.status_code == 200:
            return response.json()['ip']
    except Exception as e:
        return None

def create_accounts(proxys):
    accounts = []
    for index, proxy in enumerate(proxys):
        print(index)
        ip = check_ip(proxy)
        if ip:
            print(f"Proxy {proxy} hoạt động. IP: {ip}")
            accounts.append(proxy)
    return accounts


def save_accounts_to_file(accounts, filename):
    with open(filename, 'w') as file:
        json.dump(accounts, file, indent=4)
    print(f"Đã lưu danh sách accounts vào {filename}")


accounts = create_accounts(proxies)
save_filename = 'accounts.json'
save_accounts_to_file(accounts, save_filename)

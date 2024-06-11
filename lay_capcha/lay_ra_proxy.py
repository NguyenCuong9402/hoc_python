def read_proxies_from_file(filename):
    proxies = []
    with open(filename, 'r') as file:
        for line in file:
            proxies.append(line.strip())
    return proxies


proxy_chua_loc = read_proxies_from_file('proxy.txt')
proxy_tot = read_proxies_from_file('proxy_tot.txt')

# Danh sách các proxy đã lọc
filtered_proxies = []

# Tìm các proxy trong proxy_chua_loc cũng có trong proxy_tot
for item in proxy_tot:
    for item_2 in proxy_chua_loc:
        if item in item_2 and 'http' in item_2 :
            filtered_proxies.append(item_2)

# Ghi các proxy đã lọc vào tệp văn bản
with open("filtered_proxies.txt", "w") as file:
    for proxy in filtered_proxies:
        file.write(proxy + "\n")

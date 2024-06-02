
list_u = [["a"],"b","1", "5"]
try:
    list_u.pop(list_u.index("b"))
except:
    print("phần tử không có trong list")
print(list_u)
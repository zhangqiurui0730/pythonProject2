import time
#字符串切割
'''a = "zhangqiurui"
print(a[1:5])
print(a[1:5:2])
print(a[:])
print(a[1:])
print(a[:5])
print(a[-5:-2])
home = "chenchen and zhangqiurui and laoliu"
print(home.split("and"))

#字符串拼接效率
time01 = time.time()
for i in range(10000):
    a += "zqr"
time02 = time.time()
print(a)
print(str(time02-time01))'''

#字符串处理
zqr = "*我就是张秋，张秋就是我*"
print(len(zqr))
print(zqr.startswith("我"))
print(zqr.startswith("你"))
print(zqr.find("秋"))
print(zqr.rfind("秋"))
print(zqr.count("秋"))
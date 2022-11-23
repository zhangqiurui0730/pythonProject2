a = "zqr"
print( a*3)
b = [10,10,20,30,40]
c = ["a","b","c"]
print(len(b))
print("10出现的次数")
print(b.count(10))
#b列表中最后增加 56
b.append(56)
#b列表中删除第一次出现的10
b.remove(10)
#c列表追加到b列表
b.extend(c)
for i in range(len(b)):
    print(b[i])

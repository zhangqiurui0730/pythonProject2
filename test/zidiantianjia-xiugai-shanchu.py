a = {"name":"zqr","age":30}
b = {"name":"xiaoliu","age":"5"}
#已经有的键值去更新，没有的键值追加
a["age"] = "18"
a["addr"] = "郑州市华南城"
print(a)

#新字典中的所有键值对全部添加到旧的字典中去
a.update(b)
print(a)
print(b)

#元素删除
del a["name"]
print(a)

#删除元素，并取对应的键值对

x = a.pop("age")
print(a)
print(x)
#第一种创建字典方法
a = {"name":"zqr","age":30}
print(a)
#第二种创建字典方法
k = ["name","age"]
v = ["zqr",18]
b = dict(zip(k,v))
print(b)
#第三种创建字典方法
c = dict.fromkeys(['name','age','job'])
print(c)

#获取键值方法1
print(b["age"])

#获取键值方法2
print(b.get("name"))
print(b.get("sex"))

#列出所有键值对
print(a.items())

#列出所有的值
print(a.values())

#更新键值
a["age"] = 18
print(a)

#追加键值
a["job"] = "tester"
print(a)

#字典元素删除
a


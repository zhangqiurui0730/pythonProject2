#update 新健值全部追加到旧键值上，如果有重复直接覆盖
a = {"name":"xiaozhang","age":"20"}
b = {"name":"laozhang","age":"30","aihao":"吃"}
a.update(b)
print(a)
del (a["aihao"])
print(a)
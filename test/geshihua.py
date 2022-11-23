import builtins

a = "姓名：{0}，年龄：{1}"
print(a.format("张三","120"))

b = "姓名：{name}，年龄：{age}"
print(b.format(name='张三',age=99))
c = "数字左侧填充:{:0>2d}"
print("{:z>5d}".format(11))
m = "10"

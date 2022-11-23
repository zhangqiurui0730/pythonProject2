a = list("zhangqiurui")
print(a)
del a[0]
b = a.pop()
print(a)
print(b)
print(a.index("u",1))
print(a.index("u",2))
print(a.count('i'))

n = [10,20,10,20,30,10]

#判断是否在list里面
f = 10 in n
f2 = 100 in n
print(f)
print(f2)
#统计元素出现的次数
print(n.count(10))

#循环输出列表
for x in  n:
    print(x)

#列表排序
n.sort()
print(n)
n.sort(reverse=True)
print(n)

#列表的内置函数，最大值，最小值，合计值
print(max(n))
print(min(n))
print(sum(n))
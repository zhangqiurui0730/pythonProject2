import time
print(time.time())
now_time = '%.0f' % (time.time() * 1000)
t1 = now_time[:5]
t2 = now_time[-4:]
t3 = now_time[5:-4]
userId = t1 + t2 + t3

print(now_time)
print(t1)
print(t2)
print(t3)
print(userId)

test1 = time.time() * 1000
test2 = "{:.0f}".format(time.time() * 1000)

print("下面是新时间")
print(test2)


a = [10,20,30,40,60,50]
#从开始到索引3(不包含右边界)
print(a[:3])
#开始索引1，结束索引3
print(a[1:3])
#从索引1开始到结束
print(a[1:])
print(a[0::2])
#从倒数第二个值到最后（截取后两个）
print(a[-2:])

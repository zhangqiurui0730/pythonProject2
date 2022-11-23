#读取文件
file = open("D:/order2.txt")
content = file.read()
content2 = "["+content[:-1]+"]"

print(content2)
file.close()
#重写文件
fp = open(r'''D:/order2.txt''', "a")
fp.truncate(0)
fp.write(content2)
fp.close()
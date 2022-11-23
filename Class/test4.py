l = input('请输入字符串：')
count = 1
temp1 = ''
for index in range(1,len(l)-1):
    for acode in  range(index):
        if l[acode] == l[index]:
            acode += 1
            continue
        acode += 1
        index += 1
        count += 1
        print(count)

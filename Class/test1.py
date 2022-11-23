result = ['1','2','3','4']
for index1 in range(4):
    temp1 = result[index1]
    for index2 in range(4):
        temp2 = result[index2]
        index2 += 1
        for index3 in range(4):
            temp3 = result[index3]
            temp4 = temp1 + temp2 +temp3
            if(temp1 != temp2) and (temp1 != temp3) and (temp2 != temp3):
              print(temp4)
            index3 += 1
    index1 += 1


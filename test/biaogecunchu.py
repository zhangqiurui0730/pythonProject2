r1 = {"name":"小高","age":"18","sala":"10000"}
r2 = {"name":"小李","age":"19","sala":"20000"}
r3 = {"name":"小刘","age":"20","sala":"30000"}

ta = [r1,r2,r3]

#表格数据获取
for i in range(len(ta)):
    print(ta[i].get("sala"))
    print(ta[i].get("name"),ta[i].get("age"),ta[i].get("sala"))
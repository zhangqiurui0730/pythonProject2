a = [
    ["小张", "财务", "职员", 10000],
    ["小李", "结算", "经理", 20000],
    ["小刘", "开发", "总监", 30000],
]
# print(a)
# print(a[2][2])
for m in range(3):
    for n in range(4):
        print(a[m][n],end="\t")
    print()

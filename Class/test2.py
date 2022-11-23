l = int(input("请输入利润："))
#利润低于10万
if l < 10000 :
    result = l*0.1
    print(result)
#利润高于10万低于20万
if l in range(10000,200000):
    result = (l - 10000)*0.075 + 10000*0.1
    print(result)
#利润20-40万
#利润40-60万
#利润60-100万

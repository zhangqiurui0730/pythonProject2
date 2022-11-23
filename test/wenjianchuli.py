import xlrd
book = xlrd.open_workbook('D:\\test.xls')
print(book.sheets())
#定位到sheet1
sheet1 = book.sheet_by_name("Sheet1")
sheet1_rows = sheet1.nrows
for r in range(sheet1_rows):
    row = sheet1.row_values(r)
    user = sheet1.cell_value(r,0)
    pwd = sheet1.cell_value(r,1)
    userpwd = user + pwd
    #print(r,row)
    #print(user)
    #print(pwd)
    print(userpwd)
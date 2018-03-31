import xlrd
workbook = xlrd.open_workbook(r'E:\test\1.xlsx')
#抽取EXCEL文件

sheet1 = workbook.sheet_by_name('Sheet1')
#提取文件中的表
nRow=sheet1.nrows
nCol=sheet1.ncols
print(nRow)
print(nCol)
list1=[]
for i in range(1,nRow):
  list1.append(str(sheet1.row_values(i)[3]))
  #找到列表中的基因型
  for k in list1:
    gene1=k.split(";")
  for m in gene1:
    if m=='AMEL:X' and int(str(sheet1.row_values(i)[1])[16])%2==1:
        print(str(sheet1.row_values(i)[0]))
    if m=='AMEL:X,Y' and int(str(sheet1.row_values(i)[1])[16])%2==0:
        print(str(sheet1.row_values(i)[0]))

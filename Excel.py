import xlsxwriter

workbook = xlsxwriter.workbook("Test_PYthon_Excel.xlsx")
worksheet = workbook.add_worksheet("TestSheet")

data = "Om Muruga !!!"

#Setup Column Header
worksheet.write(0,0,"S.No")
worksheet.write(0,1,"Name")
worksheet.write(0,2,"Phone")

#Input Row Data for 1 Row/Record
worksheet.write(1,0,"1")
worksheet.write(1,1,"Senthilkumar.C")
worksheet.write(1,2,"+1 571-524-7431")



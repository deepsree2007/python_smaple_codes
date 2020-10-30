from DBConnection import DBConnection

count = int(input("how many employees ? "))
listofemps =[]
dbCon = DBConnection()
for i in range(count):
    empid =int(input("enter employee id : "))
    empname = input("enter employee name : ")
    address = input("enter employee address :")
    listofemps.append((empid,empname,address))

print(dbCon.insertdata(listofemps), " records are inserted in db")

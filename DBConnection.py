import mysql.connector

class DBConnection:
    con = None
    csr = None
    
    def __init__(self):
        if DBConnection.con==None:
            DBConnection.con = mysql.connector.connect(database='employee', user='root', password='',host='localhost')
            print("connection : ", DBConnection.con)
            DBConnection.csr = DBConnection.con.cursor()
            print("cursor : ", DBConnection.csr)
            
    def insertdata(self, rows):
        query = "insert into emp(emp_id, emp_name,address) values (%s,%s,%s)"
        DBConnection.csr.executemany(query, rows)
        DBConnection.con.commit()
        return DBConnection.csr.rowcount

    
       
    

    

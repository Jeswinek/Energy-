import mysql.connector

myconn = mysql.connector.connect(host="localhost",user="adminpi",passwd="#aA12345678",database="iemcs")
cur = myconn.cursor()
try:
 #dbs=cur.execute("create table Metre(slno int(20)not null,date DATE,time time)")
 cur.execute("alter table Metre add unit int(20)not null")

except:
 myconn.rollback()

myconn.close()

import pandas as pd
from mysql.connector import connect
mydb = connect(host='localhost', user='root', passwd='1234', database='arsalan_database')

mycursor = mydb.cursor()


mycursor.execute("select * from table1")

result = mycursor.fetchall()
result.DataFrame()

pd.read_sql("select * from table1", mydb)

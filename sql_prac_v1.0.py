import pandas as pd
from mysql.connector import connect

conn = connect(user='root', passwd='1234', host='127.0.0.1', db='arsalan_database')
mycursor = conn.cursor()


pd.read_sql("Select * from table1", conn)


mycursor.execute(
    "INSERT INTO table1 (id, first_name,	last_name,	salary) VALUES (100,'Syed Arsalan', 'Amin', 100)")
conn.commit()

# TODO: USing the execute statement

mycursor.execute("select * from table1 where")

import pandas as pd
from mysql.connector import connect

conn = connect(user='root', passwd='1234', host='127.0.0.1', db='arsalan_database')
mycursor = conn.cursor()


pd.read_sql("Select * from table1", conn)


mycursor.execute(
    "INSERT INTO table1 (id, first_name,	last_name,	salary) VALUES (170,'sultan', 'tipu', 170)")
conn.commit()

# TODO: Using the Where statement

mycursor.execute("select * from table1 where salary >= %s",
                 (40,))  # thid %s will prevent sq injection
result = mycursor.fetchall()

for i in result:
    print(i)


# TODO: Using the count statement(tells the rows)

mycursor.execute("select count(*) from table1")
result = mycursor.fetchall()

for i in result:
    print(i)


# TODO: Using order by, offset, limit:

mycursor.execute("Select * from table1 order by salary Desc  limit 1 offset 0")
result = mycursor.fetchall()
for i in result:
    print(i)

# TODO: Using order by, offset, limit:

mycursor.execute("Select * from table1")
result = mycursor.fetchall()
for i in result:
    print(i)

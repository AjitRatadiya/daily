import psycopg2

hostname = '127.0.0.1'
database = 'test'
username = 'postgres'
pwd = 'ajit'
port_id = 5432

conn = psycopg2.connect(user=username, database=database, password=pwd, host=hostname, port=port_id)  # pass database param if created
conn.autocommit = True

# # create database
# q = "CREATED DATABASE trade"
cur = conn.cursor()
# # create table
# q = "CREATE TABLE orderbook"
# # insert data into table
# q = "INSERT INTO emp (id,name) VALUES (2, 'mahesh')"
# insert multipal data into table
# data = [(3,'kamal'),(4, 'prakash'),(5, 'pramod')]
# for d in data:
#     cur.execute("INSERT INTO emp (id,name) VALUES('{a}','{b}')".format(a=d[0],b=d[1]))
# findAll data from table
# q = "SELECT * FROM emp ORDER BY id"
# # findOne data from table
# q = "SELECT * FROM emp WHERE name='1'"
# # find data from table with name only
# q = "SELECT name FROM emp"
# # delete data from table
# q = "DELETE FROM emp WHERE id='3' OR id='3' OR id='4'"
# # delete all
# q = "DELETE FROM emp"
# # updare data
# q = "UPDATE emp SET name='subham' WHERE name='pramod'"
# # drop table
# q = "DROP TABLE emp"
# cur.execute(q)
print(cur.fetchall())
print("inserted")
cur.close()
conn.close()

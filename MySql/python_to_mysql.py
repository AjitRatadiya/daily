from mysql import connector
conn = connector.connect(host='127.0.0.1', database='emp', user='root', password='ajit')
conn.autocommit = True
cur = conn.cursor()
# create database
# q = "CREATE DATABASE test"

# create table
# q = "CREATE TABLE emp (id int, name VARCHAR(255))"

# insert one
# q = "INSERT INTO emp (id, name) VALUES(1,'ajit')"
# insert many
# data = [(2,'bhimo'),(3,'kunal')]
# q = "INSERT INTO emp (id, name) VALUES(%s, %s)"
# cur.executemany(q, data)

# find one
# q = "SELECT * FROM emp WHERE name='ajit'"
# find Many
# q = "SELECT * FROM emp"

# update
# q = "UPDATE emp SET name='aj' WHERE name='ajit'"

# delete
# q = "DELETE FROM emp WHERE id=3"

# cur.execute(q)
# print(cur.fetchall())
print("OK")

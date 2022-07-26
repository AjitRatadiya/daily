import socket

s = socket.socket()
s.bind(('127.0.0.1', 9999))
s.listen(5)


con, add = s.accept()
print(add)
rec = con.recv(10000)
print(rec.decode())

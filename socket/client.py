import socket

c = socket.socket()
c.connect(("127.0.0.1", 9999))
str = "NORMAL,ADANIGREEN-EQ,BUY,NSE,MARKET,MARGIN,DAY,0.00,0.00,0.00,5,STRN001"
c.sendall(str.encode())


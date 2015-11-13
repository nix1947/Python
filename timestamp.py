#!/usr/bin/env python

import socket
from time import ctime

HOST = '' #can use any available address
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Used Inet socket family and tcp socket
tcp_sock.bind(ADDR)
tcp_sock.listen(5)	# 5: maximum no of tcp connection can accept before refused

while True:
	print("Waiting for connection")
	cli_sock, addr = tcp_sock.accept()
	print("Connected from %s" % str(addr))

	while True:
		data = cli_sock.recv(BUFSIZ)
		if not data:
			break
		cli_sock.send('[%s] %s' %(ctime(), data))
	
	cli_sock.close()
tcp_sock.close()


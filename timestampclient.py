#!/usr/bin/env python
import socket

HOST = '127.0.0.1'
PORT = 21567
BUFFER_SIZE = 1024
ADDR = (HOST, PORT)

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_sock.connect(ADDR)

while True:
	data = raw_input(">")
	if not data:
		break
	cli_sock.send(data)
	recv_data = cli_sock.recv(BUFFER_SIZE)
	if not recv_data:
		break
	print recv_data

cli_sock.close()

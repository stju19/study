#!/usr/bin/python

from socket import *

HOST = 'localhost'
PORT = 8088
BUFSIZ = 1024
ADDR = (HOST, PORT)

cliSock = socket(AF_INET, SOCK_STREAM)
cliSock.connect(ADDR)

while True:
    data = raw_input('>')
    if not data:
        break
    cliSock.send(data)
    data = cliSock.recv(BUFSIZ)
    if not data:
        break
    print data

cliSock.close()

#!/usr/bin/python

from socket import *
from time import ctime

HOST = ''
PORT = 8088
BUFSIZ = 1024
ADDR = (HOST, PORT)
serSock = socket(AF_INET, SOCK_STREAM)
serSock.bind(ADDR)
serSock.listen(5)

while True:
    print 'Waiting for connection...'
    cliSock, addr = serSock.accept()
    print '...connected from ', addr

    while True:
        data = cliSock.recv(BUFSIZ)
        if not data:
            break
        cliSock.send('[{0}] {1}'.format(ctime(), data))

cliSock.close()
serSock.close()

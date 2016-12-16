#!/usr/bin/env python

from socket import *
from time import ctime
from SocketServer import (TCPServer as TCP,StreamRequestHandler as SRH)

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)
def tcpServer():
    tcpServSocket = socket(AF_INET,SOCK_STREAM)
    tcpServSocket.bind(ADDR)
    tcpServSocket.listen(5)
    try:
        while True:
            print "waiting for connection..."
            tcpCliSock,addr = tcpServSocket.accept()
            print "...connected from:",addr    
            while True:
                data = tcpCliSock.recv(BUFSIZE)
                if not data:
                    break
                tcpCliSock.send("[%s]%s"%(ctime(),data))
            tcpCliSock.close()

    except KeyboardInterrupt:
        tcpServSocket.close()

def udpServer():
    udpServSock = socket(AF_INET,SOCK_DGRAM)
    udpServSock.bind(ADDR)
    try:
        while True:
            print "waiting for message..."
            data,addr = udpServSock.recvfrom(BUFSIZE)
            udpServSock.sendto("[%s]%s"%(ctime(),data),addr)
            print "[%s]%s"%(ctime(),data)
            print "...recvfrom and returned to:",addr
    except KeyboardInterrupt:
        udpServSock.close()
    
class MyRequestHandler(SRH):
   def handle(self):
       print "...connected from:",self.client_address
       self.wfile.write("[%s]%s"%(ctime(),self.rfile.readline()))
       

#tcpServ = TCP(ADDR,MyRequestHandler)
#print "waiting for connection..."
#tcpServ.serve_forever()
udpServer()
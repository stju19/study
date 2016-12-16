#!/usr/bin/env python

from socket import *
import struct
HOST = "10.43.211.99"
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)
def tcpCli():
    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    while True:
        data = raw_input('::')
        if not data:
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        print data,data.strip()
        
    tcpCliSock.close()

def udpCli():
    udpCliSock = socket(AF_INET,SOCK_DGRAM)
    while True:
        data = raw_input(">")
        if not data:
            break
        udpCliSock.sendto(data,ADDR)
        data,addr = udpCliSock.recvfrom(BUFSIZE)
        if not data:
            break
        print data
    udpCliSock.close()

def checksum(source_string):
    sum = 0
    countTo = (len(source_string)/2)*2
    count = 0
    while count<countTo:
        thisVal = ord(source_string[count + 1])*256 + ord(source_string[count])
        sum = sum + thisVal
        sum = sum & 0xffffffff 
        count = count + 2
    if countTo<len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff 
    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer
 
def rawCli():
    rawCliSock = socket(AF_INET,SOCK_RAW,IPPROTO_UDP)
    rawCliSock.setsockopt(IPPROTO_IP,IP_HDRINCL,1)
    source_ip = '10.43.174.121'
    dest_ip = '10.43.211.99'
    # ip header fields
    ihl = 5
    version = 4
    tos = 0
    id = 0
    frag_off = 16384
    ttl = 128
    protocol = 17
    check = 0
    saddr =inet_aton(source_ip)
    daddr = inet_aton(dest_ip)
    ihl_version = (version << 4) + ihl
    
    #udp header
    source_port = 21567
    des_port = 21567
    check1 = 0
    
    
    while True:
        data = raw_input(">")
        if not data:
            break
        dt = len(data)
        tot_len = 28+dt
        ludp = 8 + dt
        ip_header = struct.pack('!BBHHHBBH4s4s', ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)
        check = checksum(ip_header)
        ip_header = struct.pack('!BBHHHBBH4s4s', ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)
        puppet_header = struct.pack("!4s4sBBH",saddr,daddr,0x00,protocol,ludp)
        udp_header = struct.pack("!HHHH",source_port,des_port,ludp,check1)
        check2= checksum(puppet_header+udp_header+data)
        udp_header = struct.pack("!HHHH",source_port,des_port,ludp,check2)
        rawCliSock.sendto(ip_header+udp_header+data,ADDR)
        #data,addr = rawCliSock.recvfrom(BUFSIZE)
        #if not data:
        #    break
        #print addr
    rawCliSock.close()

rawCli()
#!/usr/bin/env python3
from socket import *
from time import ctime
import threading

HOST='172.16.45.135'
PORT=21569
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)  #socket
tcpCliSock.connect(ADDR)                #connect

while True:
    data=raw_input('> ')
    if not data:
        break
    tcpCliSock.send('[%s] %s' %(ctime(),data))  #send
    data=tcpCliSock.recv(BUFSIZ)                #receive
    if not data:
        break
    print data

tcpCliSock.close()                      #close

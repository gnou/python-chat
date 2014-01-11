#!/usr/bin/env python

from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)  #socket
tcpSerSock.bind(ADDR)                   #bind
tcpSerSock.listen(5)                    #listen

while True:
    print 'waiting for connection...'
    tcpCliSock.addr=tcpSerSock.accept() #accept
    print '...connected from:',addr

    while True:
        data=tcpCliSock.recv(BUFSIZ)    #receive
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(ctime(),data))  #send

tcpCliSock.close()                      #close

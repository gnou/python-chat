#!/usr/bin/env python

from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM) #生成tcp服务器的套接字
tcpSerSock.bind(ADDR) #把套接字绑定到服务器的地址上
tcpSerSock.listen(5)  #最多允许5个连接同时连进来，后来的连接就会被拒绝

while True:
        print 'waiting for connection...'
            tcpCliSock,addr=tcpSerSock.accept() #等待连接（被动等待），阻塞式的
                print '...connected from:',addr

                    while True:
                                data=tcpCliSock.recv(BUFSIZ)
                                        if not data:
                                                        break
                                                            tcpCliSock.send('[%s] %s' %(ctime(),data))

                                                            tcpCliSock.close()

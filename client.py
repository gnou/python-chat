
m socket import *
from time import ctime
import threading
HOST='172.16.45.135'
PORT=21569
BUFSIZ=1024
ADDR=(HOST,PORT)  #服务器的地址与端口

tcpCliSock=socket(AF_INET,SOCK_STREAM) #生成客户端的套接字，并连上服务器
tcpCliSock.connect(ADDR)

while True:
        data=raw_input('> ')
            if not data:
                        break
                        tcpCliSock.send('[%s] %s' %(ctime(),data)) #发送时间与数据
                            data=tcpCliSock.recv(BUFSIZ) #接收服务器的发送过来的数据
                                if not data:
                                            break
                                            print data

                                            tcpCliSock.close()

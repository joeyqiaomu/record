 # **<font color=Red> SocketServer**


```python
import socketserver
import threading

class MyHandle(socketserver.BaseRequestHandler):


    def handle(self):
        super().handle()
        print(self.request)
        print(self.client_address)
        print(self.server)

        print(self.__dict__)
        print(self.server.__dict__)

        for i in range(3):
            data = self.request.recv(1024)
            print(data)
            msg = 'server resv msg = {}'.format(data.decode()).encode()
            self.request.send(msg)

        print(threading.enumerate())
        print(threading.current_thread())
        print()


#server = socketserver.TCPServer(('127.0.0.1', 9999), MyHandle)#单线程
server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyHandle)#多线程
print(server)
server.serve_forever()# 默认阻塞行为
'''
总结
创建服务器需要几个步骤:
1. 从BaseRequestHandler类派生出子类,并覆盖其handle()方法来创建请求处理程序类,此方法将处理传入请
求
2. 实例化一个服务器类,传参服务器的地址和请求处理类
3. 调用服务器实例的handle_request()或serve_forever()方法
4. 调用server_close()关闭套接字
'''
```


 ## **<font color=Red>实现EchoServer**


```python

import socketserver
import threading

class MyHandle(socketserver.BaseRequestHandler):

    def setup(self):
        super().setup()
        self.event = threading.Event()

    def finish(self):
        super().finish()
        self.event.set()

    def handle(self):
        super().handle()
        print(self.request)
        print(self.client_address)
        print(self.server)

        print(self.__dict__)
        print(self.server.__dict__)

        while True:
            data = self.request.recv(1024)
            print(data)
            msg = 'server resv msg = {}'.format(data.decode()).encode()
            self.request.send(msg)

        print(threading.enumerate())
        print(threading.current_thread())
        print()


#server = socketserver.TCPServer(('127.0.0.1', 9999), MyHandle)#单线程
server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyHandle)#多线程
print(server)

threading.Thread(target=server.serve_forever,name='serverforever').start()
print('server')
while True:
    cmd = input(">>>>>>>>>>>>")
    if cmd == 'quit':
        server.server_close()
        print('byt')
        break
    print(threading.enumerate())



```
```python
import socket
import time
import datetime
import threading
import logging


import socketserver
import threading


FORMAT = '%(asctime)s %(process)s %(processName)s\t%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class MyHandle(socketserver.BaseRequestHandler):

    clients = {}

    def setup(self):
        super().setup()
        self.event = threading.Event()
        self.clients[self.client_address] = self.request

    def finish(self):
        super().finish()
        self.clients.pop(self.client_address)
        self.event.set()

    def handle(self):
        super().handle()
        clientinfo = self.client_address
        while not self.event.is_set():
            data = self.request.recv(1024)
            #data = b''
            if data.strip() == b'' or data == b'bye':
                logging.info('{} quits'.format(clientinfo))
                break
            print(data)
            msg = '{:%Y/%m/%d %H:%M:%S} [{}:{}] -{}'.format(datetime.datetime.now(), *clientinfo, data.decode())
            logging.info(msg)
            msg = msg.encode()
            for v in self.clients.values():
                v.send(msg)

cs = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyHandle)#多线程
print(cs)
cs.daemon_threads = True
threading.Thread(target=cs.serve_forever,name='serverforever').start()

while True:
    cmd = input(">>>>>>>>>>>>>").strip()
    if cmd == 'quit':
        print(cmd)
        cs.server_close()
        print(cmd)
        threading.Event().wait(3)
        break

    logging.info(threading.enumerate())

logging.info(threading.enumerate()) # 用来观察断开后线程的变化
logging.info(cs.clients)
```

```python
import socket
import time
import datetime
import threading
import logging


import socketserver
import threading


FORMAT = '%(asctime)s %(process)s %(processName)s\t%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class MyHandle(socketserver.StreamRequestHandler):

    clients = {}

    def setup(self):
        super().setup()
        self.event = threading.Event()
        self.clients[self.client_address] = self.rfile,self.wfile

    def finish(self):
        super().finish()
        self.clients.pop(self.client_address)
        self.event.set()

    def handle(self):
        super().handle()
        clientinfo = self.client_address
        while not self.event.is_set():
            #data = self.request.recv(1024)
            data = self.rfile.read1(1024)
            #data = b''
            if data.strip() == b'' or data == b'bye':
                logging.info('{} quits'.format(clientinfo))
                break
            print(data)
            msg = '{:%Y/%m/%d %H:%M:%S} [{}:{}] -{}'.format(datetime.datetime.now(), *clientinfo, data.decode())
            logging.info(msg)
            msg = msg.encode()
            for v in self.clients.values():
                #v.send(msg)
                v.write(msg)
                v.flush()

cs = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyHandle)#多线程
print(cs)
cs.daemon_threads = True
threading.Thread(target=cs.serve_forever,name='serverforever').start()

while True:
    cmd = input(">>>>>>>>>>>>>").strip()
    if cmd == 'quit':
        print(cmd)
        cs.server_close()
        print(cmd)
        threading.Event().wait(3)
        break

    logging.info(threading.enumerate())

logging.info(threading.enumerate()) # 用来观察断开后线程的变化
logging.info(cs.clients)
```

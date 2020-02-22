# **<font color=Red> selcet**

```python

import selectors
import socket

'''
Python的select库实现了select、poll系统调用,这个基本上操作系统都支持。部分实现了epoll。它是底层的IO多
路复用模块。
开发中的选择
1、完全跨平台,使用select、poll。但是性能较差
2、针对不同操作系统自行选择支持的技术,这样做会提高IO处理的性能
select维护一个文件描述符数据结构,单个进程使用有上限,通常是1024,线性扫描这个数据结构。效率低。
pool和select的区别是内部数据结构使用链表,没有这个最大限制,但是依然是线性遍历才知道哪个设备就绪了。
epoll使用事件通知机制,使用回调机制提高效率。
select/poll还要从内核空间复制消息到用户空间,而epoll通过内核空间和用户空间共享一块内存来减少复制


类层次结构..
BaseSelector
+-- SelectSelector 实现select
+-- PollSelector 实现poll
+-- EpollSelector 实现epoll
+-- DevpollSelector 实现devpoll
+-- KqueueSelector 实现kqueue
'''

s = selectors.DefaultSelector()#拿到selctor


#类文件对象
server = socket.socket()
server.bind(("127.0.0.1",99))
server.listen()

#官方建议采用费阻塞
server.setblocking(False)


def accept():
    conn ,raddr = server.accept()
    print(conn)
    print(raddr)

key = s.register(server,selectors.EVENT_READ,accept)

print(key)

events = s.select()#默认是阻塞的，当你注册的文件对象们　这其中的至少一个对象关注的事件就绪了，就不足赛了， 获取了就绪的对象们，包括就绪的事件，还返回ｄａｔａ

print(events)

for key,mask in events:# event ==> and mask
    print(type(key),type(mask))
    print(key.data)


server.close()
s.close()


```


代码１

```python


import selectors
import socket



s = selectors.DefaultSelector()#拿到selctor


#类文件对象
server = socket.socket()
server.bind(("127.0.0.1",9999))
server.listen()

#官方建议采用费阻塞
server.setblocking(False)
from selectors import SelectorKey
#namedtuple？？
def accept(sock:socket.socket,mask:int):
    # conn ,raddr = server.accept() #观察现象
    # print(conn)
    # print(raddr)
    pass
key = s.register(server,selectors.EVENT_READ,accept)
print(key)
print(key.__class__)

print(key)

while True:
    events = s.select()#默认是阻塞的，当你注册的文件对象们　这其中的至少一个对象关注的事件就绪了，就不足赛了， 获取了就绪的对象们，包括就绪的事件，还返回ｄａｔａ

    print(events)

    for key,mask in events:# event ==> and mask
        print(type(key),type(mask))
        print(key.data)
        key.data(key.fileobj,mask)


server.close()
s.close()

```


##### **<font color=Red> 代码２　单聊**

```python

import selectors
import socket



s = selectors.DefaultSelector()#拿到selctor


#类文件对象
server = socket.socket()
server.bind(("127.0.0.1",9999))
server.listen()

#官方建议采用费阻塞
server.setblocking(False)
from selectors import SelectorKey
#namedtuple？？


def recv(conn:socket.socket,mask:int):
    data = conn.recv(1024)
    print(data)
    msg = 'your msg = {} from {}'.format(data.decode(),conn.getpeername()).encode()
    conn.send(msg)


def accept(sock:socket.socket,mask:int):
    conn ,raddr = server.accept()
    print(conn)
    print(raddr)
    sock.setblocking(False)
    key = s.register(conn,selectors.EVENT_READ,recv)
    print(key)


key = s.register(server,selectors.EVENT_READ,accept)
# print(key)
# print(key.__class__)

print(key)

while True:
    events = s.select()#默认是阻塞的，当你注册的文件对象们　这其中的至少一个对象关注的事件就绪了，就不足赛了， 获取了就绪的对象们，包括就绪的事件，还返回ｄａｔａ

    print(events)

    for key,mask in events:# event ==> and mask
        print(type(key),type(mask))
        print(key.data)
        key.data(key.fileobj,mask)


server.close()
s.close()

```


```python
import selectors
import socket
import datetime
import threading
import logging

FORMAT = '%(asctime)s %(process)s %(processName)s\t%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class CharServer:

    def __init__(self,ip='127.0.0.1',port=9999):
        self.sock = socket.socket()
        self.addr = ip,port
        self.event = threading.Event()
        self.selector = selectors.DefaultSelector()

    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        self.sock.setblocking(False)

        key = self.selector.register(self.sock,selectors.EVENT_READ,self.accept)
        logging.info('selector-----',key)

        threading.Thread(target=self.select,name='select',daemon=True).start()

    def select(self):
        while not self.event.is_set():
            events = self.selector.select()
            for key,mask in events:
                key.data(key.fileobj,mask)

    def accept(self,sock:socket.socket,mask):
        conn,raddr = sock.accept()
        conn.setblocking(False)
        key = self.selector.register(conn,selectors.EVENT_READ,self.recv)
        logging.info('accept-----',key)

    def recv(self,conn:socket.socket,mask):
        data = conn.recv(1024)
        print(data)
        if data.strip() == b'' or data.strip() == b'quit':
            self.selector.unregister(conn)
            conn.close()
            return

        for key in self.selector.get_map().values():

            #if key.fileobj is self.sock:continue

            # print(key.data)
            # print(self.recv)
            # print(key.data is self.recv)
            # print(key.data == self.recv)
            if key.data == self.recv:
                msg = 'your msg = {} from {}'.format(data.decode(), conn.getpeername()).encode()
                s = key.fileobj
                s.send(msg)

    def stop(self):
        self.event.set()
        fs = []
        for fd,key in self.selector.get_map().items():
            fs.append(key)
        for f in fs:
            self.selector.unregister(f)
            f.close()
        self.selector.close()

if __name__ == '__main__':
    cc =CharServer()
    cc.start()
    while True:
        cmd = input(">>>>>>>>>>>>>").strip()
        if cmd == 'quit':
            cc.stop()
            break
        logging.info(threading.enumerate())
        logging.info(list(cc.selector.get_map().keys()))
        #logging.info(len(list(cc.selector.get_map().keys())))
        for fd,key in cc.selector.get_map().items():
            print(fd)
            print(key)
            print()
```

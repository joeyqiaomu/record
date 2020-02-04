# 概念
```
线程同步
  概念
    线程同步,线程间协同,通过某种技术,让一个线程访问某些数据时,其他线程不能访问这些数据,直到该线程完
成对数据的操作。
Event ***
   Event事件,是线程间通信机制中最简单的实现,使用一个内部的标记flag,通过flag的True或False的变化来进行
操作。
```
| 名称               |                                    含义                                     |
|:------------------ |:---------------------------------------------------------------------------:|
| set()              |                               标记设置为True                                |
| clear()            |                               标记设置为False                               |
| is_set()           |                               标记是否为True                                |
| wait(timeout=None) | 设置等待标记为True的时长,None为无限等待。等到返回True,未等到超时了返回False |

# **event**

```python
from threading import Event, Thread
import logging
import time
FORMAT = '%(asctime)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

#flag = False
event = Event() #全局的event事件
print(event.isSet()) #初始值为false

def boss(event:Event):
    logging.info("I'm boss, waiting for U")
    event.wait()# 阻塞等待
    # while not flag:
    #     time.sleep(0.5)
    logging.info('Good Job.')


def worker(e:Event, count=10):
    logging.info('I am working for U')
    cups = []
    # global flag
    while True:
        logging.info('make 1 cup')
        time.sleep(0.5)
        if len(cups) >= count:
            break
        cups.append(1)
    # flag = True
    logging.info('I finished my job. cups={}'.format(cups))
    event.set()


b = Thread(target=boss, name='boss', args=(event,))
w = Thread(target=worker, name='worker', args=(event,))
b.start()
w.start()

print("==============end================")
```
## wati的时间
```python
from threading import Event, Thread
import logging
import time
FORMAT = '%(asctime)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def worker(event:Event, interval:int):
    while not event.wait(interval): # 等待的时间的间隔
    # while not event.is_set():
    #     time.sleep(interval)
        logging.info('do sth.')
    print("game over")


e = Event()
Thread(target=worker, args=(e, 8)).start()

e.wait(10) # 等待
e.set()
print('====end====')
```

## time
```python
from threading import Event, Thread
import logging
import time
import threading
FORMAT = '%(asctime)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

'''
threading.Timer继承自Thread,这个类用来定义延迟多久后执行一个函数。
class threading.Timer(interval, function, args=None, kwargs=None)
start方法执行之后,Timer对象会处于等待状态,等待了interval秒之后,开始执行function函数的。
'''
def worker():
    print("game over")


t = threading.Timer(8, worker)
t.setDaemon(False)
t.start()
t.cancel()

'''
上例代码工作线程早就启动了,只不过是在工作线程中延时了4秒才执行了worker函数。
Timer是线程Thread的子类,Timer实例内部提供了一个finished属性,该属性是Event对象。cancel方法,本质上
是在worker函数执行前对finished属性set方法操作,从而跳过了worker函数执行,达到了取消的效果。
总结
Timer是线程Thread的子类,就是线程类,具有线程的能力和特征。
它的实例是能够延时执行目标函数的线程,在真正执行目标函数之前,都可以cancel它。
cancel方法本质使用Event类实现。这并不是说,线程提供了取消的方法。
'''
print('====end====')
```
# **lock**
### 锁,一旦线程获得锁,其它试图获取锁的线程将被阻塞
### 锁:凡是存在共享资源争抢的地方都可以使用锁,从而保证只有一个使用者可以完全使用这个资源。


| 名称               |                                    含义                                     |
|:------------------ |:---------------------------------------------------------------------------:|
|     acquire(blocking=True,timeout=-1)       |                               默认阻塞,阻塞可以设置超时时间。非阻塞时,timeout禁止设置成功获取锁,返回True,否则返回False                                |
|release()        |                              释放锁。可以从任何线程调用释放。已上锁的锁,会被重置为unlocked未上锁的锁上调用,抛RuntimeError异常。                        |




```python
import threading

event = threading.Event()
lock = threading.Lock()

print(lock.acquire())
print(lock.acquire(timeout=2))
print(lock.acquire(False))

def worker(l:threading.Lock):
    print('enter---------------')
    l.acquire()
    print('exit---------------',threading.current_thread().name)

for i in range(10):
    threading.Thread(target=worker,args=(lock,)).start()

event.wait(2)

while True:
    cmd = input('>>>').strip()
    if cmd == 'quit':
        break
    elif cmd == 'r':
        lock.release()
    else:
        print(threading.enumerate())


```
```python

import threading
import logging
import time
Format = '%(asctime)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=Format,level=logging.INFO)

event = threading.Event()
lock = threading.Lock()
cups = []


def worker(cup,l:threading.Lock):
    logging.info("{} is workding ".format(threading.current_thread().name))
    flag = False
    #while len(cups) < cup:# 当cup为999的时候，线程的切换，
    while True:
        time.sleep(0.01)
        l.acquire()
        if len(cups) >= cup:
            flag = True
        #l.release()
        if not flag:
            cups.append(1)
        l.release()
        if flag:
            break
    logging.info("{} finished my job.cups={}".format(threading.current_thread().name,len(cups)))


for i in range(10):
    threading.Thread(target=worker,name='worker={}'.format(i+1),args=(10000,lock)).start()

# event.wait(2)
#
# while True:
#     cmd = input('>>>').strip()
#     if cmd == 'quit':
#         break
#     elif cmd == 'r':
#         lock.release()
#     else:
#         print(threading.enumerate())
#
#
```


## balance


```python

import threading
from threading import Thread, Lock
import time



class Counter:
    def __init__(self):
        self._val = 0
        self._lock = threading.Lock()

    @property
    def value(self):
        with self._lock:
            return self._val

    def inc(self):
        with self._lock:
            self._val += 1
            try:
                Exception
            except:
                self._val -= 1

    def dec(self):
        self._lock.acquire()
        try:
            self._val -= 1
        finally:
            self._lock.release()


def balance(c:Counter, count=100):
    for _ in range(count):
        for i in range(-50, 50):
         if i < 0:
             c.dec()
         else:
             c.inc()


c = Counter()
c1 = 10 # 线程数
c2 = 1000
for i in range(c1):
    Thread(target=balance, args=(c, c2)).start()
'''
 print(c.value) 这个不适合的，因为在线程没有执行完成 就读取数值，都是起头并进的
 所以可能是线程没有完成时 ，就读取，
'''
'''
for i in range(c1):
    t = Thread(target=balance, args=(c, c2))
    t.start()
    t.join() # 不好，不是并行进行
'''
'''

'''
while True:
    time.sleep(1)
    if threading.active_count() == 1:
        print(threading.enumerate())
        print(c.value)
        break
    else:
        print(threading.enumerate())

```

## ** 非阻塞锁使用**
```python
import threading
import logging
import time


FORMAT = '%(asctime)s %(threadName)s %(thread)-10d %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
lock = threading.Lock()


def worker(l:threading.Lock):
    while True:
        flag = l.acquire(False)
        if flag:
            logging.info('do something.') # 为了显示效果,没有释放锁
        else:
            logging.info('try again')
            time.sleep(1)


for i in range(5):
    threading.Thread(target=worker, name='worker={}'.format(i), args=(lock, )).start()


```
#  **可重入锁RLock 递归锁**

- 可重入锁,是线程相关的锁。
- 线程A获得可重复锁,并可以多次成功获取,不会阻塞。最后要在线程A中做和acquire次数相同的release。

- 与线程相关,可在一个线程中获取锁,并可继续在同一线程中不阻塞多次获取锁
- 当锁未释放完,其它线程获取锁就会阻塞,直到当前持有锁的线程释放完锁
- 锁都应该使用完后释放。可重入锁也是锁,应该acquire多少次,就release多少次

```python
import logging
import threading
import time

FORMAT = '%(asctime)s %(threadName)s %s(thread) %(message)s'
logging.basicConfig(format="", level=logging.INFO)
lock = threading.RLock()


print(lock.acquire())
print(lock.acquire(False))
print(lock.acquire(timeout=4))
print(lock.acquire())
lock.release()
lock.release()
lock.release()

def sub(l:threading.RLock):
    print('enter==============================')
    print(l)
    print(threading.main_thread())
    print(l.acquire())
    print('exit============================' )

threading.Thread(target=sub,args=(lock,)).start()
print('end=============')

```


# **Condition**
| 参数名称                 |                             含义                              |
|:------------------------ |:-------------------------------------------------------------:|
| acquire(*args)           |                            获取锁                             |
| wait(self, timeout=None) |                          等待或超时                           |
| notify(n=1)              | 唤醒至多指定数目个数的等待的线程,没有等待的线程就没有任何操作 |
| notify_all()                         |                     唤醒所有等待的线程                                          |


```python
from threading import Event, Thread, Condition
import logging
import random
FORMAT = '%(asctime)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
# 此例只是为了演示,不考虑线程安全问题


class Dispachter:
    def __init__(self):
        self.data = None
        self.event = Event() # event只是为了使用方便,与逻辑无关
        self.cond = Condition()

    def produce(self, total=100):
        for _ in range(total):
            self.event.wait(1)
            with self.cond:
                data = random.randint(1, 100)
                logging.info(data)
                self.data = data
                self.cond.notify(5)
                #self.event.wait(1) # 模拟生产数据需要耗时1秒

    def consume(self):
        #while not self.event.is_set():
        while True:
            with self.cond:
                self.cond.wait()
                data = self.data
                logging.info('recieved {}'.format(data))
                self.data = None
                #self.event.wait(0.5) # 模拟消费速度,消费速度快


d = Dispachter()
p = Thread(target=d.produce, name='producer')
for i in range(10):
    c = Thread(target=d.consume, name='consumer')
    c.start()
p.start()

'''
Condition总结
Condition用于生产者消费者模型中,解决生产者消费者速度匹配的问题。
采用了通知机制,非常有效率。
使用方式
使用Condition,必须先acquire,用完了要release,因为内部使用了锁,默认使用RLock锁,最好的方式是使用
with上下文。
消费者wait,等待通知。
生产者生产好消息,对消费者发通知,可以使用notify或者notify_all方法。
'''
```

# **semaphore 信号量**

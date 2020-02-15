## **<font color=Red> 高并发解决方案**

- 并发
- 基本概念
- 并发和并行区别
 - 并行,parallel 同时做某些事,可以互不干扰的同一个时刻做几件事
 - 并发,concurrency也是同时做某些事,但是强调,一个时段内有事情要处理。
- 举例
  - 高速公路的车道,双向4车道,所有车辆(数据)可以互不干扰的在自己的车道上奔跑(传输)。
在同一个时刻,每条车道上可能同时有车辆在跑,是同时发生的概念,这是并行。
在一段时间内,有这么多车要通过,这是并发。
并发的解决


1. 队列　缓冲区
2. 争抢
3. 预处理
4. 并行
5. 提速
6. 消息中间件





```

“食堂打饭模型”
中午12点,开饭啦,大家都涌向食堂,这就是并发。如果人很多,就是高并发。
1、队列、缓冲区
假设只有一个窗口,陆续涌入食堂的人,排队打菜是比较好的方式。
所以,排队(队列)是一种天然解决并发的办法。
排队就是把人排成 队列,先进先出,解决了资源使用的问题。
排成的队列,其实就是一个缓冲地带,就是 缓冲区。
假设女生优先,每次都从这个队伍中优先选出女生出来先打饭,这就是 优先队列。
例如queue模块的类Queue、LifoQueue、PriorityQueue(小顶堆实现)。
2、争抢
只开一个窗口,有可能没有秩序,也就是谁挤进去就给谁打饭。
挤到窗口的人占据窗口,直到打到饭菜离开。
其他人继续争抢,会有一个人占据着窗口,可以视为锁定窗口,窗口就不能为其他人提供服务了。这是一种 锁机
制。
谁抢到资源就上锁,排他性的锁,其他人只能等候。
争抢也是一种高并发解决方案,但是,这样可能不好,因为有可能有人很长时间抢不到
3、预处理
如果排长队的原因,是由于每个人打菜等候时间长,因为要吃的菜没有,需要现做,没打着饭不走开,锁定着窗
口。
食堂可以提前统计大多数人最爱吃的菜品,将最爱吃的80%的热门菜,提前做好,保证供应,20%的冷门菜,现
做。这样大多数人,就算锁定窗口,也很快打到饭菜走了,快速释放窗口。
一种提前加载用户需要的数据的思路,预处理 思想,缓存常用。
4、并行
成百上千人同时来吃饭,一个队伍搞不定的,多开打饭窗口形成多个队列,如同开多个车道一样,并行打菜。
开窗口就得扩大食堂,得多雇人在每一个窗口提供服务,造成 成本上升。
日常可以通过购买更多服务器,或多开进程、线程实现并行处理,来解决并发问题。
注意这些都是 水平扩展 思想。
注:
如果线程在单CPU上处理,就不是真并行了。
但是多数服务器都是多CPU的,服务的部署往往是多机的、分布式的,这都是并行处理。
5、提速
提高单个窗口的打饭速度,也是解决并发的方式。
打饭人员提高工作技能,或为单个窗口配备更多的服务人员,都是提速的办法。
提高单个CPU性能,或单个服务器安装更多的CPU。
这是一种 垂直扩展 思想。
6、消息中间件
上地、西二旗地铁 站外 的九曲回肠的走廊,缓冲人流,进去之后再多口安检进站。
常见的消息中间件有RabbitMQ、ActiveMQ(Apache)、RocketMQ(阿里Apache)、kafka(Apache)等。
当然还有其他手段解决并发问题,但是已经列举除了最常用的解决方案,一般来说不同的并发场景用不同的策略,
而策略可能是多种方式的优化组合。
例如多开食堂(多地),也可以把食堂建设到宿舍生活区(就近),所以说,技术来源于生活。
```



## **<font color=Red> 进程和线程**

在实现了线程的操作系统中,线程是操作系统能够进行运算调度的最小单位。它被包含在进程之中,是进程中的实
际运作单位。一个程序的执行实例就是一个进程。
1. 进程(Process)是计算机中的程序关于某数据集合上的一次运行活动,是系统进行资源分配和调度的基本单位,
是操作系统结构的基础。
2. 进程和程序的关系
程序是源代码编译后的文件,而这些文件存放在磁盘上。当程序被操作系统加载到内存中,就是进程,进程中存放
着指令和数据(资源),它也是线程的容器。
Linux进程有父进程、子进程,Windows的进程是平等关系。
3. 线程,有时被称为轻量级进程(Lightweight Process,LWP),是程序执行流的最小单元。
一个标准的线程由线程ID,当前指令指针(PC)、寄存器集合和堆栈组成。
在许多系统中,创建一个线程比创建一个进程快10-100倍


进程、线程的理解
现代操作系统提出进程的概念,每一个进程都认为自己独占所有的计算机硬件资源。
- **<font color=Red>进程就是独立的王国,进程间不可以随便的共享数据**
- **<font color=Red>线程就是省份,同一个进程内的线程可以共享进程的资源,每一个线程拥有自己独立的堆栈**


# **<font color=Red> 线程**

```
# 签名
def __init__(self, group=None, target=None, name=None,
args=(), kwargs=None, *, daemon=None
```



| 状态            |     含义|
| :------------ |:---------------:|
| 就绪(Ready)     | 线程能够运行,但在等待被调度。可能线程刚刚创建启动,或刚刚从阻塞中恢复,或者被其他线程抢占 |
|运行(Running)    | 线程正在运行      |
| 阻塞(Blocked)| 线程等待外部事件发生而无法运行,如I/O操作     |
| 终止(Terminated| 线程完成,或退出,或被取消      |

### **<font color=Red> 线程结束方式，要么的死循环　要么线程出现异常　**


| 状态            |     含义|
| :------------ |:---------------:|
| target     | 线程调用的对象,就是目标函数 |
|name  | 线为线程起个名字      |
| args| 为目标函数传递实参,元组     |
| kwargs| 为目标函数关键字传参,字典      |


### **<font color=Red> 线程结束方式，要么的死循环　要么线程出现异常　**

- 通过threading.Thread创建一个线程对象,target是目标函数,可以使用name为线程指定名称。
但是线程没有启动,需要调用start方法。
- 线程之所以执行函数,是因为线程中就是要执行代码的,而最简单的封装就是函数,所以还是函数调用。
函数执行完,线程也就退出了。


- 那么,如果不让线程退出,或者让线程一直工作怎么办呢?

- 线程退出
Python没有提供线程退出的方法,线程在下面情况时退出
1、线程函数内语句执行完毕
2、线程函数中抛出未处理的异常


### **<font color=Red> threading的属性和方法**

- **<font color=Red>线程程只能运行一次**

| 状态            |     含义|
| :------------ |:---------------:|
| current_thread()    | 返回当前线程对象 |
|main_thread()    | 返回主线程对象      |
| active_count()  | 当前处于alive状态的线程个数                   |
| enumerate()     | 返回所有活着的线程的列表,不包括已经终止的线程和未开始的线程 |
| 终止(Terminated | 线程完成,或退出,或被取消                                    |

```python
    print(3,threading.enumerate(),threading.active_count())
    print()

def worker(n,m):
    showprocess()
    for i in range(n):
        time.sleep(m)
        print("I'm working")
    print('Fineshed')


t = threading.Thread(target=worker, name='worker',args=(5,),kwargs={'m':1}) # 创建线程对象
t.start() #启动

showprocess()
print("end========================================")
#线程结束方式，要么的死循环　要么线程出现异常　
```

## **<font color=Red> threading的start run 区别**
- start方法
 - 创建线程　调用操作系统创建_start_new_thread

- run方法：
 - 仅仅运行target函数　且该函数没有返回值，不会启动新的线程

### **<font color=Red> start run 运行一次的原因**

- t.run() #AttributeError: _target

 - 因为删除属性：：del self._target, self._args, self._kwargs

```python
def run(self):
        """Method representing the thread's activity.

        You may override this method in a subclass. The standard run() method
        invokes the callable object passed to the object's constructor as the
        target argument, if any, with sequential and keyword arguments taken
        from the args and kwargs arguments, respectively.

        """
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs

```

- t.start() #self._started = Event()
 - self._started = Event()

# **<font color=Red>多线程和线程安全**


```python
import threading
import time


def worker():
    t = threading.current_thread()
    for i in range(5):
        time.sleep(1)
        print('i am working', t.name, t.ident)
    print('finished')


class MyThread(threading.Thread):

    def start(self):
        print('start~~~~')
        super().start()

    def run(self):
        print('run~~~~~~')
        super().run()


t1 = MyThread(target=worker, name='worker1')
t2 = MyThread(target=worker, name='worker2')
t1.start()
t2.start()
# t1.run()
# t2.run()
worker()
worker()

'''
t1.run()
t2.run()
使用ｒｕｎ方法：
没有开新的线程,这就是普通函数调用,所以执行完t1.run(),然后执行t2.run(),这里就不是多线程。

/home/joey/python/code/venv/bin/python /home/joey/python/code/t7.py
run~~~~~~
i am working MainThread 140519771748160
i am working MainThread 140519771748160
i am working MainThread 140519771748160
i am working MainThread 140519771748160
i am working MainThread 140519771748160
finished
run~~~~~~
i am working MainThread 140519771748160
i am working MainThread 140519771748160
i am working MainThread 140519771748160
i am working MainThread 140519771748160
i am working MainThread 140519771748160
finished

t1.start()
t2.start()
当使用start方法启动线程后,进程内有多个活动的线程并行的工作,就是多线程。
一个进程中至少有一个线程,并作为程序的入口,这个线程就是主线程。
一个进程至少有一个主线程。
其他线程称为工作线程。
/home/joey/python/code/venv/bin/python /home/joey/python/code/t7.py
start~~~~
run~~~~~~
start~~~~
run~~~~~~
i am working worker1 139709635487488
i am working worker2 139709627094784
i am working worker1 139709635487488
i am working worker2 139709627094784
i am working worker1 139709635487488
i am working worker2 139709627094784
i am working worker1 139709635487488
i am working worker2 139709627094784
i am working worker1 139709635487488
finished
i am working worker2 139709627094784
finished

Process finished with exit code 0



'''



```

## **<font color=Red>线程安全**
- 线程执行一段代码,不会产生不确定的结果,那这段代码就是线程安全的


- print函数被打断了,被线程切换打断了。print函数分两步,第一步打印字符串,第二步打印换行符,就在
这之间,发生了线程的切换。
这说明print函数是线程不安全的。
- 2、使用logging
标准库里面的logging模块,日志处理模块,线程安全的,生成环境代码都使用logging



# **<font color=Red> daemon线程和non-daemon线程**

- Python中,构造线程的时候,可以设置daemon属性,这个属性必须在start方法前设置好。
- 线程daemon属性,如果设定就是用户的设置,否则就取当前线程的daemon值。
- 主线程是non-daemon线程,即daemon = False。

```python
# 源码Thread的__init__方法中
if daemon is not None:
  self._daemonic = daemon # 用户设定bool值
else:
  self._daemonic = current_thread().daemon


import threading
import time
import logging
fmtstr = "%(asctime)s %(thread)s %(threadName)s %(message)s "
logging.basicConfig(level=logging.INFO,format=fmtstr)

def worker(name,timeout):
    time.sleep(timeout)
    logging.info('i am working {} {}'.format(threading.current_thread().name, threading.current_thread().isDaemon()))

for x in range(3):
    t1 = threading.Thread(target=worker, args=('t1',4),name='worker1',daemon=False)
    t1.start()
t2 = threading.Thread(target=worker, args=('t1',2),name='worker2',daemon=True)
t2.start()

print("--end----")



```
- 总结
- 线程具有一个daemon属性,可以手动设置为True或False,也可以不设置,则取默认值None。
如果不设置daemon,就取当前线程的daemon来设置它。
- 主线程是non-daemon线程,即daemon = False。
从主线程创建的所有线程的不设置daemon属性,则默认都是daemon = False,也就是non-daemon线程。
Python程序在没有活着的non-daemon线程运行时,程序退出,也就是除主线程之外剩下的只能都是daemon线
程,主线程才能退出,否则主线程就只能等待。

### **<font color=Red> daemon应用场景**
简单来说就是,本来并没有 daemon thread,为了简化程序员的工作,让他们不用去记录和管理那些后台线程,
创造了一个 daemon thread 的概念。这个概念唯一的作用就是,当你把一个线程设置为 daemon,它可以会随主
线程的退出而退出。
- 主要应用场景有:
- 1、后台任务。如发送心跳包、监控,这种场景最多。
- 2、主线程工作才有用的线程。如主线程中维护这公共的资源,主线程已经清理了,准备退出,而工作线程使用这
些资源工作也没有意义了,一起退出最合适。
- 3、随时可以被终止的线程
- 如果主线程退出,想所有其它工作线程一起退出,就使用daemon=True来创建工作线程。
比如,开启一个线程定时判断WEB服务是否正常工作,主线程退出,工作线程也没有必须存在了,应该随着主线程
退出一起退出。这种daemon线程一旦创建,就可以忘记它了,只用关心主线程什么时候退出就行了。
daemon线程,简化了程序员手动关闭线程的工作。

- 如果在non-daemon线程A中,对另一个daemon线程B使用了join方法,这个线程B设置成daemon就没有什么意
义了,因为non-daemon线程A总是要等待B。
如果在一个daemon线程C中,对另一个daemon线程D使用了join方法,只能说明C要等待D,主线程退出,C和D
不管是否结束,也不管它们谁等谁,都要被杀掉。








# **<font color=Red> join**
　　
- join(timeout=None),是线程的标准方法之一。
- 一个线程中调用另一个线程的join方法,**<font color=Red>调用者将被阻塞,直到被调用线程终止。**
- 一个线程可以被join多次。
- timeout参数指定调用者等待多久,没有设置超时,就一直等到被调用线程结束。
**<font color=Red>调用谁的join方法,就是join谁,就要等谁**


```python
import threading
import time
import logging
fmtstr = "%(asctime)s %(thread)s %(threadName)s %(message)s "
logging.basicConfig(level=logging.INFO,format=fmtstr)

def worker(name,timeout):
    time.sleep(timeout)
    logging.info('i am working {} {}'.format(threading.current_thread().name, threading.current_thread().isDaemon()))
#
# for x in range(3):
#     t1 = threading.Thread(target=worker, args=('t1',4),name='worker1',daemon=False)
#     t1.start()
t2 = threading.Thread(target=worker, args=('t1',2),name='worker2',daemon=True)
t2.start()
t2.join()
print("--end----")
```


# **<font color=Red> threading.local类**


```python

'''
   多线程中　用到全局变量　要特别的小心的用
'''
import threading
import time
import logging
fmtstr = "%(asctime)s %(thread)s %(threadName)s %(message)s "
logging.basicConfig(level=logging.INFO,format=fmtstr)
x = 0　#全局部变量
def worker():
    global x
    for i in range(100):
        time.sleep(0.001)
        x += 1
        #logging.info('i am working {} {}'.format(threading.current_thread().name, threading.current_thread().isDaemon()))
    print(threading.current_thread().name,x)


for i in range(10):
    threading.Thread(target=worker ,name='worker-{}'.format((i+1))).start()




'''
   多线程中　局部都是安全，
'''
import threading
import time
import logging
fmtstr = "%(asctime)s %(thread)s %(threadName)s %(message)s "
logging.basicConfig(level=logging.INFO,format=fmtstr)

def worker():
    x = 0　#局部变量
    for i in range(100):
        time.sleep(0.001)
        x += 1
        #logging.info('i am working {} {}'.format(threading.current_thread().name, threading.current_thread().isDaemon()))
    print(threading.current_thread().name,x)


for i in range(10):
    threading.Thread(target=worker ,name='worker-{}'.format((i+1))).start()





import threading
import time
import logging
fmtstr = "%(asctime)s %(thread)s %(threadName)s %(message)s "
logging.basicConfig(level=logging.INFO,format=fmtstr)
# class A:pass
# global_data = A()

global_data = threading.local()　#为每一个线程创建一个

def worker():
    global_data.x = 0
    for i in range(100):
        time.sleep(0.001)
        global_data.x += 1
        #logging.info('i am working {} {}'.format(threading.current_thread().name, threading.current_thread().isDaemon()))
    print(threading.current_thread().name,global_data.x)


for i in range(10):
    threading.Thread(target=worker ,name='worker-{}'.format((i+1))).start()


```

# **<font color=Red> 线程同步()**
- 概念
 - **<font color=Red>线程同步,线程间协同,通过某种技术,让一个线程访问某些数据时,其他线程不能访问这些数据,直到该线程完
成对数据的操作。**

## **<font color=Red> Event()**
- Event事件,是线程间通信机制中最简单的实现,使用一个内部的标记flag,通过flag的True或False的变化来进行
操作

| 状态            |     含义|
| :------------ |:---------------:|
| set()  | 标记设置为True|
|clear()   | 标记设置为False     |
| is_set()  | 标记是否为True               |
| wait(timeout=None)     | 设置等待标记为True的时长,None为无限等待。等到返回True,未等到超时了返回False |


```python
from threading import Event, Thread
import logging
import time
FORMAT = '%(asctime)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

event = Event() #初始值为fasle

def boss(event:Event,timeout=10):
    logging.info("I'm boss, waiting for U")
    # 阻塞等待
    event.wait()
    logging.info('Good Job.')

def worker(event:Event, count=10):
    logging.info('I am working for U')
    cups = []
    while True:
        logging.info('make 1 cup')
        time.sleep(0.5)
        cups.append(1)
        if len(cups) >= count:
            event.set()# block status

b = Thread(target=boss, name='boss', args=(event,))
w = Thread(target=worker, name='worker', args=(event,))
b.start()
w.start()





import threading
import time
import logging
fmtstr = "%(asctime)s %(thread)s %(threadName)s %(message)s "
logging.basicConfig(level=logging.INFO,format=fmtstr)
# class A:pass
# global_data = A()

global_data = threading.local()
e = threading.Event()
def worker(e:threading.Event,timeout=10):
    while not e.wait(timeout):#没隔一秒执行一次
        print("wait--------")
    print('game over~~~~~')


t= threading.Thread(target=worker ,name='worker-{}',args=(e,1))
t.start()

print("end---------------")






````
## **<font color=Red>定时器 Timer/延迟执行**

```python
import threading
import time
import logging
fmtstr = "%(asctime)s %(thread)s %(threadName)s %(message)s "
logging.basicConfig(level=logging.INFO,format=fmtstr)
# class A:pass
# global_data = A()

# global_data = threading.local()
# e = threading.Event()
def worker():
    print('game over~~~~~')


t= threading.Timer(8,worker)
t.setDaemon(False)
t.start()
t.cancel()

print("end---------------")

'''
threading.Timer继承自Thread,这个类用来定义延迟多久后执行一个函数。
class threading.Timer(interval, function, args=None, kwargs=None)
start方法执行之后,Timer对象会处于等待状态,等待了interval秒之后,开始执行function函数的。



Timer是线程Thread的子类,Timer实例内部提供了一个finished属性,该属性是Event对象。cancel方法,本质上
是在worker函数执行前对finished属性set方法操作,从而跳过了worker函数执行,达到了取消的效果。
总结
Timer是线程Thread的子类,就是线程类,具有线程的能力和特征。
它的实例是能够延时执行目标函数的线程,在真正执行目标函数之前,都可以cancel它。
cancel方法本质使用Event类实现。这并不是说,线程提供了取消的方法。

'''
```


## **<font color=Red>Lock**
- Lock
- 锁,一旦线程获得锁,其它试图获取锁的线程将被阻塞
- 锁:凡是存在共享资源争抢的地方都可以使用锁,从而保证只有一个使用者可以完全使用这个资源。


| 状态            |     含义|
| :------------ |:---------------:|
| acquire(blocking=True timeout=-1) | 默认阻塞,阻塞可以设置超时时间。非阻塞时,timeout禁止设置 成功获取锁,返回True,否则返回False|
|release()   | 释放锁。可以从任何线程调用释放。 已上锁的锁,会被重置为unlocked未上锁的锁上调用, 抛RuntimeError异常。   |


```python
import  logging
import threading

FORMAT = '%(asctime)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


event = threading.Event()
lock = threading.Lock() # 互斥 mutex

print(lock.acquire())
print(lock.acquire(timeout=5))
print(lock.acquire(False))
print('-' * 30)


def worker(l:threading.Lock):
    print("enter~~~~~~~~~~~")
    l.acquire()
    print("exit~~~~~~~~~~~")

for i in range(5):
    threading.Thread(target=worker,args=(lock,)).start()

print("------------------------")
event.wait(2)

while True:
    cmd = input(">>>>>>>>>>>>>>")
    if cmd == "quit":
        break
    elif cmd == 'r':
        lock.release()
    else:
        print(threading.enumerate())
-------------
import threading
import logging
import time


fmtstr = "%(asctime)s %(thread)s %(threadName)s %(message)s"
logging.basicConfig(level=logging.INFO,format=fmtstr)
lock = threading.Lock()

cups = []


def worker(l:threading.Lock, count=100):
    logging.info('{} is wording'.format(threading.current_thread().name))
    flag = False
    while True:
        time.sleep(0.01)
        l.acquire()
        if len(cups) >= count:
            flag = True
        #l.release() #wrong
        if not flag:
            cups.append(1)
        l.release()
        if flag:
            break
    logging.info("{} finished my job.cups={}".format(threading.current_thread().name, len(cups)))


for i in range(10):
    t = threading.Thread(target=worker, name='work={}'.format(i+1),args=(lock, 100))
    t.start()



```

```python
import threading
from threading import Thread, Lock
import time
class Counter:
    def __init__(self):
        self._val = 0
        self.__lock = Lock()
    @property
    def value(self):
        with self.__lock:
            return self._val
    def inc(self):
        try:
            self.__lock.acquire()
            self._val += 1
        finally:
            self.__lock.release()
    def dec(self):
        with self.__lock:
            self._val -= 1
def run(c:Counter, count=100):
        for _ in range(count):
            for i in range(-50,50):
                if i < 0:
                    c.dec()
                else:
                    c.inc()
c = Counter()
c1 = 10 # 线程数
c2 = 1000
# for i in range(c1):
#     Thread(target=run, args=(c, c2)).start()
# print(c.value) # 这一句合适吗?  在线程还没有计算完成后，就直接去值

theard_list = []
for i in range(11):
    t = threading.Thread(target=run, args=(c, c2))
    t.start()
    theard_list.append(t)
    #t.join()

for t in theard_list:
    t.join()
print(c.value,"~~~~~~~~~~~~~~~~~~~~~~~~~~`")

```

## **<font color=Red>可重入锁RLock Rcusive**



## **<font color=Red>Condition**


## **<font color=Red>Csemaphore 信号量**

- 应用举例连接池
因为资源有限,且开启一个连接成本高,所以,使用连接池。

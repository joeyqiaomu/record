
# **<font color=Red> 数据结构和GIL**

# **<font color=Red> GIL全局解释器锁**

- CPython 在解释器进程级别有一把锁,叫做GIL,即全局解释器锁。
- **<font color=Red>GIL 保证CPythonY一个进程中,只有一个线程执行字节码。甚至是在多核CPU的情况下,也只允许同时只能有一个CPU
上运行该进程的一个线程**

```
CPython中
IO密集型,某个线程阻塞,就会调度其他就绪线程;
CPU密集型,当前线程可能会连续的获得GIL,导致其它线程几乎无法使用CPU。
在CPython中由于有GIL存在,IO密集型,使用多线程较为合算;CPU密集型,使用多进程,要绕开GIL。
新版CPython正在努力优化GIL的问题,但不是移除。
如果在意多线程的效率问题,请绕行,选择其它语言erlang、Go等
```
```python

'''
CPU密集型,当前线程可能会连续的获得GIL,导致其它线程几乎无法使用CPU
'''
import threading
import logging
import datetime
logging.basicConfig(level=logging.INFO, format="%(thread)s %(message)s")
start = datetime.datetime.now()
# 计算
def calc():
  sum = 0
    for _ in range(1000000000): # 10亿
    sum += 1
t1 = threading.Thread(target=calc)
t2 = threading.Thread(target=calc)
t3 = threading.Thread(target=calc)
t4 = threading.Thread(target=calc)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
delta = (datetime.datetime.now() - start).total_seconds()
logging.info(delta)

----------------------------------------------------------------------
# 计算
def calc():
  sum = 0
    for _ in range(1000000000): # 10亿
    sum += 1
calc()
calc()
calc()
calc()
delta = (datetime.datetime.now() - start).total_seconds()
logging.info(delta)

```


# **<font color=Red> 多进程**


- 注意:多进程代码一定要放在 __name__ == "__main__" 下面执行。
- multiprocessing还提供共享内存、服务器进程来共享数据,还提供了用于进程间通讯的Queue队列、Pipe管道


| 参数名称                 |                             含义                              |
|:------------------------ |:-------------------------------------------------------------:|
| pid          |                      进程id                            |
| wait(self, timeout=None) |                 进程的退出状态码                |
|terminate()           | 终止指定的进程 |



- 多进程就是启动多个解释器进程,进程间通信必须序列化、反序列化

- 数据的线程安全性问题 如果每个进程中没有实现多线程,GIL可以说没什么用了


```python

'''
计算密集行--多进程
io密集行 ---一个进程

多线程
'''
import multiprocessing
import datetime
import logging
from multiprocessing import Event, Lock,Semaphore,Queue
#进程之间通信用到的锁，信号量


FORMAT = '%(asctime)s %(process)s %(processName)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc(i):
    sum = 0
    for _ in range(1000000000): # 10亿
        sum += 1
    return i, sum

if __name__ == '__main__':
    start = datetime.datetime.now() # 注意一定要有这一句
    ps = []
    for i in range(4):
        p = multiprocessing.Process(target=calc, args=(i,), name='calc-{}'.format(i))
        ps.append(p)
        p.start()
    for p in ps:
        p.join()
        print(p.name, p.exitcode)

    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)
    print('===end====')
```
## **进程池**
| 参数名称                 |                             含义                              |
|:------------------------ |:-------------------------------------------------------------:|
| apply(self, func, args=(), kwds={})         |                  阻塞执行,导致主进程执行其他子进程就像一个个执行                           |
| apply_async(self, func, args=(), kwds={}  callback=None, error_callback=None)|                 与apply方法用法一致,非阻塞异步执行,得到结果后会执行回调               |
|close()           | 关闭池,池不能再接受新的任务,所有任务完成后退出进程 |
|terminate()           | 立即结束工作进程,不再处理未处理的任务 |
|join()           | 主进程阻塞等待子进程的退出, join方法要在close或terminate之后使用|




### **<font color=Red> pool.apply(calc, (i,)) #同步 阻塞的方法**
```python
import multiprocessing
import threading
import datetime
import logging
from multiprocessing import Event,Lock,Semaphore

FORMAT = '%(asctime)s %(process)s %(processName)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc(i):
    sum = 0
    for _ in range(1000000000): # 10亿
        sum += 1
    ret = i, sum
    logging.info(ret)
    return ret

if __name__ == '__main__':
    start = datetime.datetime.now() # 注意一定要有这一句
    #ps = []
    pool = multiprocessing.Pool(4)
    for i in range(4):
        #p = multiprocessing.Process(target=calc, args=(i,), name='calc-{}'.format(i))
        r = pool.apply(calc, (i,)) #同步 阻塞的方法
        logging.info(r)
    logging.info("+++++++++++++++++++++++++++++++++")
    pool.close()
    pool.join()

    # for p in ps:
    #     p.join()
    #     logging.info("{} {}".format(p.name, p.exitcode))

    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)

    print(threading.enumerate())
    print('===end====')

```


### **<font color=Red> r = pool.apply_async(calc, (i,)) #异步 非阻塞的方法**
- 异步 打饭的时候，仅仅哪一个牌子


```python
import multiprocessing
import threading
import datetime
import logging
from multiprocessing import Event,Lock,Semaphore

FORMAT = '%(asctime)s %(process)s %(processName)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc(i):
    sum = 0
    for _ in range(1000000000): # 10亿
        sum += 1
    ret = i, sum
    logging.info(ret)
    return ret

if __name__ == '__main__':
    start = datetime.datetime.now() # 注意一定要有这一句
    pool = multiprocessing.Pool(4)
    for i in range(4):
        r = pool.apply_async(calc, (i,)) #异步 阻塞的方法
        logging.info(r)
        logging.info("×××××××××××××××××××××××××××××8")

    logging.info("+++++++++++++++++++++++++++++++++")
    pool.close()
    logging.info("==============================")
    pool.join()
    logging.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)

    print(threading.enumerate())
    print('===end====')

’‘’
/home/joey/python/code/venv/bin/python /home/joey/python/code/t5.py
2020-02-04 00:14:15,870 25624 MainProcess MainThread 140062857996096 <multiprocessing.pool.ApplyResult object at 0x7f62e9ca1470>
2020-02-04 00:14:15,871 25624 MainProcess MainThread 140062857996096 ×××××××××××××××××××××××××××××8
2020-02-04 00:14:15,871 25624 MainProcess MainThread 140062857996096 <multiprocessing.pool.ApplyResult object at 0x7f62e9ca1588>
2020-02-04 00:14:15,871 25624 MainProcess MainThread 140062857996096 ×××××××××××××××××××××××××××××8
2020-02-04 00:14:15,871 25624 MainProcess MainThread 140062857996096 <multiprocessing.pool.ApplyResult object at 0x7f62e9ca1668>
2020-02-04 00:14:15,871 25624 MainProcess MainThread 140062857996096 ×××××××××××××××××××××××××××××8
2020-02-04 00:14:15,871 25624 MainProcess MainThread 140062857996096 <multiprocessing.pool.ApplyResult object at 0x7f62e9ca1748>
2020-02-04 00:14:15,871 25624 MainProcess MainThread 140062857996096 ×××××××××××××××××××××××××××××8
2020-02-04 00:14:15,871 25624 MainProcess MainThread 140062857996096 +++++++++++++++++++++++++++++++++
2020-02-04 00:14:15,871 25624 MainProcess MainThread 140062857996096 ==============================
2020-02-04 00:15:16,557 25626 ForkPoolWorker-2 MainThread 140062857996096 (1, 1000000000)
2020-02-04 00:15:18,442 25625 ForkPoolWorker-1 MainThread 140062857996096 (0, 1000000000)
2020-02-04 00:15:18,843 25627 ForkPoolWorker-3 MainThread 140062857996096 (3, 1000000000)
2020-02-04 00:15:19,122 25628 ForkPoolWorker-4 MainThread 140062857996096 (2, 1000000000)
63.332732
[<_MainThread(MainThread, started 140062857996096)>]
===end====
2020-02-04 00:15:19,188 25624 MainProcess MainThread 140062857996096 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Process finished with exit code 0

‘‘’
```
### **<font color=Red>callback**
```python

import multiprocessing
import datetime
import logging
import threading
from multiprocessing import Event, Lock,Semaphore,Queue
#进程之间通信用到的锁，信号量


FORMAT = '%(asctime)s %(process)s %(processName)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc(i):
    sum = 0
    for _ in range(1000000000): # 10亿
        sum += 1
    logging.info('i={} sum{}'.format(i,sum))
    return i, sum

if __name__ == '__main__':
    start = datetime.datetime.now() # 注意一定要有这一句
    pool = multiprocessing.Pool(4)
    for i in range(4):
        print(1,threading.enumerate())
        r = pool.apply_async(calc, (i,),callback=lambda x:logging.info('{}.in main~~~~~~~~~'.format(x)))
        logging.info(r)
        print("++++++++++++++++++++++++++++++++++")
    print("++++++========================++++++++++")
    pool.close()
    print("*************************************")
    pool.join()
    print("*********+++++++++++++++++++*****************")
    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)
    print(2,threading.enumerate())
    print('===end====')


    /home/joey/python/code/venv/bin/python /home/joey/python/code/t5.py
2020-02-04 12:13:08,324 5263 MainProcess MainThread 140689459234624 <multiprocessing.pool.ApplyResult object at 0x7ff4ce2235c0>
2020-02-04 12:13:08,338 5263 MainProcess MainThread 140689459234624 ************************************
2020-02-04 12:13:08,338 5263 MainProcess MainThread 140689459234624 <multiprocessing.pool.ApplyResult object at 0x7ff4ce2236a0>
2020-02-04 12:13:08,338 5263 MainProcess MainThread 140689459234624 ************************************
2020-02-04 12:13:08,338 5263 MainProcess MainThread 140689459234624 <multiprocessing.pool.ApplyResult object at 0x7ff4ce2237f0>
2020-02-04 12:13:08,339 5263 MainProcess MainThread 140689459234624 ************************************
2020-02-04 12:13:08,339 5263 MainProcess MainThread 140689459234624 <multiprocessing.pool.ApplyResult object at 0x7ff4ce223860>
2020-02-04 12:13:08,339 5263 MainProcess MainThread 140689459234624 ************************************
2020-02-04 12:13:08,339 5263 MainProcess MainThread 140689459234624 +++++++++++++++++++++++++++++++++
2020-02-04 12:13:08,342 5263 MainProcess MainThread 140689459234624 ==============================
2020-02-04 12:13:08,865 5267 ForkPoolWorker-4 MainThread 140689459234624 (1, 10000000)
2020-02-04 12:13:08,869 5263 MainProcess Thread-3 140689390307072 (1, 10000000) in main~~
2020-02-04 12:13:08,876 5264 ForkPoolWorker-1 MainThread 140689459234624 (2, 10000000)
2020-02-04 12:13:09,030 5266 ForkPoolWorker-3 MainThread 140689459234624 (3, 10000000)
2020-02-04 12:13:09,030 5265 ForkPoolWorker-2 MainThread 140689459234624 (0, 10000000)
2020-02-04 12:13:09,206 5263 MainProcess Thread-3 140689390307072 (3, 10000000) in main~~
2020-02-04 12:13:09,207 5263 MainProcess Thread-3 140689390307072 (0, 10000000) in main~~
2020-02-04 12:13:09,208 5263 MainProcess Thread-3 140689390307072 (2, 10000000) in main~~
2020-02-04 12:13:09,295 5263 MainProcess MainThread 140689459234624 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1.065048
[<_MainThread(MainThread, started 140689459234624)>]
```

```python
import multiprocessing
import threading
import datetime
import logging
from multiprocessing import Event,Lock,Semaphore

FORMAT = '%(asctime)s %(process)s %(processName)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc(i):
    sum = 0
    for _ in range(1000000000): # 10亿
        sum += 1
    ret = i, sum
    logging.info(ret)
    return ret


def sub(pool:multiprocessing.Pool,target,i):
    r = pool.apply(target,(i,))
    logging.info(r)

if __name__ == '__main__':
    start = datetime.datetime.now() # 注意一定要有这一句
    pool = multiprocessing.Pool(4)
    for i in range(4):
        t = threading.Thread(target=sub,args=(pool,calc,i),name='sub={}'.format(i))
        t.start()
        logging.info("************************************")

    logging.info("+++++++++++++++++++++++++++++++++")
    pool.close() #等着进程完成后
    #pool.terminate() #强制终止掉进程
    logging.info("==============================")
    pool.join() #等结果
    logging.info("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)

    print(threading.enumerate())
    print('===end====')



===end====

```

## **<font color=Red>多进程、多线程的选择**
- CPU密集型 CPython中使用到了GIL,多线程的时候锁相互竞争,且多核优势不能发挥,选用Python多进程效率更高。
- IO密集型在Python中适合是用多线程,可以减少多进程间IO的序列化开销。且在IO等待的时候,切换到其他线程继续执行,效率不错。
- 应用
请求/应答模型:WEB应用中常见的处理模型
master启动多个worker工作进程,一般和CPU数目相同。发挥多核优势。
worker工作进程中,往往需要操作网络IO和磁盘IO,启动多线程,提高并发处理能力。worker处理用户的请求,往往需要等待数据,处理完请求还要通过网络IO返回响应。
这就是nginx工作模式。

# **<font color=Red>Executor类子类对象。**

| 名称               |       含义          |
|:------------------ |:---------------------------------------------------------------------------:|
| ThreadPoolExecutor(max_workers=1)   |    池中至多创建max_workers个线程的池来同时异步执行,返回Executor实例                                  |
| submit(fn, *args, **kwargs)        |                        提交执行的函数及其参数,返回Future类的实例                              |
| shutdown(wait=True)        |            清理池                                         |


# **<font color=Red> Future类**






## **<font color=Red>线程池**


```python
from concurrent.futures import ThreadPoolExecutor
import threading
import  logging
import time
FORMAT = '%(asctime)s %(process)s %(processName)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def worker(n):
    logging.info('enter....')
    time.sleep(n)
    logging.info('finished ......................')


execcutor = ThreadPoolExecutor(max_workers=3)
for i in range(3):
    future = execcutor.submit(worker,5)
    logging.info(future)
for i in range(3):
    future = execcutor.submit(worker,5)
    logging.info(future)

logging.info('===============================')
execcutor.shutdown()
logging.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

while True:
    if threading.active_count() == 1:
        logging.info(threading.enumerate())
        logging.info(future)
        break
    time.sleep(1)

```
```python
from concurrent.futures import ThreadPoolExecutor
import threading
import  logging
import time
FORMAT = '%(asctime)s %(process)s %(processName)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def worker(n):
    logging.info('enter....')
    time.sleep(n)
    logging.info('finished ......................')
    return 1000+n


execcutor = ThreadPoolExecutor(max_workers=3)
fs = []
for i in range(3):
    future = execcutor.submit(worker,5)
    logging.info(future)
    fs.append(future)


logging.info('===============================')
execcutor.shutdown()
logging.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

while True:
    if threading.active_count() == 1:
        logging.info(threading.enumerate())
        logging.info(future)
        break
    time.sleep(1)

while True:
    flag = True
    for f in fs:
        print(f.done())
        flag = flag and f.done()

        if not flag:
            break
    time.sleep(1)
    print()

    if flag:
        execcutor.shutdown()
        logging.info(threading.enumerate())
        break

print("++++++++++++++++++++++++++++++++++++++++")

for f in fs:
    print(f.result())
```

## **<font color=Red>多进程池**

```python
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import threading
import  logging
import time
FORMAT = '%(asctime)s %(process)s %(processName)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def worker(n):
    logging.info('enter....')
    time.sleep(n)
    logging.info('finished ......................')
    return 1000+n

if __name__ == "__main__":
    execcutor = ProcessPoolExecutor(max_workers=3)
    fs = []
    for i in range(6):
        future = execcutor.submit(worker,i+2)
        logging.info(future)
        fs.append(future)


    logging.info('===============================')
    execcutor.shutdown()
    logging.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    while True:
        if threading.active_count() == 1:
            logging.info(threading.enumerate())
            logging.info(future)
            break
        time.sleep(1)

    while True:
        flag = True
        for f in fs:
            print(f.done())
            flag = flag and f.done()

            if not flag:
                break
        time.sleep(1)
        print()

        if flag:
            execcutor.shutdown()
            logging.info(threading.enumerate())
            break

    print("++++++++++++++++++++++++++++++++++++++++")

    for f in fs:
        print(f.result())
```



```python
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import threading
import  logging
import time
FORMAT = '%(asctime)s %(process)s %(processName)s %(threadName)s %(thread)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


def worker(n):
    logging.info('enter....')
    time.sleep(n)
    logging.info('finished ......................')
    return 1000+n

if __name__ == "__main__":
    #execcutor = ProcessPoolExecutor(max_workers=3)
    fs = []
    #with execcutor:
    with ProcessPoolExecutor(max_workers=3) as execcutor:
        for i in range(6):
            future = execcutor.submit(worker,i+2)
            logging.info(future)
            fs.append(future)

        logging.info('===============================')
        execcutor.shutdown()
        logging.info('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        while True:
            flag = True
            for f in fs:
                print(f.done())
                flag = flag and f.done()

                if not flag:
                    break
            time.sleep(1)
            print()

            if flag:
                #execcutor.shutdown()
                logging.info(threading.enumerate())
                break

    print("++++++++++++++++++++++++++++++++++++++++")

    for f in fs:
        print(f.result())
```

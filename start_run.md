
| 参数名称           |     含义|
| :------------ |:---------------:|
| start()     | 启动线程。每一个线程必须且只能执行该方法一次|
| run()       | 运行线程函数    |


```python

from threading import Thread
import time
import threading

'''
start() #  调用操作系统的系统调用来创建线程，启动操作系统线程
run() #    运行线程中的函数，仅仅运行的普通函数
'''


class MyThead(Thread):
    def start(self) -> None:
        print("start ~~~~~~~~~")
        super().start() #  调用操作系统的系统调用来创建线程，启动操作系统线程

    def run(self) -> None:
        print("run ~~~~~~~~~")
        super().run() #  运行线程函数
def worker():
    #time.sleep(2)
    print(threading.enumerate())
    print(threading.current_thread(),'~~~~~~~~~i am working')
    global t
    t = 100



t1 = MyThead(target=worker, name='worker100') # 线程对象
t1.start() #启动
#t.run()
print(t, "-------")
'''
t的打印结果：
    就看线程和主进程之间运行，因为起头并进的运行，就看线程和主进程之间那个前运行，就看操作系统的进程调度

    start ~~~~~~~~~
    run ~~~~~~~~~
    [<_MainThread(MainThread, started 140369454405440)>, <MyThead(worker100, started 140369422063360)>]
    <MyThead(worker100, started 140369422063360)> ~~~~~~~~~i am working
    100 -------


    Traceback (most recent call last):
    File "/home/joey/python/code/t2.py", line 27, in <module>
    print(t, "-------")
    NameError: name 't' is not defined
    start ~~~~~~~~~
    run ~~~~~~~~~
    [<_MainThread(MainThread, stopped 140367710197568)>, <MyThead(worker1
'''
#t.start() #启动
# t._target=worker
# t._args=()
# t._kwargs={}
#t.run()
```

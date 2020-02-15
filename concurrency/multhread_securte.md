| 参数名称   |                                     含义                                      |
|:---------- |:-----------------------------------------------------------------------------:|
| daemon属性 | 表示线程是否是daemon线程,这个值必须在start()之前设置,否则引发RuntimeError异常 |
| isDaemon() |                               是否是daemon线程                                |
|    setDaemon        | 设置为daemon线程,必须在start方法之前设置 |                                                                               |

```python
import time
import threading


def worker(name, timeout):
    time.sleep(timeout)
    print('{} working'.format(name))


# 主线程 是non-daemon线程
t1 = threading.Thread(target=worker, args=('t1', 2), name="work100",daemon=True) # 调换5和10看看效果
t1.start()
t2 = threading.Thread(target=worker, args=('t2', 4), name="work200",daemon=False)
t2.start()
print('end================================')

import sys
sys.exit(100)



'''
t = threading.Thread(target=foo, daemon=False) 试一试
发现线程(daemon为false or none)t依然执行,主线程已经执行完,但是一直等着线程t。
修改为 t = threading.Thread(target=foo, daemon=True) 试一试
线程（daemon为true）程序立即结束了,主线程根本没有等线程t

线程具有一个daemon属性,可以手动设置为True或False,也可以不设置,则取默认值None。
如果不设置daemon,就取当前线程的daemon来设置它。
主线程是non-daemon线程,即daemon = False。
从主线程创建的所有线程的不设置daemon属性,则默认都是daemon = False,也就是non-daemon线程。
Python程序在没有活着的non-daemon线程运行时,程序退出,也就是除主线程之外剩下的只能都是daemon线
程,主线程才能退出,否则主线程就只能等待


'''
```

```python

import time
import threading


def worker(name, timeout):
    time.sleep(timeout)
    print('{} working'.format(name))


# 主线程 是non-daemon线程
t1 = threading.Thread(target=worker, args=('t1', 2), name="work100",daemon=True) # 调换5和10看看效果
t1.start()
t1.join() #阻塞 t1线程执行完后 主线调用了t1.join 就必须等待t1完成后在执行 其中 timeout等待的时间 默认为none 永久等待
print('end================================')

import sys
sys.exit(100)
'''

join(timeout=None),是线程的标准方法之一。
一个线程中调用另一个线程的join方法,调用者将被阻塞,直到被调用线程终止。
一个线程可以被join多次。
timeout参数指定调用者等待多久,没有设置超时,就一直等到被调用线程结束。
调用谁的join方法,就是join谁,就要等谁。

'''

'''
/home/joey/python/code/venv/bin/python /home/joey/python/code/t1.py
t1 working
end================================

Process finished with exit code 100


'''
```

## threading.loca


```python
import threading
import time

#x = 0

global_data = threading.local()

# threading.local() 代码要阅读     为每一个线程增加一个dict 保存数据
def worker():
    #x=0 #  在多线程中国 使用局部变量 那是绝对的安全 因为运行在每一个线程中栈
    #global x #gloabl
    global_data = 0

    for i in range(100):
        time.sleep(0.0001)
        global_data  += 1
    print(threading.current_thread(), global_data)


for i in range(10):
    threading.Thread(target=worker).start()
```

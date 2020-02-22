
# **<font color=Red> ASYNCIO**
- **<font color=Red>事件循环是asyncio提供的核心运行机制**。

```python
import threading
import time

def a():
    for i in range(3):
        print("a.x", i)
        yield


def b():
    for x in range(3):
        print("b.x", x)
        yield
x=a()
y=b()

for i in range(3):#循环 生成器函数
    next(x)
    next(y)
```
# **<font color=>协程**

- 协程不是进程、也不是线程,它是用户空间调度的完成并发处理的方式
- 进程、线程由操作系统完成调度,而协程是线程内完成调度。它不需要更多的线程,自然也没有多线程切换
带来的开销
- 协程是非抢占式调度,只有一个协程主动让出控制权,另一个协程才会被调度
协程也不需要使用锁机制,因为是在同一个线程中执行
- 多CPU下,可以使用多进程和协程配合,既能进程并发又能发挥协程在单线程中的优势
- Python中协程是基于生成器的
- asyncio.iscoroutine(obj) 判断是不是协程对象
-  asyncio.iscoroutinefunction(func) 判断是不是协程函数

### **<font color=>Future**
- 和concurrent.futures.Future类似。通过Future对象可以了解任务执行的状态数据。
事件循环来监控Future对象是否完成。
### **<font color=>FTask任务**
- Task类是Future的子类,它的作用就是把协程包装成一个Future对象。

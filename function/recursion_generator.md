# **<font color=Red>递归函数**




# **<font color=Red>生成器函数****

- 生成器函数
 - 包含yield语句的生成器函数调用后,生成 生成器对象 的时候,生成器函数的函数体不会立即执行
 - next(generator) 会从函数的当前位置向后执行到之后碰到的第一个yield语句,会弹出值,并暂停函数执行
 - 再次调用next函数,和上一条一样的处理过程
 - 继续调用next函数,生成器函数如果结束执行了(显式或隐式调用了return语句),会抛出StopIteration异
常


## **<font color=Red>生成器generator**
 - 生成器指的是生成器对象,可以由生成器表达式得到,也可以使用yield关键字得到一个生成器函数,调用这函数得到一个生成器对象
 - 生成器对象,是一个可迭代对象,是一个迭代器
 - 生成器对象,是延迟计算、惰性求值的

## **<font color=Red>生成器函数**
- 函数体中# **<font color=Red>包含yield语句的函数**,就是生成器函数,调用后返回生成器对象

- 普通函数调用,函数会立即执行直到执行完毕。
- 生成器函数调用,并不会立即执行函数体,而是需要使用next函数来驱动生成器函数执行后获得的生成器对象。
- 生成器表达式和生成器函数都可以得到生成器对象,只不过生成器函数可以写的更加复杂的逻辑

```python

def inc():
    for i in range(5):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        yield i
        print("++++++++++++++++++++++++++")

#无限循环
def inc():
    count += 0
    while True:
        count += 1
        yield count

g = inc()
[next(g) for i in range(10)]

#_--------------------------------------------------
    count = 0
    while True:
        count += 1
        yield count

def inc():
    c = counter()
    return next(c)

print(inc())
print(inc())
print(inc())

１
１
１

#_----------------------------－－－－－－－－－－－－－－－－－－－－
def counter():
    count = 0
    while True:
        count += 1
        yield count

#print(inc.__defaults__) default　默认值在函数定义是就已经定义好了
def inc(c = counter()):
    return next(c)

print(inc())
print(inc())
print(inc())

１
２
３


#-----------------------------

def inc():
    def counter():
        count = 0
        while True:
            count += 1
            yield count
    c = counter() #每次都重新生成
    return next(c)

print(inc())
print(inc())
print(inc())


1
1
1
#-----------------------------------------------
def inc():
    def counter():
        count = 0
        while True:
            count += 1
            yield count
    c = counter()
    #return lambda :next(c)
    def fn():
      return next(g)
    return fn
g = inc()
print(g())
print(g())
print(g())

1
2
3


-------------------------------------------------
def fin(n):
    a = 0
    b = 1
    while True:
        yield a
        a,b = b,a+b


```


### **<font color=Red>生成器交互**


```python
def inc():
    def counter():
        count = 0
        while True:
            count += 1
            response = yield count
    c = counter()
    #return next(c)
    return lambda :next(c)
g = inc()
g()
g()
g()
```

## **<font color=Red>协程Coroutine**

- 生成器的高级用法
 - 它比进程、线程轻量级,是在用户空间调度函数的一种实现
 - Python3 asyncio就是协程实现,已经加入到标准库
 - Python3.5 使用async、await关键字直接原生支持协程
- 协程调度器实现思路
 - 有2个生成器A、B
 - next(A)后,A执行到了yield语句暂停,然后去执行next(B),B执行到yield语句也暂停,然后再次调用
 - next(A),再调用next(B)在,周而复始,就实现了调度的效果
 - 可以引入调度的策略来实现切换的方式
 - 协程是一种非抢占式调度

 ```python
  def counter():
        count = 0
        while True:
            count += 1
            response = yield count
            if response is not None and isinstance(response,int):
                count = response
  c1=counter()
  c2 = counter()

  for x in range(5):
    print(next(c1))
    next(c2)
    print(next(c2))

 ```

## **<font color=Red> yield from语法**

- 从Python 3.3开始增加了yield from语法,使得  **<font color=Red>yield from iterable 等价于 for item in iterable: yielditem **。
- yield from就是一种简化语法的语法糖。

```python
 def counter():
    count = 0
    while True:
        count += 1
        response = yield count
        if response is not None and isinstance(response, int):
            count = response


def inc(c=None):
    if c is None:
        c = counter
    # for x in c:
    #     yield x
    yield from c

 ```

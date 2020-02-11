## **<font color=Red>高级函数**
- 高阶函数
- 高阶函数(High-order Function)
- 数学概念 y = f(g(x))
在数学和计算机科学中,高阶函数应当是至少满足下面一个条件的函数
 - 接受一个或多个函数作为参数
 - 输出一个函数


 ```python
def counter(base):
    def inc(step=1):
        nonlocal base
        base += step
        return base
    return inc

c1 = counter(10)
c2 = counter(10)

-------------------------------------------------------------------
inc = 100

def inc(step=0):
    return 1

def counter():
    return inc

c1 = counter(10)
c2 = counter(10)

上面两个函数区别是 inc 函数　一个是局部变量，一个全局变量


 ```

## **<font color=Red>实现排序**

```python

def sort(iterable, *, key=None, reverse=False):
  newlist = []
  for x in iterable:
    cx = key(x) if key else x
    for i, y in enumerate(newlist):
      cy = key(y) if key else y
      comp = cx > cy if reverse else cx < cy # 实现reverse参数
      if comp: # x > y立即插入,说明y小被挤向右边。 换成 x < y是什么意思?
        newlist.insert(i, x)
        break
      else: # 不大于,说明是最小的,尾部追加
        newlist.append(x)
  return newlist


```

### **<font color=Red>排序sorted**

- 定义 sorted(iterable, *, key=None, reverse=False) ->list

```python
sorted(lst, key=lambda x:6-x) # 返回新列表
list.sort(key=lambda x: 6-x) # 就地修改
```


### **<font color=Red>过滤filter**



- 定义 filter(function, iterable) == if element : return element
- 对**<font color=Red>可迭代对象进行遍历,返回一个迭代器</font>**
- function参数是一个参数的函数,且返回值应当是bool类型,或其返回值等效布尔值。
- function参数如果是None,可迭代对象的每一个元素自身等效布尔值
- 把可迭代的对象拿出来　一个个进行过滤，

```
list(filter(lambda x: x%3==0, [1,9,55,150,-3,78,28,123]))
list(filter(None, range(5)))
list(filter(None, range(-5, 5)))
list(filter(lambda x:True, range(-5,5)))

list(filter(lambda x:None, range(-5,5))) # if(fn(element)):yield element
```


### **<font color=Red>映射map**
- 定义 map(function, *iterables) -> map object
- 对多个可迭代对象的元素,按照指定的函数进行映射 返回一个迭代器

```
list(map(lambda x: 2*x+1, range(10)))
dict(map(lambda x: (x%5, x), range(500)))
dict(map(lambda x,y: (x,y), 'abcde', range(10)))
```
# **<font color=Red>柯里化**

- 指的是将原来接受两个参数的函数变成新的接受一个参数的函数的过程。新的函数返回一个以原有第二个参
数为参数的函数
- z = f(x, y) 转换成 z = f(x)(y)的形式

```python

def add(x,y):
    def _add(z):
        return x+y+z
    return _add


def add(x):
    def _add(y):
        def __add(z):
            return x+y+z
        return __add
    return _add


def add(x):
    def _add(y,z):
        return x+y+z
    return _add



```

# **<font color=Red>装饰器**


```python
def add(x,y):
    return x+y


def logger(fn):
    print("before")
    print("add function: {} {}".format(4,5))
    ret = fn(4,5)
    print("after")
    return ret
logger(add)

def add(x,y):
    return x+y


def logger(fn,*args,**kwargs):
    print("before")
    print("add function: {} {}".format(args,kwargs))
    ret = fn(*args,**kwargs)
    print("after")
    return ret
logger(add,4,5) -- _logger(add)(4,5) 可列化


def add(x,y):
    return x+y


def logger(fn):
    def _logger(*args,**kwargs):
        print("before")
        print("add function: {} {}".format(args,kwargs))
        ret = fn(*args,**kwargs)
        print("after")
        return ret
    return _logger

logger(add)(4,5)

－－－－－－－－－－－－－－－----------------------装饰器：
def logger(fn):
    def _logger(*args,**kwargs):
        print("before")
        print("add function: {} {}".format(args,kwargs))
        ret = fn(*args,**kwargs)
        print("after")
        return ret
    return _logger


@logger # 等价于logger(add)
def add(x,y):
    return x+y


@logger 等价式 add = logger(add) ==> add=_logger 将装饰的标识符提取，作为自己的参数

add(4,5) ->_logger(4,5) ->logger(add)(4,5)

```

 **<font color=Red>装饰器(无参)@wrapper实际上一个单形参的函数**
 - 是一个函数
 - 函数作为它的形参。无参装饰器实际上就是一个单形参函数
 - 返回值也是一个函数(也可以不返回函数，根据实际的情况)
 - 可以使用@functionname方式,简化调用
 - 注:此处装饰器的定义只是就目前所学的总结,并不准确,只是方便理解

- 装饰器和高阶函数
 - 装饰器可以是高阶函数,但装饰器是对传入函数的功能的装饰(功能增强)




 ```python

import datetime
import time

def copy_properties(src):# 柯里化
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__  = src.__doc__
        return dst
    return _copy

def logger(fn):
    @copy_properties(fn) #－－－－－－>装饰器(带参)@copy_properties(fn)实际上等效为一个单形参的函数
    #--wrapper=copy_properties(fn)(wrapper)
    #-->_copy(wrapper)
    # returen--wrapper if reture None
    def wrapper(*args,**kwargs):
        '''this is wrapper .......'''
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta =(datetime.datetime.now()-start).total_seconds()
        print("{} took {:.2f}".format(fn.__name__, delta))
        return ret

    #copy_properties(fn)(wrapper)　柯里化

    return wrapper

@logger#－－－－－－>装饰器(无参)@wrapper实际上等效为一个单形参的函数
def add(x,y):
    """
    this is add .......
    """
    time.sleep(2)
    return x+y

 ```



# **<font color=Red>functools模块**
## **<font color=Red>functoolsfrom functools  import update_wrapper,wraps**

```python

import datetime
import time
from functools import update_wrapper,wraps


def copy_properties(src):  # 柯里化
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        return dst

    return _copy


def logger(fn):
    #@copy_properties(fn)  # －－－－－－>装饰器(带参)@copy_properties(fn)实际上等效为一个单形参的函数
    # --wrapper=copy_properties(fn)(wrapper)
    # -->_copy(wrapper)
    # returen--wrapper if reture None
    #@wraps(fn)
    def wrapper(*args, **kwargs):
        '''this is wrapper .......'''
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print("{} took {:.2f}".format(fn.__name__, delta))
        return ret

    # copy_properties(fn)(wrapper)　柯里化
    update_wrapper(wrapper,fn)

    return wrapper


@logger  # －－－－－－>装饰器(无参)@wrapper实际上等效为一个单形参的函数
def add(x, y):
    """
    this is add .......
    """
    time.sleep(2)
    return x + y

add(40,50)
print(add.__name__,add.__doc__)
```

```python
import datetime
import time
from functools import update_wrapper,wraps


def copy_properties(src):  # 柯里化
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        return dst

    return _copy

def logger(drtion=5):
    def _logger(fn,durtion=5):
        #@copy_properties(fn)  # －－－－－－>装饰器(带参)@copy_properties(fn)实际上等效为一个单形参的函数
        # --wrapper=copy_properties(fn)(wrapper)
        # -->_copy(wrapper)
        # returen--wrapper if reture None
        @wraps(fn)
        def wrapper(*args, **kwargs):
            '''this is wrapper .......'''
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            if delta > durtion:
                print("{} took {:.2f}".format(fn.__name__, delta))
            else:
                print("too fast")
            return ret

        # copy_properties(fn)(wrapper)　柯里化
        update_wrapper(wrapper,fn)

        return wrapper
    return _logger


@logger()  # d带参装饰器必须要有()即使是默认值，add = logger()(add)
def add(x, y):
    """
    this is add .......
    """
    time.sleep(2)
    return x + y

add(40,50)
print(add.__name__,add.__doc__)
```

```python

import datetime
import time
from functools import update_wrapper,wraps


def copy_properties(src):  # 柯里化
    def _copy(dst):
        dst.__name__ = src.__name__
        dst.__doc__ = src.__doc__
        return dst

    return _copy


def timetest(delta, duration, fn):
    if duration > delta:
        print("{} took {:.2f} is too slow".format(fn.__name__, delta))

timetest1 = (lambda delta, duration, fn: print("{} took {:.2f} is too slow".format(fn.__name__, delta)) if delta < duration else None )

def logger(duration=3, func=timetest1):
    def _logger(fn):
        #@copy_properties(fn)  # －－－－－－>装饰器(带参)@copy_properties(fn)实际上等效为一个单形参的函数
        # --wrapper=copy_properties(fn)(wrapper)
        # -->_copy(wrapper)
        # returen--wrapper if reture None
        @wraps(fn)
        def wrapper(*args, **kwargs):
            '''this is wrapper .......'''
            start = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - start).total_seconds()
            func(delta,duration,fn)
            return ret

        # copy_properties(fn)(wrapper)　柯里化
        update_wrapper(wrapper,fn)

        return wrapper
    return _logger


@logger()  # －－－－－－>装饰器(无参)@wrapper实际上等效为一个单形参的函数
def add(x, y):
    """
    this is add .......
    """
    time.sleep(2)
    return x + y

add(40,50)
print(add.__name__,add.__doc__)

'''
右边的程序
'''
```

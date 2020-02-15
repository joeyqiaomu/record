
# **<font color=Red>Python类型注解Annotation**

# **<font color=Red>inspect模块**

- signature(callable),获取签名(函数签名包含了一个函数的信息,包括函数名、它的参数类型、它
所在的类和名称空间及其他信息)

- inspect.isfunction(add),是否是函数
- inspect.ismethod(add)),是否是类的方法
- inspect.isgenerator(add)),是否是生成器对象
- inspect.isgeneratorfunction(add)),是否是生成器函数
- inspect.isclass(add)),是否是类
- inspect.ismodule(inspect)),是否是模块
- inspect.isbuiltin(print)),是否是内建对象
- 还有很多is函数,需要的时候查阅inspect模块帮助



```python
import inspect
def add(x:int, y:int, *args,**kwargs) -> int:
return x + y
sig = inspect.signature(add)
print(sig, type(sig)) # 函数签名
print('params : ', sig.parameters) # OrderedDict
print('return : ', sig.return_annotation)
print(sig.parameters['y'], type(sig.parameters['y']))
print(sig.parameters['x'].annotation)
print(sig.parameters['args'])
print(sig.parameters['args'].annotation)
print(sig.parameters['kwargs'])
print(sig.parameters['kwargs'].annotation)
````


```python
import inspect
def add(x,y:int=5,*args,m,n:int=10,**kwargs):
    pass

sig = inspect.signature(add)
params = sig.parameters
'''
params:是一个有序字典,其中是key参数的名称，value是一个字典，值是一个Parameter类型的类
OrderedDict([('x', <Parameter "x:int">), ('y', <Parameter "y:int=6">)])
OrderedDict([('x', <Parameter "x:int">), ('y', <Parameter "y:int=6">)])
OrderedDict([('x', <Parameter "x:int">), ('y', <Parameter "y:int=6">)])
'''

for k,v in params.items():
    print(v.name,k,"--name")
    print(v.default)
    print(v.annotation)
    print(v.kind)

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
x x --name 　　　　　　　　　参数的名称
<class 'inspect._empty'> 参数的默认值
<class 'inspect._empty'>　参数的注解
POSITIONAL_OR_KEYWORD　　参数的类型

y y --name
5　　　－　参数的默认值
<class 'int'>　－参数的注解　－－y:int=5
POSITIONAL_OR_KEYWORD

args args --name
<class 'inspect._empty'>
<class 'inspect._empty'>
VAR_POSITIONAL

m m --name
<class 'inspect._empty'>
<class 'inspect._empty'>
KEYWORD_ONLY

n n --name
10
<class 'int'>
KEYWORD_ONLY

kwargs kwargs --name
<class 'inspect._empty'>
<class 'inspect._empty'>
VAR_KEYWORD

```



# **<font color=Red>参数检查**
```python

import inspect
from inspect import  Parameter
import logging



def check(fn):
    def wrapper(*args,**kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters
        #params :  OrderedDict([('x', <Parameter "x:int">), ('y', <Parameter "y:int">), ('args', <Parameter "*args">), ('kwargs', <Parameter "**kwargs">)])
        print(params)
        #print("+++++++++++++++++========================")
        values = list(params.values())
        keys = list(params.keys())
        # for i, x in enumerate(args):
        #     if not isinstance(x, values[i].annotation):
        #         raise TypeError("waong = {} {}".format(keys[i],x))
        flag = True
        for x,(k,v) in zip(args,params.items()):
            if v.annotation!= inspect._empty and not isinstance(x, v.annotation):
                #raise TypeError("wrong = {} {}".format(k, v))
                flag = False
                break

        for k,v in kwargs.items():
            if params[k].annotation != params[k].empty and not isinstance(v, params[k].annotation):
                #raise TypeError("wrong = {} {} in kwargs".format(k, v))
                flag = False
                break
        if not flag:
            logging.info("annotatios is wrong")
        else:
            ret = fn(*args,**kwargs)
        return ret
    return wrapper

@check
def add(x:int, y:int=6)->int:
    return x + y


add(1,2)
add(4, y=5)
add(x=4,y=5)

```

# **<font color=Red>参数检查　Python之functools**



## **<font color=Red>partial方法**
- 偏函数,把函数部分的参数固定下来,相当于为部分的参数添加了一个固定的默认值,形成一
个新的函数并返回
- 从partial生成的新函数,是对原函数的封装

```python
from functools import update_wrapper,wraps,reduce,partial
import inspect
def add(x,y,z):
    return x + y+z

# print(reduce(lambda x,y:x+y,range(5)))
# print(reduce(lambda x,y:x*y,range(1,5),10))

# newfunc=partial(add,4)
# print(inspect.signature(newfunc))
# #print(newfunc(x=5))#add(4,y)

newfunc=partial(add,y=4)　--> (x, *, y=4, z) 参数签名
print(inspect.signature(newfunc))

print(newfunc(4,z=4))

－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

#partial函数本质
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords): # 包装函数
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func # 保留原函数
    newfunc.args = args # 保留原函数的位置参数
    newfunc.keywords = keywords # 保留原函数的关键字参数参数
    return newfunc
def add(x,y):
return x+y
foo = p




from functools import update_wrapper,wraps,reduce
import inspect


def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords): # 包装函数
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func # 保留原函数
    newfunc.args = args # 保留原函数的位置参数
    newfunc.keywords = keywords # 保留原函数的关键字参数参数
    return newfunc
def add(x,y,*args,z,**kwargs):
    return x+y+z

# print(reduce(lambda x,y:x+y,range(5)))
# print(reduce(lambda x,y:x*y,range(1,5),10))

# newfunc=partial(add,4)
# print(inspect.signature(newfunc))
# #print(newfunc(x=5))#add(4,y)

newfunc1 = partial(add,1,2,3,z=100)
print(newfunc1.func, newfunc1.args,newfunc1.keywords)
print(inspect.signature(newfunc1))
print(newfunc1(1,3,5,7))
'''
: args = (1,2,3)
: fargs =(1,2,3,5)
'''

WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')
WRAPPER_UPDATES = ('__dict__',)
def update_wrapper(wrapper,
                   wrapped,
                   assigned = WRAPPER_ASSIGNMENTS,
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    # Issue #17482: set __wrapped__ last so we don't inadvertently copy it
    # from the wrapped function when updating __dict__
    wrapper.__wrapped__ = wrapped
    # Return the wrapper so this can be used as a decorator via partial()
    return wrapper


def wraps(wrapped,
          assigned = WRAPPER_ASSIGNMENTS,
          updated = WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)

```

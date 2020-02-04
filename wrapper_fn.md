## **装饰器**

```python
import time
from functools import wraps
import inspect
import datetime


def logger(fn):
    print("logger~~~~~~~~~~~")
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs) #cache|wrapper
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__,delta)
        return ret
    return wrapper


def cache(fn):
    print("cache~~~~~~~~~~~")
    local_cache = {}
    @wraps(fn)
    def wrapper(*args,**kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters
        print(params)
        target = {}
        # # values = list(params.keys())
        # target.update(zip(params.keys(), args))#顺序传参的问题
        # 关键字参数
        # for k,v in kwargs.items():
        #     target[k] =v
        target.update(zip(params.keys(), args), **kwargs)
         # 缺省值得问题
        # for k,v in params.items():
        #     if k not in target.keys():
        #         target[k] = v.default


        # for k,_ in(params.keys() - target.keys()):
        #     target[k] = params[k].default

        # target.update(((k,v.default) for k,v in params.items() if k not in target.keys()))

        target.update(((k, params[k].default) for k in(params.keys() - target.keys())))

        key = tuple(sorted(target.items()))
        if key not in local_cache.keys():
            local_cache[key] = fn(**target)
        return local_cache[key]
    return wrapper


@logger  # add = logger(add)  add = logger(cache|wrapper) ->add = logger}wrapper
@cache  # add = cache(add) add = cache | wrapper
def add(x=4, y=5):
    time.sleep(2)
    return x + y


print(add())
# print("=====================")
# print(add(x=4))
# print(add(y=5))
# print(add())
'''
装饰器调用的顺序 有下至上，由近至远的调用
cache~~~~~~~~~~~
logger~~~~~~~~~~~
OrderedDict([('x', <Parameter "x=4">), ('y', <Parameter "y=5">)])
add 2.000544
9
'''

```

## 增加cache移除
```python

iimport time
from functools import wraps
import inspect
import datetime


def logger(fn):
    print("logger~~~~~~~~~~~")
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs) #cache|wrapper
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__,delta)
        return ret
    return wrapper

def cache(duration=5):
    def _cache(fn):
        print("cache~~~~~~~~~~~")
        local_cache = {}
        @wraps(fn)
        def wrapper(*args,**kwargs):
            now = datetime.datetime.now().timestamp()
            #expire_keys = [k for k, (_, timestamp) in local_cache.items() if now - timestamp > duration ]
            # expire_keys = []
            # for k,(_,timestamp) in local_cache.items():
            #     if now - timestamp > duration: #出错的情况呢？？？？？
            #         expire_keys.append(k)
            for k in [k for k, (_, timestamp) in local_cache.items() if now - timestamp > duration ]:
                local_cache.pop(k)

            sig = inspect.signature(fn)
            params = sig.parameters
            print(params)
            target = {}
            # # values = list(params.keys())
            # target.update(zip(params.keys(), args))#顺序传参的问题
            # 关键字参数
            # for k,v in kwargs.items():
            #     target[k] =v
            target.update(zip(params.keys(), args), **kwargs)
             # 缺省值得问题
            # for k,v in params.items():
            #     if k not in target.keys():
            #         target[k] = v.default


            # for k,_ in(params.keys() - target.keys()):
            #     target[k] = params[k].default

            # target.update(((k,v.default) for k,v in params.items() if k not in target.keys()))

            target.update(((k, params[k].default) for k in(params.keys() - target.keys())))

            key = tuple(sorted(target.items()))
            if key not in local_cache.keys():
                local_cache[key] = fn(**target), datetime.datetime.now().timestamp()
            return local_cache[key]
        return wrapper
    return _cache


@logger  # add = logger(add)  add = logger(cache|wrapper) ->add = logger}wrapper
@cache()  # add = cache(add) add = cache | wrapper
def add(x=4, y=5):
    time.sleep(2)
    return x + y


print(add())
print("=====================")
print(add(x=4))
time.sleep(4)
print("=====================")
print(add(y=5))
print(add())


'''
装饰器调用的顺序 有下至上，由近至远的调用
cache~~~~~~~~~~~
logger~~~~~~~~~~~
OrderedDict([('x', <Parameter "x=4">), ('y', <Parameter "y=5">)])
add 2.000544
9
'''
```
```python
import time
from functools import wraps
import inspect
import datetime


def logger(fn):
    print("logger~~~~~~~~~~~")
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs) #cache|wrapper
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__,delta)
        return ret

    return wrapper


def _make_key(fn,args, kwargs):
    sig = inspect.signature(fn)
    params = sig.parameters
    print(params)
    target = {}
    # # values = list(params.keys())
    # target.update(zip(params.keys(), args))#顺序传参的问题
    # 关键字参数
    # for k,v in kwargs.items():
    #     target[k] =v
    target.update(zip(params.keys(), args), **kwargs)
    # 缺省值得问题
    # for k,v in params.items():
    #     if k not in target.keys():
    #         target[k] = v.default
    # for k,_ in(params.keys() - target.keys()):
    #     target[k] = params[k].default
    # target.update(((k,v.default) for k,v in params.items() if k not in target.keys()))
    target.update(((k, params[k].default) for k in (params.keys() - target.keys())))
    key = tuple(sorted(target.items()))
    return key,target


def _clean_expires(cache, duration):
    now = datetime.datetime.now().timestamp()
    for k in [k for k, (_, timestamp) in cache.items() if now - timestamp > duration]:
        cache.pop(k)


def cache(duration=5):
    def _cache(fn):
        print("cache~~~~~~~~~~~")
        local_cache = {}
        @wraps(fn)
        def wrapper(*args,**kwargs):
            #l懒策略，清除过去数据
            _clean_expires(local_cache,duration)
            #创建key
            key, target = _make_key(fn, args, kwargs)

            if key not in local_cache.keys():
                local_cache[key] = fn(**target), datetime.datetime.now().timestamp()
            return local_cache[key]

        return wrapper
    return _cache


@logger  # add = logger(add)  add = logger(cache|wrapper) ->add = logger}wrapper
@cache()  # add = cache(add) add = cache | wrapper
def add(x=4, y=5):
    time.sleep(2)
    return x + y


print(add())
print("=====================")
print(add(x=4))
time.sleep(5)
print("=====================")
print(add(y=5))
print(add())


'''
装饰器调用的顺序 有下至上，由近至远的调用
cache~~~~~~~~~~~
logger~~~~~~~~~~~
OrderedDict([('x', <Parameter "x=4">), ('y', <Parameter "y=5">)])
add 2.000544
9
'''
```
```python
import time
from functools import wraps
import inspect
import datetime


def logger(fn):
    print("logger~~~~~~~~~~~")
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs) #cache|wrapper
        delta = (datetime.datetime.now() - start).total_seconds()
        print(fn.__name__,delta)
        return ret

    return wrapper

from collections import OrderedDict
def _make_key(fn,args, kwargs):
    sig = inspect.signature(fn)
    params = sig.parameters
    print(params)
    #target = {}
    target  = OrderedDict()
    # # values = list(params.keys())
    # target.update(zip(params.keys(), args))#顺序传参的问题
    # 关键字参数
    # for k,v in kwargs.items():
    #     target[k] =v
    # target.update(zip(params.keys(), args), **kwargs)
    # 缺省值得问题
    # for k,v in params.items():
    #     if k not in target.keys():
    #         target[k] = v.default
    # for k,_ in(params.keys() - target.keys()):
    #     target[k] = params[k].default
    # target.update(((k,v.default) for k,v in params.items() if k not in target.keys()))

    target.update(zip(params.keys(), args))
    for k ,v in params.items():
        if k not in target.keys():
            if k in kwargs.keys():
                target[k] = kwargs[k]
            else:
                target[k] = v.default
    # target.update(((k, params[k].default) for k in (params.keys() - target.keys())))
    #key = tuple(sorted(target.items()))
    key = tuple(sorted(target.items()))
    return key, target


def _clean_expires(cache, duration):
    now = datetime.datetime.now().timestamp()
    for k in [k for k, (_, timestamp) in cache.items() if now - timestamp > duration]:
        cache.pop(k)


def cache(duration=5):
    def _cache(fn):
        print("cache~~~~~~~~~~~")
        local_cache = {}
        @wraps(fn)
        def wrapper(*args,**kwargs):
            #l懒策略，清除过去数据
            _clean_expires(local_cache,duration)
            #创建key
            key, target = _make_key(fn, args, kwargs)

            if key not in local_cache.keys():
                local_cache[key] = fn(**target), datetime.datetime.now().timestamp()
            return local_cache[key]

        return wrapper
    return _cache


@logger  # add = logger(add)  add = logger(cache|wrapper) ->add = logger}wrapper
@cache()  # add = cache(add) add = cache | wrapper
def add(x=4, y=5):
    time.sleep(2)
    return x + y


print(add())
print("=====================")
print(add(x=4))
time.sleep(5)
print("=====================")
print(add(y=5))
print(add())


'''
装饰器调用的顺序 有下至上，由近至远的调用
cache~~~~~~~~~~~
logger~~~~~~~~~~~
OrderedDict([('x', <Parameter "x=4">), ('y', <Parameter "y=5">)])
add 2.000544
9
'''
```

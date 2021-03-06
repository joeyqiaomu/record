# **CLASS属性**

```
 - __name__ 类函数方法的名字
 - __module__ 类定义所在的模块名
 - __class__ 对象或类所属的类
 - __bases__ 类的基类的元组,顺序为它们在基类列表中出现的顺序
 - __doc__ 类、函数的文档字符串,如果没有定义则为None
 - __mro__ 类的mro,class.mro()返回的结果的保存在 __mro__ 中
 - __dict__ 类或实例的属性,可写的字典
 ```


## **dir() **
```
- dir(obj)对于不同类型的对象obj具有不同的行为:
  - 如果对象是模块对象,返回的列表包含模块的属性名和变量名
  - 如果对象是类型或者说是类对象,返回的列表包含类的属性名,及它的祖先类的属性名
  - 如果是类的实例
     - 有 __dir__ 方法,返回可迭代对象的返回值
     - 没有 __dir__ 方法,则尽可能收集实例的属性名、类的属性和祖先类的属性名
 - 如果obj不写,返回列表包含内容不同
     - 在模块中,返回模块的属性和变量名
     - 在函数中,返回本地作用域的变量名
     - 在方法中,返回本地作用域的变量名

```
```python
import t1
from t1 import Animal


class Cat(Animal):
    x = 'cat'
    y = 'abcd'


class Dog(Animal):

    def __init__(self,name):
        super().__init__(name)
        self.a = 100

    def __dir__(self): #仅仅影响实例*****************************
        return ['dog'] # 必须返回可迭代对象


print('---------')
print('Current Module\'s names = {}'.format(dir())) # 模块名词空间内的属性
print('animal Module\'s names = {}'.format(dir(t1))) # 指定模块名词空间内的属性

print('++++++++++++++++++++++++++++++++++++++++++')

print(dir(Cat))
print(Cat.__dict__.keys() | Animal.__dict__.keys()|object.__dict__.keys())

c = Cat("garfied")
print(dir(c))
print(Cat.__dict__.keys() | Animal.__dict__.keys()|object.__dict__.keys())

print('+++++++++++*************************++++++')
d = Dog("dog")
print(dir(Dog))
print(dir(d))
```


### 内建函数
- locals() 返回当前作用域中的变量字典
- globals() 当前模块全局变量的字典


```python

class A:
    def show(self): # 方法中
        a = 100
        t = int(a)
        print(dir())
        print(locals())


def test(a=50, b=100): # 函数中
    c = 150
    print(dir())
    print(locals())

print(1,dir())
print(2,sorted(locals().keys()))
print(2,sorted(globals().keys()))
test()
A().show()

'''

1 ['A', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'test']
2 ['A', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'test']
2 ['A', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'test']
['a', 'b', 'c']
{'c': 150, 'b': 100, 'a': 50}
['a', 'self', 't']
{'t': 100, 'a': 100, 'self': <__main__.A object at 0x7fbef172cd68>}
'''


```
- 分类:
 - 创建、初始化与销毁
__new__
__init__ 与 __del__
可视化
hash
bool
运算符重载
容器和大小
可调用对象
上下文管理
反射
描述器
其他杂项


## **实例化**


### **创建、初始化与销毁**
```
__new__：构造方法
    实例化一个对象
    该方法需要返回一个值,如果该值不是cls的实例,则不会调用 __init__
    该方法永远都是静态方法

__init__  初始化方法
 __del__ 析构方法

```
```python
‘’‘
1 现有创建实例 __new__
2 实例初始化，出厂配置 __init__
3 实例删除 也即是引用计数清零



class A:
    def __new__(cls, *args,**kwargs): # static 方法 手工注入cls
        print(cls)
        print(args)
        args = 'jerry'
        cls.test = 'abc' #增加一个类的属性 但是没定义一个实例都要创建，不好
        print(kwargs)
        #return super().__new__(cls) # 注意__new__方法没用【在元编程中有用】
        ret = super().__new__(cls)  # 注意__new__方法没用【在元编程中有用】
        return ret

    def __init__(self,name):
        self.name = name

a = A("tom") #
#第一步调用__new__ 返回实例
#第二步 __new__返回的实例交给__init__进行初始化

print(a)

’‘’
```
## **可化和hash**
-  print format str 都要调用__str__ ,如果没有__str__,则调用__repr__
-  除了上述（print format str）外，都用__repr__ 如果__repr__不存在，直接调用父类

- __注意不能通过判断是否带引号来判断输出值的类型,类型判断要使用type或isinstance__


```python
‘’‘
__str__ -- str
_repr__ --repr

’‘’

class Persion:
    def __new__(cls, *args,**kwargs): # static 方法 手工注入cls
        print(cls)
        print(args)
        args = 'jerry'
        cls.test = 'abc' #增加一个类的属性 但是没定义一个实例都要创建，不好
        print(kwargs)
        #return super().__new__(cls) # 注意__new__方法没用【在元编程中有用】
        ret = super().__new__(cls) # 注意__new__方法没用【在元编程中有用】
        return ret

    def __init__(self,name,age):
        self.name = name
        self.age = age

a = Persion("tom",10) # __new__ 返回实例 交给__init__进行初始化
b = Persion("jerry",20) # __new__ 返回实例 交给__init__进行初始化
print(a)
‘’‘
此打印出来的结果为 很难看懂，
<__main__.Persion object at 0x7f397649f320>
’‘’

------------------------------------------------------------

class Persion:
    # def __new__(cls, *args,**kwargs): # static 方法 手工注入class
    #     print(cls)
    #     print(args)
    #     args = 'jerry'
    #     cls.test = 'abc' #增加一个类的属性 但是没定义一个实例都要创建，不好
    #     print(kwargs)
    #     #return super().__new__(cls) # 注意__new__方法没用【在元编程中有用】
    #     ret = super().__new__(cls) # 注意__new__方法没用【在元编程中有用】
    #     return ret

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "str : {} {}".format(self.name,self.name)

    def __repr__(self):
        return "repr : {} {}".format(self.name,self.name)

    def __bytes__(self):
        return "bytes : {} {}".format(self.name,self.name).encode()



a = Persion("tom",10) # __new__ 返回实例 交给__init__进行初始化
b = Persion("jerry",20) # __new__ 返回实例 交给__init__进行初始化
print(a)
print(str(a)) #调用__str__
print(bytes(a)) #调用__bytes__
print(repr(a)) #调用__repr__

print("~~~~~~~~~~~~~~")
print([a],(a,)) #调用__repr__
print(a) #调用__repr__
print(str(a)) #调用__repr__
print('{}'.format(a)) #调用__repr__

# print format str 都要调用__str__ ,如果没有__str__,则调用__repr__
# 除了上述（print format str）外，都用__repr__ 如果__repr__不存在，直接调用父类

```
## **hash**
- 内建函数 hash() 调用的返回值,返回一个整数。如果定义这个方法该类的实例就可hash

```python
'''
 __hash__ ----- hash函数

 __eq__ ：对应==操作符,判断2个对象是否相等,返回bool值 定义了这个方法,如果不提供 __hash__ 方法,那么实例将不可hash了


__hash__： 内建函数 hash() 调用的返回值,返回一个整数。如果定义这个方法该类的实例就可hash。


__hash__ 方法只是返回一个hash值作为set的key,但是 去重 ,还需要 __eq__ 来判断2个对象是否相等。
hash值相等,只是hash冲突,不能说明两个对象是相等的。因此,一般来说提供 __hash__ 方法是为了作为set或者dict的key,如果 去重 要同时提供 __eq__ 方法。


不可hash对象isinstance(p1, collections.Hashable)一定为False。去重 需要提供 __eq__ 方法。

list 为什么不能hash？？ 因为list类中有一个 __hash__ == None

'''

class Persion:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Person : {} {}>".format(self.name, self.name)


    def __hash__(self): #必须返回是integer TypeError: __hash__ method should return an integer
        return  1

#最简单的hash 就是取摸反 1%5
a = Persion("tom",10) # __new__ 返回实例 交给__init__进行初始化
print(hash(a))

print(hash("abc"))
print(hash("abc"))

```
```python

'''
对于一个类来说：相等是 表示内容相同 但是实例相等 但是object的==方法是比较地址 和 is方法一致 a == b 是比较地址

set  去重必须是要hash 和 内容都相同
'''

class Persion:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "<Person : {} {}>".format(self.name, self.age)

    def __eq__(self, other): # ==的魔术方法
        return self.age == other.age


    def __hash__(self): #必须返回是integer TypeError: __hash__ method should return an integer
        # import random
        # return random.randint(1,100)
        return 123

    __hash__ = None --哈希函数为none 　不可哈希

#最简单的hash 就是取摸反 1%5
a = Persion("tom",10) # __new__ 返回实例 交给__init__进行初始化
b = Persion("tom",10) # __new__ 返回实例 交给__init__进行初始化
print(id(a), hash(a))
print(id(b), hash(b))
print({123, 123})
print({a,b}) #去重复是内容相同 不是hash值相同
print("`````````````", a == b) # == 是表示内容相同 但是object的==方法是比较地址 和 is方法一致 a == b 是比较地址

s = {a,b}
print(id(s.pop()))

#set  去重必须是要hash 和 内容都相同
# t1=(123,)
# t2=(123,)
#
# print(id(t1), hash(t1))
# print(id(t2), hash(t2))
# print({t1,t2})
#

’‘’
  def __hash__(self): #必须返回是integer TypeError: __hash__ method should return an integer
        # import random
        # return random.randint(1,100)
        return 123


注意 修改了 _eq__函数 比较结果不一样
/home/joey/python/code/venv/bin/python /home/joey/python/code/t1.py
139650566409576 123
139650566409632 123
{123}
{<Person : tom 10>}
````````````` True
139650566409576

Process finished with exit code 0

/home/joey/python/code/venv/bin/python /home/joey/python/code/t1.py
140511667085096 96
140511667143624 1
{123}
{<Person : tom 10>, <Person : tom 10>}
````````````` True
140511667085096

Process finished with exit code 0
‘’’

'''
hash函数:如果类实现了__eq__函数，那么必须要实现 __hash__方法 否则不可hash
TypeError: unhashable type: 'Point'


'''
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __hash__(self):
        #return super().__hash__()
        return hash((self.x,self.y)) #函数实现（传入元祖）

    def __repr__(self):
        return '<Point {} {}>'.format(self.x,self.y)


p1 = Point(4,5)
p2 = Point(4,5)

print(p1 is p2,p1 == p2)

print(hash(p1),hash(p2))

print({p1,p2})
```




## **bool等效**

```python
’‘’
如果一个实例可以用 bool 函数 要用　__bool__
如果没有　__bool__　方法，就判断 __len__　方法

‘’’
class A:
    def __bool__(self):
        print("in bool ")
        return bool(1)
        return bool(self) #自己调用自己


print(bool(A))
print(bool(A()))

print(bool([]))

if A():
    print("a ~~~~~~~~`")
```

## **运算符重载**
- 比较运算符
  - <, <=, ==, >,
  -  __lt__ , __le__ , __eq__ , __gt__ , __ge__ , __ne__
- 算数运算符,移位、位运算也有对应的方法
  - +, -, *, /, %, //,
  - __add__ , __sub__ , __mul__ , __truediv__ , __mod__ ,
**, divmod __floordiv__ , __pow__ , __divmod__
-
  - +=, -=, *=, /=, __iadd__ , __isub__ , __imul__ , __itruediv__ , %=, //=, **= __imod__ , __ifloordiv__ , __ipow__

```python
class A:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def __sub__(self, other):
        return self.age - other.age

    def __isub__(self, other): # 如果没有定义__isub__,则会调用__sub__
        #return A(self.name, self - other) #实例地址改变
        self.age -= other.age
        return self  # 实例地址不改变

a1= A("tom")
a2= A("jerry",20)
a1 - a2 # 调用 __sub__
a1 -= a2  #调用 __isub__ ,如果没有__isub__不存在 则调用__sub__
print(a1 - a2)
print(a2 - a1)
#——————————————————————————————————————————————————————————————————————————

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __hash__(self):
        #return super().__hash__()
        return hash((self.x,self.y))

    def __repr__(self):
        return '<Point {} {}>'.format(self.x,self.y)

    def add(self,o):
        return self.__class__(self.x + o.x,self.y+o.y)

    __add__ = add

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


p1 = Point(4,5)
p2 = Point(4,5)

print(p1.add(p2))
#运算符重载
print(p1 + p2 + p2) #链式编程 注意返回值 一定要实例本身
print((p1 + p2).add(p2).__add__(p2) + p2) #链式编程 注意返回值 一定要实例本身

'''

'''
```
```python
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __hash__(self):
        #return super().__hash__()
        return hash((self.x,self.y))

    def __repr__(self):
        return '<Point {} {}>'.format(self.x,self.y)

    def add(self,o):
        return self.__class__(self.x + o.x,self.y+o.y)


    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


p1 = Point(4,5)
p2 = Point(4,5)

print(p1.add(p2))
print(p1 + p2 + p2) #链式编程 注意返回值 一定要实例本身
print((p1 + p2).add(p2).__add__(p2) + p2) #链式编程 注意返回值 一定要实例本身


```
#### **functools.total_ordering 装饰器**

```python

from functools import total_ordering

@total_ordering
class A:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self,other):
        return self.age > other.age

    # def __ge__(self,other):
    #     return self.age >= other.age
a1= A("tom")
a2= A("jerry",20)

print(a1 > a2)
print(a2 < a1)

------------------------------

class A:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self,other):
        return self.age > other.age

    def __ge__(self,other):
        return self.age >= other.age
a1= A("tom")
a2= A("jerry",20)

print(a1 > a2)
print(a2 < a1)

'''
__eq__ 等于可以推断不等于
__gt__ 大于可以推断小于
__ge__ 大于等于可以推断小于等于
也就是用3个方法,就可以把所有比较解决了,所以total_ordering可以不使用
'''
```


## **容器化 __len__ __iter__ __getitem__ __setitem__**

```python

__len__() :  内建函数len(),返回对象的长度(>=0的整数),如果把对象当做容器类型看,就如同list
或者dict。__len__() bool()函数调用的时候,如果没有 __bool__() 方法,则会看 __len__() 方法是否存在,
存在返回非0为真

__iter__() :  迭代容器时,调用,返回一个新的迭代器对象
__contains_()) : in 成员运算符,没有实现,就调用 __iter__ 方法遍历
__getitem__() : 实现self[key]访问。序列对象,key接受整数为索引,或者切片。对于set和dict,key为hashable。key不存在引发KeyError异常
__setitem__(): __setitem__ 和 __getitem__ 的访问类似,是设置值的方法


__missing__():  字典或其子类使用 __getitem__() 调用时,key不存在执行该方法

为什么空字典、空字符串、空元组、空集合、空列表等可以等效为False? 因为len反复的值为0
```
### **购物车容器化**
```python
class Cart:

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)
        return self

    def __iter__(self):
    # yield from self.items
        return iter(self.items)

    def __getitem__(self, index): # 索引访问
        return self.items[index]

    def __setitem__(self, key, value): # 索引赋值
        self.items[key] = value

    # def __str__(self):
    #     return str(self.items)
    #
    def __add__(self, other): # +
        self.add(other)
        return self

    def __repr__(self):
        return "< {} {} >".format(__class__.__name__,self.items)


cart = Cart()

cart.add(1)
cart.add(2)
print(len(cart)) # 对应是__len__ 方法
print(cart[0]) #对应是__getitme__ 方法
for x in cart: #对应是__iter__ 方法
    print(x)
cart[0] = 100 # 对应是__setitme__ 方法
print(cart)

cart + 5 +4
print(cart)

```

## **可调用对象(任意一个类的实例是否可调用)**

```
__call__ : 类中定义一个该方法,实例就可以像函数一样调用
```
```python
class Fib:

    def __init__(self):
        self.items = [0,1,1]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        if index < 0 :
            raise IndexError("Not Negative index")
        print("11111111111111")
        if index < len(self):
            return self.items[index]
        print("2222222222222222222222222222222")
        for i in range(len(self.items) ,index+1): #3
            self.items.append(self.items[i-1] + self.items[i-2])
            print("######################################3")
        return self.items[index]


    def __repr__(self):
        return "<{}{}>".format(__class__.__name__,self.items)


    def __call__(self, index):
        return self[index]


f = Fib()

print(f(35))
print("---------------------------------")
print(f[40])
print(f(6))
print(f)

----------------------------------------------------------------
class Fib:

    def __init__(self):
        self.items = [0,1,1]

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __call__(self, index):
        if index < 0 :
            raise IndexError("Not Negative index")
        print("11111111111111")
        if index < len(self):
            return self.items[index]
        print("2222222222222222222222222222222")
        for i in range(len(self.items) ,index+1): #3
            self.items.append(self.items[i-1] + self.items[i-2])
            print("######################################3")
        return self.items[index]


    def __str__(self):
        return "<{}{}>".format(__class__.__name__,self.items)


    __repr__ = __str__


    def __getitem__(self, index):
        return self(index)


f = Fib()

print(f(35))
print("---------------------------------")
print(f[40])
print(f(6))
print(f)
```


## **上下文管理**

```
 __enter__ :　进入与此对象相关的上下文。如果存在该方法,with语法会把该方法的返回值作为绑定到as
子句中指定的变量上

 __exit__　：　退出与此对象相关的上下文。

 当一个对象同时实现了 __enter__ ()和 __exit__ ()方法,它就属于上下文管理的对象

```
```python

class Point:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
with Point() as p: # AttributeError: __exit__
    pass

'''
/home/joey/python/code/venv/bin/python /home/joey/python/code/t1.py
Traceback (most recent call last):
  File "/home/joey/python/code/t1.py", line 8, in <module>
    with Point() as p: # AttributeError: __exit__
AttributeError: __enter__


/home/joey/python/code/venv/bin/python /home/joey/python/code/t1.py
Traceback (most recent call last):
  File "/home/joey/python/code/t1.py", line 7, in <module>
    with Point() as p: # AttributeError: __exit__
AttributeError: __exit__



'''

'''
__enter__ : 进入与此对象相关的上下文。如果存在该方法,with语法会把该方法的返回值作为绑定到as 子句中指定的变量上
__exit__　；　退出与此对象相关的上下文。
当一个对象同时实现了 __enter__ ()和 __exit__ ()方法,它就属于上下文管理的对象


with p as f:
with语法,
   会调用with后的对象的__enter__方法,
    如果有as,则将该方法的返回值赋给as子句的变量上例,可以等价为f = p.__enter__()


__enter__ 方法 没有其他参数。
__exit__ 方法有3个参数:
__exit__(self, exc_type, exc_value, traceback)
这三个参数都与异常有关。
如果该上下文退出时没有异常,这3个参数都为None。
如果有异常,参数意义如下
exc_type ,异常类型
exc_value ,异常的值
traceback ,异常的追踪信息
__exit__ 方法返回一个等效True的值,则压制异常;否则,继续抛出异常
'''

import time
class Point:

    def __init__(self):
        print(1, "init~~~~~~~~~~~~~~")
        time.sleep(3)

    def __enter__(self):
        print(2, "enter~~~~~~~~~~~~~~")
        time.sleep(3)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(5, " exit~~~~~~~~~~~~~")
        time.sleep(3)

with 是　进入with快调用witｈ后面的实例(Point())的__enter__ 离开是调用witｈ后面的实例(Point())的__exit__

with Point() as p: #  b = self.__enter__()__ 返回值是自己的self_
    print(3, "enter with ~~~~~~~~~~~~~~")
    1/0 #　出现异常情况下　执行顺序　１　２　３　５　
    time.sleep(3)
    print(4, "exit with ~~~~~~~~~~~~~~")

p = Point()
with p as f:
  print('in with-------------')
  print(p == f)
  print('with over')
  print('=======end==========')
with语法,会调用with后的对象的__enter__方法,如果有as,则将该方法的返回值赋给as子句的变量上例,可以等价为f = p.__enter__()

执行顺序

/home/joey/python/code/venv/bin/python /home/joey/python/code/t1.py
1 init~~~~~~~~~~~~~~
2 enter~~~~~~~~~~~~~~
3 enter with ~~~~~~~~~~~~~~
4 exit with ~~~~~~~~~~~~~~
5  exit~~~~~~~~~~~~~

Process finished with exit code 0
```

```python
import time
class Point:

    def __init__(self):
        print(1, "init~~~~~~~~~~~~~~")

    def __enter__(self):
        print(2, "enter~~~~~~~~~~~~~~")
        return self
    #  exc_type 异常类型
    #  exc_val 异常值
    #  traceback
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        print(5, " exit~~~~~~~~~~~~~")
        return  1 # return 等效为true，则压制异常，如果等效为false，则抛出异常

# with 语法：
a = Point()
with a as b:   # b = a.__enter__() 返回值是自己的self
    print(1, a)
    print(2, b)
    print(a == b)
    print(a is b)
    print(id(a),id(b))
    print("================================")
    1 / 0

#
# f = open('t1.py')
# with f as f1:
#     print(f == f1)
#     print(f is f1)
#     print(id(f),id(f1))
#
#
# with open('t2.py') as f:
#     print()


```
##  **计时**

```python
import time
import datetime
from functools import wraps,update_wrapper

class Timeit:

    def __init__(self,fn):
        self._fn = fn

    def __enter__(self):
        self.start = datetime.datetime.now()
        #return self._fn
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (datetime.datetime.now()-self.start).total_seconds()
        print("{} took {}s. in dec".format(self._fn.__name__, delta))

    def __call__(self, *args, **kwargs):
        #return self._fn(*args, **kwargs)
        start = datetime.datetime.now()
        ret = self._fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print("{} took {}s. in timeit()".format(self._fn.__name__, delta))
        return ret


def timeit(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start = datetime.datetime.now()
        ret = fn(*args,**kwargs)
        delta = (datetime.datetime.now()-start).total_seconds()
        print("{} took {}s. in timeit()".format(fn.__name__, delta))
        return ret
    return wrapper


@timeit
def add(x,y):
    time.sleep(3)
    return x+ y


with Timeit(add) as timeinstance:
    timeinstance(4,5)

add(4, 5)

Timeit(add)(5,6)
```


```python

import time
import datetime
from functools import wraps,update_wrapper

class Timeit:

    def __init__(self,fn):
        self._fn = fn

    def __enter__(self):
        self.start = datetime.datetime.now()
        #return self._fn
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        delta = (datetime.datetime.now()-self.start).total_seconds()
        print("{} took {}s. in dec".format(self._fn.__name__, delta))

    def __call__(self, *args, **kwargs):
        #return self._fn(*args, **kwargs)
        start = datetime.datetime.now()
        ret = self._fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print("{} took {}s. in timeit()".format(self._fn.__name__, delta))
        return ret


@Timeit# add =Timeit(add) s
def add(x,y):
    time.sleep(3)
    return x+ y

print(add(4, 5))


```


```python
import time
import datetime
from functools import wraps,update_wrapper

class Timeit:

    def __init__(self,fn):
        self._fn = fn

    def __call__(self, *args, **kwargs):
        #return self._fn(*args, **kwargs)
        start = datetime.datetime.now()
        ret = self._fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print("{} took {}s. in timeit()".format(self._fn.__name__, delta))
        return ret


@Timeit# add =Timeit(add)
def add(x,y):
    time.sleep(3)
    return x+ y

print(add(4, 5))

print(callable(add) ,callable(Timeit),callable(Timeit(add)))

callable ----就是是标识符后面可以添加()
 1　函数可调用　
 ２　类本身就是可以实例化，当然可调用
 ３　Timeit(add)　实例有__call__方法，也可以掉用
```


```python


import time
import datetime
from functools import wraps,update_wrapper

class Timeit:
    ''' i am Timite '''
    def __init__(self,fn):
        self._fn = fn
        # self.__doc__ = fn.__doc__
        # self.__name__ = fn.__name__
        #update_wrapper(self,fn)
        wraps(fn)(self)

    def __call__(self, *args, **kwargs):
        #return self._fn(*args, **kwargs)
        start = datetime.datetime.now()
        ret = self._fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print("{} took {}s. in timeit()".format(self._fn.__name__, delta))
        return ret




@Timeit# add =Timeit(add)
def add(x,y):
    '''thi is add function '''
    time.sleep(1)
    return x+ y

print(add(4, 5))
print(add.__doc__)
print(add.__name__)
print(callable(add) ,callable(Timeit),callable(Timeit(add)))


```

## **上下文应用场景**

1. 增强功能
在代码执行的前后增加代码,以增强其功能。类似装饰器的功能。
2. 资源管理
打开了资源需要关闭,例如文件对象、网络连接、数据库连接等
3. 权限验证
在执行代码之前,做权限的验证,在 __enter__ 中处理


## **contextlib.contextmanager**

```python
import contextlib
@contextlib.contextmanager
def foo(): #
  print('enter')
  # 相当于__enter__()
  yield # yield 5,yield的值只能有一个,作为__enter__方法的返回值
  print('exit') # 相当于__exit__()
with foo() as f:
  raise Exception()
print(f)
```

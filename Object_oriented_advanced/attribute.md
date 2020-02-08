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
分类:
创建、初始化与销毁
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

    __hash__ = None

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
如果一个实例可以用 bool 函数 要用__bool__如果没有__bool__方法，就判断 __len__方法

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

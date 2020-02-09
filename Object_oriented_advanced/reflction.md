# **Reflction**

- __概述__
  - 运行时,区别于编译时,指的是程序被加载到内存中执行的时候。
  - 反射,reflection,指的是运行时获取类型定义信息。
  - 一个对象能够在运行时,像照镜子一样,反射出其类型信息。
  - 简单说,在Python中,能够通过一个对象,找出其type、class、attribute或method的能力,称为反射或者自
省。具有反射能力的函数有 __type()__、__isinstance()__、__callable()__、__dir()__、__getattr()__等



```python



class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return "Point({}, {})".format(self.x, self.y)
    #
    # __repr__ = __str__
    #
    # def show(self):
    #     print(self.x, self.y)


setattr(Point, 'XYZ', 100)

if not hasattr(Point, 'show'):
    setattr(Point, 'show', lambda self : print(self.x, self.y))

print(Point.__dict__)
p = Point(4, 5)
print(p.x)
p.show()
Point.show(p)
print(getattr(p, "y", 2000))
# if not hasattr(p,'z'):
#     print(getattr(p, "z",3000))

setattr(p,'z',100)

print(p.__dict__)

if not hasattr(p, 'showy'):
    setattr(p, 'showy', lambda :print('123'))

if not hasattr(p, 'showx'):
    setattr(p, 'showx', lambda self :print(self.x))


p.showy()　#<function <lambda> at 0x000001C4EF954D38>　没有参数的函数
p.showx(p) #<function <lambda> at 0x000001C4EF954D38>
p.show()　＃<bound method <lambda> of <__main__.Point object at 0x000001C4EF95EE08>>

print(p.__dict__)
print(p.show)
print(p.showy)

'''
实例自己的方法，参数手动添加<function <lambda> at 0x000001C4EF954D38>
类的实例方法会自动添加self实例　<bound method <lambda> of <__main__.Point object at 0x000001C4EF95EE08>>
'''

```
## **动态增加属性**

- getattr(object,  通过name返回object的属性值。当属性不存在,将使用default返回,如果没有
name[, default]) default,则抛出AttributeError。name必须为字符串
- setattr(object,name, value) object的属性存在,则覆盖,不存在,新增
- hasattr(object,name) 判断对象是否有这个名字的属性,name必须为字符串

```python
'''
getattr(object,  通过name返回object的属性值。当属性不存在,将使用default返回,如果没有
name[, default]) default,则抛出AttributeError。name必须为字符串
setattr(object,name, value) object的属性存在,则覆盖,不存在,新增
hasattr(object,name) 判断对象是否有这个名字的属性,name必须为字符串
'''

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    __repr__ = __str__
    #
    # def show(self):
    #     print(self.x, self.y)


print(Point.__dict__)
p1 = Point(4, 5)
p2 = Point(10,10)
setattr(Point,"__add__",lambda self,other:self.__class__(self.x + self.x ,self.y + self.y))
print(p1 + p2)




```

## **分发器**

```python
class Dispatcher():

    def __init__(self):
        pass


    def reg(self,name,fn):
        setattr(self,name,fn)

    def run(self):
        while True:
            cmd = input(">>>>>>>>>").strip()
            if cmd == "quit":
                break
            getattr(self,cmd,lambda :print("unknow cmmand {}".format(cmd)))

d = Dispatcher()
d.reg("ls",lambda :print("ls command"))
d.run()
```



## 　**魔术函数**
- 查找属性顺序为: instance.__dict__ --> instance.__class__.__dict__ --> 继承的祖先类(直到object)的__dict__ ---找不到--> 调用__getattr__()

- 实例通过.点号设置属性,例如 self.x = x 属性赋值,就会调用 __setattr__() ,属性要加到实例的 __dict__中,就需要自己完成。



```python

'''
__getattr__(self, item):# 实例访问属的时候，找不到的时候AttributeError，如果有此方法怎访问__getattr__

实例访问方属性顺序。实例－类－夫类-object　如果还没有找到，则查看__getattr__有没有配置，有的话，怎访问次方法，没有怎报AttributeError

__setattr__(self, key, value):　只要对实例进行属性设置　就必须先调用__setattr__函数.连初始化函数__init__ 也一样
'''
class Base:
    n = 10


class Point(Base):

    z = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    __repr__ = __str__

    def show(self):
        print(self.x, self.y,self.z)

    def __getattr__(self, item):# 实例访问属的时候，找不到的时候AttributeError，如果有此方法怎访问__getattr__
        print("item ~~~~~~~~~~~~~~~~~", item)
        print(type(item))
        self.__dict__[item] = 1000
        return self.__dict__[item]

    def __setattr__(self, key, value):
        #print("__setattr__ ~~~~~~~~~~~~~~~~~", key, value)
        #super().__setattr__(key, value)
        self.__dict__[key] =value
        #setattr(self,key,value) #这个就是调用__setattr__的函数，这样就造成无限递归

    def __delattr__(self, item):
        print("del attribute {}".format(item))


p1 = Point(4,5)

# print(p1.x , p1.y,p1.z,p1.n)
# print(p1.xxx)
# print(p1.__dict__)
#=============================================

print(p1.__dict__)
print(p1.x, "++++++++++++++++++++")
del p1.x
del Point.z
del p1.z


```

## **__getattribute__**

```python



class Base:
    n = 10


class Point(Base):

    z = 6
    d = {}

    def __init__(self, x, y):
         self.x = x
         self.y = y
        # self.__dict__['x'] = x
        # self.__dict__['y'] = x

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    __repr__ = __str__

    def show(self):
        print(self.x, self.y,self.z)

    def __getattr__(self, item):# 实例访问属的时候，找不到的时候AttributeError，如果有此方法怎访问__getattr__
        return self.d[item]

    def __setattr__(self, key, value):
        print("__setattr__ ~~~~~~~~~~~~~~~~~", key, value)
        self.__dict__[key] = value

    def __delattr__(self, item):
        print("del attribute {}".format(item))

    def __getattribute__(self, item):#实例访问属性第一道关卡 也就是
        print(item,type(item))
        #return super().__getattribute__(item)
        raise AttributeError("aaaaaaaaa") # 返回AttributeError 直接调用__getattr__


p1 = Point(4,5)

print(p1.__dict__)

```




1. __getattr__() 当通过搜索实例、实例的类及祖先类查不到属性,就会调用此方法
2. __setattr__() 通过 . 访问实例属性,进行增加、修改都要调用它
3. __delattr__() 当通过实例来删除属性时调用此方法
4. __getattribute__ 实例所有的属性调用都从这个方法开始

- 属性查找顺序:
 - 实例调用__getattribute__() --> instance.__dict__ --> instance.__class__.__dict__ --> 继承的祖先类(直到object)的__dict__ --> 调用__getattr__()

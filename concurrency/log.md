# **<font color=Red>Loggin**


## **<font color=Red>log**


```python

from logging import root,Logger
import logging

FORMAT = '%(asctime)s %(name)s\t(process)s %(processName)s\t%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

'''
logging.getLogger('l1')
如果logger对象'l5' ，如果l5对象存在，则返回，如果不存在，则创造新对象
'''
l5 = logging.getLogger('l1')  # 如果logger对象'l5' ，如果l5对象存在，则返回，如果不存在，则创造新对象
c = logging.getLogger(__name__)  # 自定义的ｌｏｇｇｅｒ　来自父列

print(c.name, type(c), c.parent, c.parent is root)
c1 = logging.getLogger(__name__ + '.child')  # 设置子类
print(c1.name, type(c), c1.parent, c1.parent is c)

c2 = logging.getLogger('c1.c1')  # 设置子类

'''
每一个logger实例,都有一个等效的level。
logger对象可以在创建后动态的修改自己的level。
等效level决定着logger实例能输出什么级别信息
'''

root = logging.getLogger()
root.level = 20  # 级别调整
root.info('test')

'''
那消息的级别大于或者等于前logger的有效级别去比较，才有资格输出
当前logger有效级别，如果没有设置，则继承其父的级别
log1.setLevel(logging.NOTSET+1) 设置有效级别
'''

log1 = logging.getLogger(__name__)
log1.info('test info') # 那消息的级别大于或者等于前logger的有效级别去比较，才有资格输出
log1.debug('test debug')

print(log1.level, log1.getEffectiveLevel())

log1.setLevel(50)
print(log1.level)

log1.info('test info')
log1.debug('test debug')

logging.info('root info input')


```

## **<font color=Red>handle**

```python
'''
andler 控制日志信息的输出目的地,可以是控制台、文件。
  可以单独设置level
  可以单独设置格式
  可以设置过滤器
  Handler类层次Handler
    StreamHandler # 不指定使用sys.stderr
    FileHandler # 文件
    _StderrHandler # 标准输出
    NullHandler # 什么都不做
'''
#from logging import root,Logger
import logging
import sys

FORMAT = '%(asctime)s %(name)s\t(process)s %(processName)s\t%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO,filename='root.log')


'''
动态加载ｈａｎｄｌｅ
h= logging.FileHandler('root.log')
root.addHandler(h)
print(root.handlers)

'''
root = logging.getLogger()

print(root.handlers)
h= logging.FileHandler('root.log')
root.addHandler(h)
print(root.handlers)

h1= logging.FileHandler('root1.log')
root.addHandler(h1)
print(root.handlers)

st = logging.StreamHandler(sys.stdout)


logging.info('test info')

--------------

#from logging import root,Logger
import logging
import sys

FORMAT = '%(asctime)s %(name)s\t(process)s %(processName)s\t%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO,filename='root.log')


'''
子logging 继承ｈａｎｄｌｅｓ

'''
root = logging.getLogger()

st = logging.StreamHandler(sys.stdout)
root.addHandler(st)

logging.info('test info')
#
log1 = logging.getLogger('hello')
print("in log1", log1.handlers)
log1.info('test info ini log1')




```



- logger实例
- 如果不设置level,则初始level为0。
- 如果设置了level,就优先使用自己的level,否则,继承最近的祖先的level。
信息是否能够从该logger实例上输出,就是要看当前函数的level是否大于等于logger的有效level,否则输出不了。

**<font color=Red>继承关系及信息传递**

1. 每一个Logger实例的level如同入口,让水流进来,如果这个门槛太高,信息就进不来。例如
log3.warning('log3'),如果log3定义的级别高,就不会有信息通过log3

2.如果level没有设置,就用父logger的,如果父logger的level没有设置,继续找父的父的,最终可以找到root
上,如果root设置了就用它的,如果root没有设置,root的默认值是WARNING

 **<font color=Red>h消息传递流程**

1. 如果消息在某一个logger对象上产生,这个logger就是 **<font color=Red>当前logger**,首先消息level要和当前logger的
EffectiveLevel比较,如果低于当前logger的EffectiveLevel,则流程结束;否则生成log记录。
2. 日志记录会交给当前logger的所有handler处理,记录还要和每一个handler的级别分别比较,低的不处
理,否则按照handler输出日志记录。
3. 当前logger的所有handler处理完后,就要看自己的propagate属性,如果是True表示向父logger传递这
个日志记录,否则到此流程结束。
4. 如果日志记录传递到了父logger,不需要和父logger的level比较,而是直接交给父的所有handler,父
logger成为当前logger。重复2、3步骤,直到当前logger的父logger是None退出,也就是说当前logger
最后一般是root logger(是否能到root logger要看中间的logger是否允许propagate)。
logger实例初始的propagate属性为True,即允许向父logger传递消息
logging.basicConfig函数
如果root没有handler,就默认创建一个StreamHandler,如果设置了filename,就创建一个FileHandler。
如果设置了format参数,就会用它生成一个Formatter对象,否则会生成缺省Formatter,并把这个
formatter加入到刚才创建的handler上,然后把这些handler加入到root.handlers列表上。level是设置给root logger的。
如果root.handlers列表不为空,logging.basicConfig的调用什么都不做。

 ## **<font color=Red>设置自定义日志格式**

```python
from logging import root,Logger
import logging

FORMAT = '%(asctime)s %(name)s\t(process)s %(processName)s\t%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
log1 =logging.getLogger('log1')
log1.propagate = False
import sys

h = logging.StreamHandler(sys.stdout)
h1=logging.FileHandler('/home/{}.log'.format(__name__))
log1.addHandler(h)
log1.addHandler(h1)
print(log1.handlers[0].formatter)

f = logging.Formatter("*********%(message)s*****") # 自己设置日志格式
h.setFormatter(f)
print(log1.handlers[0])

print(log1.handlers[0].formatter._fmt)

log1.info("test info string")



from logging import root,Logger
import logging

FORMAT = 'root\t [%(name)s]\t(process)s %(processName)s\t%(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
log1 =logging.getLogger('log1')
log1.propagate = True
import sys

h = logging.StreamHandler(sys.stdout)
#h1=logging.FileHandler('python.log'.format(__name__))
log1.addHandler(h)
#print(log1.handlers[0].formatter)

f = logging.Formatter("logg1\t[%(name)s] %(message)s*****") # 自己设置日志格式
h.setFormatter(f)
#print(log1.handlers[0])

#print(log1.handlers[0].formatter._fmt)

#log1.info("test info string")

filter = logging.Filter('log1')
h.addFilter(filter)
log2 = logging.getLogger('log1.log2')

log2.info("test2 info string")
print(filter,filter.name,filter.nlen) #name制指定过滤的字符串，nlen是的长度


```

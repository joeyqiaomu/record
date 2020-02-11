# **<font color=Red>内建函数**


## **<font color=Red>枚举 enumerate(seq, start=0)**

- 迭代一个序列,返回索引数字和元素构成的二元组
- start表示索引开始的数字,默认是0

```python
for x in enumerate([2,4,6,8]):
    print(x)
for x in enumerate("abcde"):
    print(x,end=" ")

```

## **<font color=Red>迭代器和取元素 iter(iterable)、next(iterator[, default])**

- iter将一个可迭代对象封装成一个迭代器
- next对一个迭代器取下一个元素。如果全部元素都取过了,再次next会抛StopIteration异常

```python
it = iter(range(5))
  next(it)
it = reversed([1,3,5])
  next(it)
```
## **<font color=Red>拉链函数zip(*iterables)**

- 像拉链一样,把多个可迭代对象合并在一起,返回一个迭代器
- 将每次从不同对象中取到的元素 **<font color=Red>合并成一个元组</frot>**

```python

list(zip(range(10),range(10)))
list(zip(range(10),range(10),range(5),range(10)))
dict(zip(range(10),range(10)))
{str(x):y for x,y in zip(range(10),range(10))}

```

## **<font color=Red>sorted(iterable[, key][, reverse]) 排序**



- **<font color=Red>立即返回一个新的列表</frot>**,默认升序
- reverse是反转

```python
sorted([1, 3, 5])
sorted([1, 3, 5], reverse=True)
sorted({'c':1, 'b':2, 'a':1})
'''
为了解决不同呢类型之间排序问题，提供一个参数，ｋｅｙ是函数，这个函数可以把元素强制类型转换为你制定的类型
，但是转换的结果　只是用来比较大小，不改变最后生成的列表的元素本身
'''

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '1']
sorted(l1,key=str)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## **<font color=Red> 翻转 reversed(seq)**

- **<font color=green>有序的序列　返回一个翻转元素的迭代器</frot>**


```python


list(reversed("13579"))

{ reversed((2, 4)) } # 有几个元素?

for x in reversed(['c','b','a']):
　　　print(x)
reversed(sorted({1, 5, 9}))

for x in (i**2 for i in reversed(sorted({1,5,9}))):
    print(x)


```


## **<font color=Red> 翻转 迭代器和取元素 iter(iterable)、next(iterator[, default])**
- iter将一个可迭代对象封装成一个迭代器
- next对一个迭代器取下一个元素。如果全部元素都取过了,再次next会抛StopIteration异常

```python
it = iter(range(5))
next(it)
it = reversed([1,3,5])
next(it)
```

## **<font color=Red> 可迭代对象**
- 可迭代对象
  - 能够通过迭代一次次返回不同的元素的对象。
   - 所谓相同,不是指值是否相同,而是元素在容器中是否是同一个,例如列表中值可以重复的,
['a', 'a'],虽然这个列表有2个元素,值一样,但是两个'a'是不同的元素,因为有不同的索引
  - 可以迭代,但是未必有序,未必可索引
  - 可迭代对象有:list、tuple、string、bytes、bytearray、range对象、set、dict、生成器、迭代器
等
  - 可以使用成员操作符in、not in,in本质上对于线性结构就是在遍历对象,非线性结构求hash

3 in range(10)
3 in (x for x in range(10))
3 in {x:y for x,y in zip(range(4),range(4,10))} #效率最高

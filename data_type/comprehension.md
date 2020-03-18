# **<font color=Red>列表解析式**

```
语法
   [返回值 for 元素 in 可迭代对象 if 条件]
   使用中括号[],内部是for循环,if条件语句可选
   返回一个新的列表
列表解析式是一种语法糖
    编译器会优化,不会因为简写而影响效率,反而因优化提高了效率
    减少程序员工作量,减少出错
    简化了代码,但可读性增强


    l1 = list(range(10))
    l2 = []
    for i in l1:
      l2.append((i+1)**2)
      print(l2)
列表解析式
    l2 = [(i+1)**2 for i in range(10)]
    print(l2)
    print(type(l2)
```
```python
'''
合适下面的情况，没有else的情况
'''
lst4 = []
for i in range(30):
    if i % 2 ==0:
        if i % 3 == 0:
            lst4.append(i)


```

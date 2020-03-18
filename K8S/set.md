# **<font color=Red> Set**

- 约定
- set 翻译为集合
- collection 翻译为集合类型,是一个大概念
- set 的元素的集合 <font color=Red>**可变的 无序的 不重复 </font>

## **set的元素要求必须可以hash**
- 目前学过的不可hash的类型有list、set,dict
- 元素不可以使用索引
-  set可以迭代

## **set定义 初始化**
- set() -> new empty set object
- set(iterable) -> new set object
```
s1 = set()
s2 = set(range(5))
s3 = set(list(range(10)))
s4 = {} # ?
s5 = {9,10,11} # set
s6 = {(1,2),3,'a'}
s7 = {[1],(1,),1} # ?
```
## **set和线性结构**
- 线性结构的查询时间复杂度是O(n),即随着数据规模的增大而增加耗时
- set、dict等结构,内部使用hash值作为key,时间复杂度可以做到O(1),查询时间和数据规模无关

- 可hash
  - 数值型int、float、complex
  - 布尔型True、False
  - 字符串string、bytes
  - tuple
  - None
 - 上都是不可变类型,是可哈希类型,hashable
 - <font color=Red> set的元素必须是可hash的 </font>

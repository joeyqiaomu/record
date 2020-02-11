# **<font color=Red>lambda**

- 使用lambda关键字定义匿名函数,格式为 **<font color=Red>lambda [参数列表]: 表达式**
- 参数列表不需要小括号。无参就不写参数
- 冒号用来分割参数列表和表达式部分
- **<font color=Red>不需要使用return。表达式的值,就是匿名函数的返回值。表达式中不能出现等号</frot>**
- lambda表达式(匿名函数)只能写在一行上,也称为单行函数
匿名函数往往用在为高阶函数传参时,使用lambda表达式,往往能简化代码
- **<font color=Red>表达式绝对不能有等号出现**

```python

lambda x:x+1
<function __main__.<lambda>>
(lambda x,y:x+y)(4,5)

(lambda x,y:100)(4,5) #恒定返回１００
def foo(x,y):
  return １００

 (lambda :100)(）＃无参表达式

# 返回常量的函数
print((lambda :0)())
# 加法匿名函数,带缺省值
print((lambda x, y=3: x + y)(5))
print((lambda x, y=3: x + y)(5, 6))
# keyword-only参数
print((lambda x, *, y=30: x + y)(5))
print((lambda x, *, y=30: x + y)(5, y=10))
# 可变参数
print((lambda *args: (x for x in args))(*range(5)))
print((lambda *args: [x+1 for x in args])(*range(5)))
print((lambda *args: {x%2 for x in args})(*range(5)))
[x for x in (lambda *args: map(lambda x: x+1, args))(*range(5))]
#
高阶函数
[x for x in (lambda *args: map(lambda x: (x+1,args), args))(*range(5))]

{x:y for x,y in (lambda *args: map(lambda x: (x+1,args), args))(*range(5))}



```

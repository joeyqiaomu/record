# **异常的捕获**

- 程序会在异常抛出的地方中断执行,如果不捕获,就会提前结束程序(其实是终止当前线程的执行)


```
try:
    待捕获异常的代码块
except [异常类型]:
    异常的处理代码块

```
## **异常类及继承层次**

```
# Python异常的继承
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
+-- RuntimeError
|
+-- RecursionError
+-- MemoryError
+-- NameError
+-- StopIteration
+-- StopAsyncIteration
+-- ArithmeticError
| +-- FloatingPointError
| +-- OverflowError
| +-- ZeroDivisionError
+-- LookupError
| +-- IndexError
| +-- KeyError
+-- SyntaxError
+-- OSError
| +-- BlockingIOError
| +-- ChildProcessError
| +-- ConnectionError
| | +-- BrokenPipeError
| | +-- ConnectionAbortedError
| | +-- ConnectionRefusedError
| | +-- ConnectionResetError
| +-- FileExistsError
| +-- FileNotFoundError
| +-- InterruptedError
| +-- IsADirectoryError
```

## **try**

```
try的工作原理
1、如果try中语句执行时发生异常,搜索except子句,并执行第一个匹配该异常的except子句
2、如果try中语句执行时发生异常,却没有匹配的except子句,异常将被递交到外层的try,如果外层不处理这个异
常,异常将继续向外层传递。如果都不处理该异常,则会传递到最外层,如果还没有处理,就终止异常所在的线程
3、如果在try执行时没有发生异常,如有else子句,可执行else子句中的语句
4、无论try中是否发生异常,finally子句最终都会执行
```

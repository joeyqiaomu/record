

```
一，使用系统自带的pdb模块进行单步调试
所谓的单步调试，就是指的是每次执行一句Python语句。 单步执行代码,通过在用户终端命令 python -m pdb xxx.py 启动脚本，进入单步执行模式。注意在终端命令输入的前面，会有这样一个显示：

(Pdb)，这就表示进入了pdb命令调试。然后输入下面的命令即可。

注意：我们经常看见在python代码中会有 import pdb 这样的语句，但是这样的“单步执行模式”，是不需要在代码里面添加这句话的，当然天街也可以。

 pdb命令行：

    1）进入命令行Debug模式，python -m pdb xxx.py  这个格式是固定的

          之所以可以这样做，主要是因为pdb.py 可以被当做一个脚本执行。

    2）h：（help）帮助

    3）w：（where）打印当前执行堆栈

    4）d：（down）执行跳转到在当前堆栈的深一层（个人没觉得有什么用处）

    5）u：（up）执行跳转到当前堆栈的上一层

    6）b：（break）添加断点

                 b 列出当前所有断点，和断点执行到统计次数

                 b line_number：当前脚本的line_no行添加断点

                 b filename:line_number：脚本filename的line_no行添加断点

                 b function：在函数function的第一条可执行语句处添加断点

    7）tbreak：（temporary break）临时断点

                 在第一次执行到这个断点之后，就自动删除这个断点，用法和b一样

    8）cl：（clear）清除断点

                cl 清除所有断点

                cl bpnumber1 bpnumber2... 清除断点号为bpnumber1,bpnumber2...的断点

                cl line_number 清除当前脚本line_number行的断点

                cl filename:line_number 清除脚本filename的line_number行的断点

    9）disable：停用断点，参数为bpnumber，和cl的区别是，断点依然存在，只是不启用

    10）enable：激活断点，参数为bpnumber(即哪一个断点，1，2，3，4......)

    11）s：（step）执行下一条命令

                如果本句是函数调用，则s会执行到函数的第一句

    12）n：（next）执行下一条语句

                如果本句是函数调用，则执行函数，接着执行当前执行语句的下一条。

    13）r：（return）执行当前运行函数到结束

    14）c：（continue）继续执行，直到遇到下一条断点，这个比较重要，常常和断点结合起来使用。

    15）l：（list）列出源码

                 l 列出当前执行语句周围11条代码

                 l first 列出first行周围11条代码

                 l first second 列出first--second范围的代码，如果second<first，second将被解析为行数

    16）a：（args）列出当前执行函数的函数

    17）p expression：（print）输出expression的值

           比如：(Pdb) p 1+2

                   这里会打印出 3

          再比如：(Pdb) p c    #这里用来查看某个变量c的值

    18）pp expression：好看一点的p expression

    19）run：重新启动debug，相当于restart

    20）q：（quit）退出debug

    21）j lineno：（jump）设置下条执行的语句函数

                只能在堆栈的最底层跳转，向后重新执行，向前可直接执行到行号

    22）unt：（until）执行到下一行（跳出循环），或者当前堆栈结束

    23）condition bpnumber conditon，给断点设置条件，当参数condition返回True的时候bpnumber断点有效，否则bpnumber断点无效

注意：

    1：直接输入Enter，会执行上一条命令；

    2：输入PDB不认识的命令，PDB会把他当做Python语句在当前环境下执行；

    3：常用的命令有，（6）（8）（9）（10）（11）（12）（13）（14）（15）（16）（17）（18）（19）（20）

二、使用set_trace()设置断点
pdb单步执行太麻烦了，所以第二种方法是import pdb 之后，直接在代码里需要调试的地方放一个pdb.set_trace()，就可以设置一个断点， 程序会在pdb.set_trace()暂停并进入pdb调试环境，可以用pdb 变量名查看变量，或者c继续运行。

如下代码：
————————————————
版权声明：本文为CSDN博主「LoveMIss-Y」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_27825451/article/details/85600992
```

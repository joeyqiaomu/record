# **<font color=Red> grep**

```

文本处理三剑客
		  grep：文本过滤工具(模式。pattern)
			 grep： 基本正则表达式 -E -F
			 egrep：扩展正则表达式。-G -F
			 fgrep : 不启用正则表达式
		  sed ：steam editor 流编辑器，文本编辑工具
		  awk ： Linux上实现为gawk 文本报告生成器（格式化文本）

		正则表达式：regual expression RGGEXP
			有一类特殊字符以及文本字符所编写的模式，其中有些字符不表示其字母意义，而是用于标识控制或者通配功能
			分两类：
				 基本正则表达式：BRE
				 扩展正则表达式：ERE
			元字符：\(hello[[:space:]]\+\)\+
		grep:golbal serach regular expression and print out the line
			作用：文本搜索工具，根据用户指定的“模式（过滤条件）” 对目标文本进行行进行匹配检查：打印匹配到的行
			模式：有正则表达式的云字符以及文本字符所有编写的过滤的条件

			  正则表达式引擎：
			  grep [OPTIONS] PATTERN [FILE...]
			  grep [OPTIONS] [-e PATTERN | -f FILE] [FILE...]
			  option:
				--auto
				-o : 只显示匹配的字符串本身
				-i --ignore-case :igore-case 忽略大小写
				-v --invert-match，显示不能被模式匹配
				-q --quiet, --silent 静默模式
				-E 支持使用扩展的正则表达式云字符

				-A #：after
				-B #：before
				-C #: context 前后各#行
				grep -C 2  "root" /etc/passwd


				(1) 字符匹配
					. : 匹配任意单个字符 : grep "r..t" /etc/passwd
					[]：指定范围内的任意单个字符 --grep "r[o]\{2\}t" /etc/passwd ,grep "r[[:alpha:]][[:alpha:]]t" /etc/passwd
					[^]指定范围外的任意单个字符
					[[:digit:]] [[:lower:]][:upper:]] [[:alnum:]][[:alpht:]]

					\d --[0-9]匹配1位数字
					\D --[^0-9]匹配1位非数字
					\s 匹配1位空白字符,包括换行符、制表符、空格 [ \f\r\n\t\v]
					\S 匹配1位非空白字符
					\w 匹配[a-zA-Z0-9_],包括中文的字
					\W 匹配\w之外的字符

				(2) 匹配次数 ,用到指定其出现字符的字符的后面，用于显示其前面字符的次数
					* 匹配其前面的字符任意此 0,1,多次 {0,}---贪婪模式
					  例子：.*匹配任意长度的字符
					\?: 匹配其前面的字符0或1次   -至多一次
					\+:  匹配其前面的字符1或多次 --至少一次
					\{m\}：匹配其前面的字符1次
					\{m,n\}：匹配其前面的至少m次至多n次
						\{,n\}：匹配其前面的至多n次
						\{m,\}：匹配其前面的至少m次
				(3) 位置锚定
					 行首锚定：^ 用于模式的最左侧
					 行尾锚定：$ 用于模式的最右侧
					 ^pattern$: 匹配整行
						^$ 空白行：
						^[[:space:]]*$ 空行或包含空白字符的行
					单词：非特殊字符组成的连续的字符（字符串）都成为单词
					\< or \b ,词首锚定 用于单词模式的左作词
					\> or \b ,词尾锚定  用于单词模式的右作词
					\B 不匹配单词的边界：
					     t\B 包含t的单词但是不以t结尾的t字符,例如write
                         \Bb不以b开头的含有b的单词,例如able
					\< pattern\> :匹配完整的单词
					grep -v ".*/bin/bash$" /etc/passwd
					grep  "^[[:digit:]]\{2,3\}$" /etc/passwd
					grep  "\<[0-9]\{2,3\}\>" /etc/passwd
					   至少一个空白字符开头，且后面非空白字符的行
					grep  "^[[:space:]]\+[^[:space:]]" /etc/grub2.cfg

				(4) 分组以及引用
					\( \):将一个或多个字符捆绑在一起，当做一个整体来进行处理：
					note：分组括号中的模式匹配到的内容会被正则表达式引擎自动记录于内部的变量中，这些变量为
					\1 ,模式从左侧起，第一个左括号以及与之匹配的右括号之间的模式所匹配的字符
					\2 ,模式从左侧起，第二个左括号以及与之匹配的右括号之间的模式所匹配的字符
					\3 ,模式从左侧起，第三个左括号以及与之匹配的右括号之间的模式所匹配的字符
					。。。。。。。。。。。。。。。。。
					he loves his lover
					he likes his lover
					she likes her liker
					she loves her liker
					grep "\(l..e\)*\1"
					grep "^\(r..t\).*\1" /etc/passwd
				后向引用：引用前面的分组括号中的模式所匹配到的字符：
		egrep：
			支持扩展的正则表达式实现类似grep文本过滤功能 -E
			NAME
		   grep, egrep, fgrep - print lines matching a pattern

			SYNOPSIS
				   grep [OPTIONS] PATTERN [FILE...]
				   grep [OPTIONS] [-e PATTERN | -f FILE] [FILE...]
			选项：
				-l -o -v -a -A -B -C
				-G
			   (1) 字符匹配
					. : 匹配任意单个字符 --匹配除换行符外任意要给字符
					[]：指定范围内的任意单个字符
					[^]: 指定范围外的任意单个字符
					[[:digit:]] [[:lower:]][:upper:]] [[:alnum:]][[:alpht:]]
					\d --[0-9]匹配1位数字
					\D --[^0-9]匹配1位非数字
					\s 匹配1位空白字符,包括换行符、制表符、空格 [ \f\r\n\t\v]
					\S 匹配1位非空白字符
					\w 匹配[a-zA-Z0-9_],包括中文的字
					\W 匹配\w之外的字符
				(2) 匹配次数 ,用到指定其出现字符的字符的后面，用于显示其前面字符的次数
					* 匹配其前面的字符任意此 0,1,多次 {0,}---贪婪模式
					 .*匹配任意长度的字符
					?: 匹配其前面的字符0或1次
					+:  匹配其前面的字符1或多次
					{m}：匹配其前面的字符1次
					{m,n}：匹配其前面的至少m次至多n次
						{,n}：匹配其前面的至多n次
						{m,}：匹配其前面的至少m次
				(3) 位置锚定
					 行首锚定：^
					 行尾锚定：$
					 ^pattern$:
						^[[:space:]]*$ 空行或包含空白字符的行
					单词：非特殊字符组成的连续的字符（字符串）都成为单词
					\< or \b ,词首锚定 用于单词模式的左作词
					\> or \b ,词尾锚定  用于单词模式的右作词
					\< pattern\> :匹配完整的单词
					\B 不匹配单词的边界：
					     t\B 包含t的单词但是不以t结尾的t字符,例如write
                         \Bb不以b开头的含有b的单词,例如able

				(4) 分组以及引用
					( ):将一个或多个字符捆绑在一起，当做一个整体来进行处理：
					note：分组括号中的模式匹配到的内容会被正则表达式引擎自动记录于内部的变量中，这些变量为
					\1 ,模式从左侧起，第一个左括号以及与之匹配的右括号之间的模式所匹配的字符
					\2 ,模式从左侧起，第二个左括号以及与之匹配的右括号之间的模式所匹配的字符
					\3 ,模式从左侧起，第三个左括号以及与之匹配的右括号之间的模式所匹配的字符
					。。。。。。。。。。。。。。。。。

					或
					  a|b ：a或b
						C|cat :C 或者cat

					(?:w|f)ood    如果仅仅为了改变优先级,就不需要捕获分组
					(?:w|f)(oo)d

					(?<name>exp)(?'name'exp)命名分组捕获,但是可以通过name访问分组Python语法必须是(?P<name>exp)
					(?<head>\D+)(?<age>\d+)(?<tail>\D*) --age 18.
				零宽断言
					(?=exp)	  断言exp 一定要出现匹配的右边出现呢 也就是说后面一定有一个 exp前缀 	f(?=oo) 匹配的是f但是f后面一定有oo出现,但是匹配的f，断言没有出现group
					(?<=exp)  断言exp 一定要出现匹配的左边出现呢 也就是说前面一定有一个 exp前缀 	(?<=f)ood ，(?<=t)ook分别匹配 ood ook 但是条件是前一定有f t出现
			   负向零宽断言
					(?!exp)	 断言exp 一定不要出现匹配的右边出现呢 也就是说后面一定有一个 exp前缀
					(?<!exp) 断言exp 一定不要出现匹配的左边出现呢 也就是说前面一定有一个 exp前缀

				断言会不会捕获呢?也就是断言占不占分组号呢?
			    断言不占分组号。断言如同条件,只是要求匹配必须满足断言的条件。

				(5) 贪婪和非贪婪
				    代码 说明
					举例
					*? 匹配任意次,但尽可能少重复
					+? 匹配至少1次,,但尽可能少重复
					?? 匹配0次或1次,,但尽可能少重复
					{n,}? 匹配至少n次,但尽可能少重复
					{n,m}? 匹配至少n次,至多m次,但尽可能少重复

				grep -E "^(root|centos|joey)\>" /etc/passwd
				cat /etc/rc.d/init.d/functions | grep -E -o "^[_[:alnum:]]+\(\)"
				echo /etc/sysconfig/ | grep -E -o "[^/]+/?$"
				grep -E "^([^:]+\>).*\1$" /etc/passwd
				grep -E "^([^:]+\>).*\1$" /etc/passwd

		fgrep ： 不支持正则表达式云字符
			当作不需要用到云字符去编写模式时，使用fgrep性能更好

```
# **<font color=Red> sed**

```
sed命令：
	stream editor 流编辑器，行
	awk：文本格式化工具 报告生成器
	工作原理：
	    (1):从文本文件中一次读入一行，复制一份，放入sed的自己模式空间中（加工车间）
		  处理后 在标准输出的输出结果，默认是对文本文件每一行作处理

		(2):从文本文件中一次读入一行，复制一份，放入sed的内存中sed的模式空间（加工车间）,然后在模式中进行模式匹配，
		   如果匹配了，   默认要输出至标准输出 - 然后再做一次edit edit结果可以定义输出，也可以不输出
		   如果没有匹配。 默认要输出至标准输出(也可以定义不输出)

	pattern space ---内存空间中的模式空间
	hold space  ----内存空间中的hold空间
    sed - stream editor for filtering and transforming text
      SYNOPSIS
       sed [OPTION]... 'script' [input-file]...
            script ：
				    地址定界编辑命令
			OPTIONS:
			    -n ：不输出模式空间中内容至屏幕
				-e ：script, --expression=script：多点编辑，
				   sed -e 's@^#[[:space:]]*\+@@g' -e '/^UUID/d' /etc/fstab
				-f ： /path/to/sed_srcipt_file
				        每行一个编辑命令：
				-r ：支持扩展的正则表达式：
				-i[SUFFIX], --in-place[=SUFFIX]：直接编辑原文件

            地址定界：
			     (1)：空地址，对全文进行处理
				 (2)：单地址：
						   #：指定行
						   /pattern/:被此地址匹配到的每一行
				 (3)：地址范围：
						   #,#
						   # ,+#:相对地址加法
						   #, /pat1/ 第一次匹配的中间所有行
						   /pat1/, /pat2/ 匹配第一次pat1到pat2
						   $最后一行
				 (4)：步进：~
				          1~2:所有基数上
				          2~2:所有偶数行
			编辑命令：
			    d: 删除 sed "1,5d" /etc/fstab set "/^#/d" /etc/fstab sed '1~2d' /etc/fstab
				    sed -n '/^#/d' /etc/fstab ：-n 不输出的标准输出，那么没有匹配都会禁止输出，匹配到的做d删除动作 结果是什么都没有输出到屏幕
					sed '1~2d' /etc/fstab 显示偶数行
				p: 显示模式空间中的内容
				        sed  '1~2p' /etc/fstab     1 默认显示      2 编辑后再显示，就是奇数行显示2此
						sed  -n '1~2p' /etc/fstab  1 关闭默认显示，2 编辑显示 就是只显示奇数行
				a: append 在匹配行后面追加 text ，支持使用\n多行插件
                     sed '3a \new line' /etc/fstab
                     sed '3i \new line\nnew new line ' /etc/fstab
                     sed '/^UUID/i \new line\nanother line' /etc/fstab
				i:   insert 在匹配行前面追加 text ，支持使用\n多行插件
				c：\test :把匹配到的行替换此处指定的文本“text”；整行替换
				    sed '/^UUID/c \new line' /etc/fstab
				w path/to/someifle,保存模式匹配的内容保存到文件 path/to/someifle
				    sed '/^[^#]/w /tmp/fstab.new' /etc/fstab
                    sed -n '/^[^#]/w /tmp/fstab.new' /etc/fstab
				r: 读取指定文件的内容至当前文件被模式匹配到的行后面：文件合并
				     sed '3r /etc/issue' /etc/fstab
				=：为模式匹配到的行打印行号
				   sed '/^UUID/=' /etc/fstab
				!:条件取反 地址定界!编辑命令
				   sed '/^#/!d' /etc/fstab

				   地址定界！编辑命令
				s///：查找替换，其分隔符可自动指定，常用有s@@@s
				    替换标记
					    g：全局提花
						p：显示替换成功的行
						w/path/to/somefile：将替换成功的结果保存至指定文件中
				sed 's@^[[:space:]]\+@@'  /etc/grub2.cfg
				sed -e 's@^#[[:space:]]*\+@@g' -e '/^UUID/d' /etc/fstab
				echo "/var/log/messages/" | sed  's@[^/]\+/\?$@@'
				echo "/var/log/messages/" | sed -r 's@[^/]+/?$@@'


			高级命令：
			    h  ： 把模式空间（pattern space）中的内容覆盖到hold space保存空间中
				H  :  把模式空间中的内容追加到hold space保存空间中

				g  ： 把hold space保存空间中的内容覆盖到模式空间中
				G  :  把hold space保存空间中的内容追加到模式空互换覆盖到hold space保存空间中

				x  :  把模式空间（pattern space）中的内容互换到hold space保存空间中
				n  ： 覆盖读取匹配到的行的下一行至模式空间中
				N  ： 追加读取匹配到的行的下一行至模式空间中
				d  :  删除模式空间的行
				D  :  删除多行模式空间中的所有行

				sed -n 'n;p' /etc/fatab    ---显示偶数行
				sed '1!G;h;$!d' /etc/fstab----逆序显示文件内容
				  1! 不是第一行
				  $! 不是最后一行
				sed '$!d' FILE          ----- 取出最后一行
				   sed '$!d' /etc/fstab
				sed '$!N;$!D' FILE         ---取出文件最后两行
				   sed '$!N;$!D' /etc/fstab
				sed '/^$/d;G' FILE         ---删除原有的所有空白行，而后为所有的非空白行后
				    添加一个空白行
				sed 'n;d' FILE 显示奇数行
				sed 'G' FILE，在原有每行后方再添加一个空白行
```

# **<font color=Red> awk**
```
文本处理工具：
     grep egrep fgrep 文本过滤工具 PATTERN
	 sed：行编辑器
	      模式空间，保持空间
	 awk：报告生成器，格式化文本输出

awk ：报表生成器，格式化文本输出：aho，weinberger，kernighan
gawk
    基本用法： gawk [options] 'program' FILE ....
	        program:PATTERN{ACTION STATEMENT}
			     语句之间用分号分隔
	             print,printf
			options选项：
			    -F: 指明输入用到字段分隔符
                -v: var=value ：自定义变量：
			处理文本：
			    1 一次读取一行文本，根据分隔符(默认是空白字符)，切割成N份，每一片的分隔的内容
				  都放在awk的内建的变量中($1 $2 $3.....),整行放在$0中，
				2 然后对于每一个分隔的内容，再做判断做出处理
				3 awk的循环是在字段间完成遍历操作($1 $2 $3.....)
				tail -5 /etc/fstab | awk '{print $2,$4 }'
            1 输出
			print items,items
                (1)逗号分隔符
                (2)输出的各item可以字符串，也可以是数值，当前记录的字段，变量或awk的表达式
                (3)如省略item 相当于print $0	awk '{print $0}'
				awk '{print}'
				awk '{print $1,$2...}'
				awk '{print "hello",$2,$4 }'
				awk '{print "hello:"$2,$4 }'
            2 变量：
                   (2.1) 内建变量
				       (1)FS: input field sepeatror   输入字段分隔符,默认为空白字符
					      awk -v FS=':' '{print $1}' /etc/passwd=== awk -F: '{print $1}' /etc/passwd
					   (2)OFS: OUTPUT field sepeatror 输入字段分隔符,默认为空白字符
					      awk -v FS=':' -v OFS=':' '{print $1,$3,$7}' /etc/passwd
						  awk -v FS=":" -v OFS=":" '{print $1,$3,$7}' /etc/passwd
					   (3)RS:input record sepeatror   输入的换行符，文本输入的行分隔符
					   (4)ORS:outpur record sepeatror 输处的换行符  文本输处的行分隔符
					   awk -v RS=' ' '{print}' /etc/passwd

					   (5)NF：number of field 每一行字段数量
					       awk '{print NF}'  /etc/fstab
						   awk'{print $NF}'  /etc/fstab
					   (6)NR number of record 文件的行数
					      awk '{print NR}'  /etc/fstab /etc/issue
						  awk '{print FNR}'  /etc/fstab /etc/issue
 					   (7)FNR: 各个文件分别的行数
					    awk '{print FNR ,$2}' /etc/fstab /etc/issue
					   (8) FILENAME 当前文件名：
					  	   awk '{print FILENAME}'  /etc/fstab /etc/issue
					   (9)  ARGC:  命令行参数的个数 awk 'BEGIN{print ARGC}'  /etc/fstab /etc/issue
					   (10) ARGV： 数组,保存的时命令行所给定的各参数     awk 'BEGIN{print ARGV[0]}'  /etc/fstab /etc/issue
					   [root@test ~]#awk 'BEGIN{print ARGV[0]}'  /etc/fstab /etc/issue
							awk
							[root@test ~]#awk 'BEGIN{print ARGV[1]}'  /etc/fstab /etc/issue
							/etc/fstab
							[root@test ~]#awk 'BEGIN{print ARGV[4]}'  /etc/fstab /etc/issue

							[root@test ~]#awk 'BEGIN{print ARGV[2]}'  /etc/fstab /etc/issue
							/etc/issue
							[root@test ~]#
				 (2.2) 自定义变量：
                        变量区分字符大小写
				      1 -v var=value
					  2 在pragram 中直接定义
					   awk 'BEGIN{test="jhlll hhh";print test}'
					   #awk -v test='hello gawk' 'BEGIN{test1="hello gwak1";print test,test1}' /etc/issue

				3 printf命令：
				     格式化输出：printf FORMAT,item1,item2,.....

					  (1): FORAMT  必须给出
					  (2): 不会自动唤行，需要显示给出行控制符，\n
					  (3): FORMAT中给出需要分别为后面的每一个item指定一个格式化符号：

					  格式符：
					     %c :    显示字符串的ASCII码
						 $d $i:  显示十进制整数
						 %e %E:  科学技术法数值显示
							 %f   :  显示为浮点数
							 %g $G : 以科学技术法或浮点形式显示数值
						 %s :    显示字符串
						 %u ：   无符号整数
						 %% ：   显示%自身
						修饰符：
						  #[.#]:第一数字控制显示的宽度；第二个#表示小数点后的精度
						       %3.1f
							-：左对齐
							+：显示数值的符号
						  awk -F: '{printf "Username:%18s, UID:%d\n",$1,$3}' /etc/passwd
						  awk -F: '{printf "Username:%-15s, UID:%d\n",$1,$3}' /etc/passw
						  awk -F: '{printf "Username:%s, UID:%d\n",$1,$3}' /etc/passwd
						  awk -F: '{printf "username : %-20s  UUID : %d\n",$1,$3}' /etc/passwd
                 4 操作符：
				        4.1 算术操作符:
							   +-*%
							   +x：转换为数值
						4.2 字符串操作符：没有符号的操作符，字符串链接
						4.3 复制操作符
							   =，+=，-=，/=,
							   ++ --
					    4.4 比较操作符：or
								> >= < <= != ==
						4.5 模式匹配符：
							   ~ 是否匹配
							   ！~：是否不匹配
						4.6 逻辑操作符：
								&& || !
			            4.7函数调用：
						   fucntion_name(arg1,arg2......)
					    4.8条件表达式：
						   selector[条件表达式]?if-true-expression:if-false-expression
						   awk -F: '{$3>=1000?usertype="commom uer":usertype="system uesr or sysuer";printf "%15s:%-s\n",$1,usertype}' /etc/passwd
                5 PATTERN
				    1  Empty:空模式，匹配每一行
					2  /regular expression/: 仅处理能够被此模式匹配的行--正则表达式
					     awk '/UUID/{print $1}' /etc/fstab
						 awk '!/UUID/{print $1}' /etc/fstab

				    3 relational expression ：关系表达式：结果有"真" 有"假"：结果为"真"才会被处理：
				        真：结果为非0值 非空字符串
						wk -F: '$3>=1000{print $1,$3}' /etc/passwd
						wk -F: '$3>=1000{print $1,$3}' /etc/passwd

						awk -F: '$NF=="/bin/bash"{print $1,$NF}' /etc/passwd
						awk -F: '$NF~/bash$/{print $1,$NF}' /etc/passwd
				   4 Line Ranges:行范围
				       不支持直接给出数字的模式
				      awk -F: '/root/,/gdm/{print $1}' /etc/passwd
					  awk -F: '/^r/,/^q/{print $1}' /etc/passwd
					  awk -F: '(NR>=2&&NR<=10){print $1}' /etc/passwd

				   5 BEGIN/END模式：
						BEGIN{}:仅在开始处理文件中文本之前 执行一次程序
						END {} :仅在文本处理处理完成之后执行一次

				       awk -F: 'BEGIN{print "   username           uuid\n -------------------------------"}{printf "%15s %5s\n",$1,$3}' /etc/passwd
					   awk -F: 'BEGIN{print "   username           uuid\n -------------------------------"}{printf "%15s %5s\n",$1,$3}END{print "===============================\n END"}' /etc/passwd
               6 常用action：
					  1 expressions: 比较表达式等
					  2 control statements：if while等
					  3 compound statements：组合语句：
					  4 input statemenets
					  5 output statements
			   7 控制语句：
			      if(condition){statements}
				  if(condition){statements} else {statemenets}

                  while (condition){statements}
                  do {statements}while (condition)
                  for (expr1;expr2;expr3){statemenets}

                   break,continue,
				   delete array[index]
				   delete array
				   exit {statements}

				  7.1 if-else:
				      if(condition){statemenets}
					  if(condition){statements} else {statemenets}
						awk -F: '{if($3>=1000) print $1,$3}' /etc/passwd
						awk -F: '{if($3>=1000) printf "comom user%s\n", $1 }' /etc/passwd
						awk -F: '{if($3>=1000) {printf "comom user%s\n", $1} else {printf "system user:%s\n",$1} }' /etc/passwd

				       使用场景：对awk取得的整行或某一个字段做条件判断：
				       awk -F: '{if($NF=="/bin/bash") print $1}' /etc/passwd
					   awk '{if(NF>5) print}' /etc/fstab
					   df -h | awk -F% '/^\/dev/{print $1}'| awk '{if($NF>=15) print $1}'
					   df -h | awk -F% '/^\/dev\/sda+/{print $1}' | awk '{if($NF>=16) print $1}'

				 7.2  while (condition){statements}
                      使用场景： 对一样内琢个字段一类似处理使用，对数组的各元素琢一处理是使用：

					  awk '/^[[:space:]]*linux16/{i=1;while(i<=NF){print $i,length($i);i++}}' /etc/grub2.cfg

					  awk '/^[[:space:]]*linux16/{i=1;while(i<=NF){if(length($i)>=7) {print $i,length($i)};i++}}' /etc/grub2.cfg
			     7.3  do-while 循环 ：至少执行一次
			          do {statements} while (condition)
			     7.4 for 循环：
				      for (expr1;expr2;expr3){statemenets}
			          for (variable assignment;condition;iteration process) {statements}
					  awk '/^[[:space:]]*linux16/{for(i=1;i<+NF;i++) {print $i,length($i)}} ' /etc/grub2.cfg

					  特殊用法：能够遍历数组的元素：
					      语法for(var in array){for-body}===var是数组的下标
				 7.5: switch语句：
				      switch（expression）{case VALUE1 or /regexp/:statement;case VALUE2 or /regexp/:statement;....default:statement}
			     7.6:break 和 continue
				        break[n]
						continue
				 7.7 next;
				     能提前结束本行处理，直接进入下一行
				     awk -F: '{if($3%2!=0)next;print $1,$3}' /etc/passwd
		 8，ARRAY数组：
		    关联数组：array[index-expression]
			      index-expression
				      1  可使用任意字符串：字符串使用双引号
					  2  如果某数组元素事先不存在，在引用是，awk会自动创建此元素，并将其值初始化为“空串”
					     如要判断数组中是是否存在，要使用"index in array"

						 weekdays["mon"]="monday"
						 如要遍历数组每一个数组
						    for(var in array){araay[var]} var是数组的索引
						    注意var会遍历array的每个索引或者下标值
						  awk 'BEGIN{weekdays["mon"]="Monday";weekdays["tue"]="Tuesday";for(i in weekdays){print weekdays[i]}}'

						  状态统计：
						      netstat -tan | awk '/^tcp\>/ {state[$NF]++}END{for (i in state){print i,state[i]}}'

							  awk '{ip[$1]++}END{ for(i in ip) {print i,ip[i]}}' /var/log/httpd/access_log
							  练习：统计/etc/fstab文件中每一个文件系统类型出现的次数
							       awk '/^UUID/{fs[$3]++}END{for(i in fs){print i ,fs[i]}}' /etc/fstab
							  练习：统计指定文件中每一个单词出现的次数
							      awk '{for(i=1;i<=NF;i++){count[$i]++}}END{for(i in count){print i,count[i]}}' /etc/fstab
	   9 函数：
	      9.1 内置函数：
		      数值处理
			     rand():返回0和1之间的数值
				 length([s]):返回字符串的长度
				 sub（r,s,[t]） :以r表示的模式，来查找t所表示的字符串中的匹配的内容，并将其第一此出现替换为s所表示的内容
				 gsub（r,s,[t]） :以r表示的模式，来查找t所表示的字符串中的匹配的内容，并将其所有出现替换为s所表示的内容
				 split(s,a,[,r]) :以r为分隔符切割字符s，并将切割后的结果保存至a所表示的数值中:
				 netstat -tan | awk '/^tcp\>/{split($5,ip,":");count[ip[1]]++}END{for(i in count){print i ,count[i]}}'
          9.2 自定义函数
		  《sed and awk.

```

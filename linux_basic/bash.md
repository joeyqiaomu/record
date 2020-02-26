

# **<font color=Red> bash**
```


bash 脚本编程之算术运算
   算术运行格式：
    (1):let var=算术运行表达式
	    echo $var
	(2) VAR= [算术表达式]       echo "$[$num1+$num3]"
	(3) VAR= $((（算术表达式]))  echo "$(($num1+$num3))"
	(4) VAR = $(expr $num1+$num )  echo  "$(expr $num1 + $num3)"
	注意：乘法符号在有些场景中需要使用转义符
	练习：
	   写一个脚本，完成如下功能
	   添加三个，求此三个用户的UID之后
文件查找：
  locate ，find
  locate:
	  依赖于事先构建好的索引库
		 系统自动实现(周期性任务)
		 手动更新数据库(updatedb)---很耗费资源
	  工作特性：
		 查找速度快：
		 迷糊查找：
		 非实时查找：

		  locate [OPTION]... PATTERN..
		  -b ：只匹配路径中基名
		  -c ：统计出共有多少个符合条件的文件
		  -r ：BRE
	find：
	    实时查找工具：通过遍历指定路劲起始下文件系统层级结构完文件
		工作特性
			精确查找：
			实时查找
			查找速度慢
	用法：
    find [options][查找起始路径][查找条件][处理动作]
	find [-H] [-L] [-P] [-D debugopts] [-Olevel] [path...] [expression]
	     查找起始路径：指定目标起始路径 默认当前目录
		 查找条件： 指定查找标准，可根据文件名，大小，类型，从属关系，权限等标准进行
		        默认为找出指定路径下的所有文件
		处理动作： 对符合查找的条件的文件做出的操作，例如删除等操作，默认为输出至标准输出
	超找条件：
	     表达式：选项+测试
         根据文件名：
			patter（支持glob分隔的通配符）
			  * ？[],[^]
			 -name patter 精确匹配
			 -iname patter 忽略大小写的查找
			 find /etc -name "passwd"
			 find /etc -iname "passwd"
			 find /etc -name "passwd??"
			 -regex pattern :基于正则表达式模式进行查找，但是匹配是整个路劲，而非其名
		根据文件从属文件：
		    -user USERNAME。查找属主指定用户的所有的文件
			-group GROUPNAME。查找属组指定组的所有的文件
			-uid UID ：查找指定的UID的所有的文件
			-uid GID ：查找指定的GID的所有的文件
			-nouser  ：查找没有属主的文件
			-nogrou  : 查找没有属组的文件
			find /etc -user joey
			find /etc -nogrou
		根据文件的类型查找
		  -type
		    f:普通文件
			d:目录文件
			l:符号链接文件
			b：块设备文件
			c：字符文件
			p：管道文件
			s: 套接字文件

			find /dev -type d
			find /dev -type l
		组合测试：
		   find /tmp -nouser -o -type f -ls
		   与：-a 默认组合逻辑
		   或：-o 组合逻辑
		   非：-not ，i

		   find /tmp -not -user root -a -not -iname "*fstab*"
		   find /tmp -not (-user root -o -not -iname "*fstab*"\) -ls
		 根据文件大小查找
		    -site[+|-] #UNIT
			    常用[K M G ]
				#UNIT(#-1,#]
				-#UNIT(0,#-1]
				+#UNIT(#,oo]
	     根据时间出查找：
		    以天为单位
			   atime [+|-]#
				     #:[#,#+1) 大于#天，少于#+1天
					 -#:[0.#) #天内
					 +#:(OO.#-1]
					     +#   |   # |   -#    |
					--------------------------
					find /tmp -atime +7 7天之前访问
					find /tmp -atime 7
					find /tmp -mtime -1 1天之内修改的文件
			   -mtime
			   -ctime
            以分钟时间查找
			   -amin
			   -mmin
			   -cmin

		根据用户权限
		   -perm[/|-] mode 权限
		        mode，精确权限匹配（find ./ 664 -ls）
		        /mode 任何一类用户（u，g，o）的权限的任何一位（r，w，x）符合条件
				    find ./ -perm /664 -ls）
					find ./ -not -perm -222 -ls
                    9为权限之间存在“或”的关系
				-mode 每一类用户（u，g，o）的权限的每一位（r，w，x）符合条件
				    9为权限之间存在“与”的关系
				    find ./ -664 -ls）
					find ./ -perm -222 -ls
					find ./ -not -perm -222 -ls
		处理动作：
			-print：输出至标准输出 默认动作
			-ls  ： 类似对查找的文件执行ls-l 命令，输出文件的详细信息
			-delete 删除超找的文件
			-fls : /path/to/files 把查找到的所有文件的长格式保存至指定文件中
			-ok command {}\; 对查找的每一个文件执行有command表示的命令,每次操作有用户的确认
			-exec command {} \; :对查找的每一个文件执行有command表示的命令 每次操作不需要确认
				{} 表示引用

			find ./ -nouser -a -nogroup -ok  chown root:root {} \;
			find ./ -nouser -a -nogroup -exec chown root:root {} \;

			[root@centos7 test]# find ./ -perm /002 -exec mv {} {}.danger \;
				[root@centos7 test]# ls -l
				total 0
				-r--r--rw-. 1 root root 0 Jun  8 21:21 a.danger
				-rwxrwxrwx. 1 root root 0 Jun  8 21:21 b.danger
				-rw-rw-rw-. 1 root root 0 Jun  8 21:21 c.danger
				-rw-r--r--. 1 root root 0 Jun  8 21:21 d
				-rw-r--r--. 1 root root 0 Jun  8 21:21 e
				-rwxrwxrwx. 1 root root 0 Jun  8 21:21 f.danger
				-rw-r--r--. 1 root root 0 Jun  8 21:21 g
				[root@centos7 test]#
		注意：find传递查找到的文件路径至后面的命令时，是先查找所有符合的文件路径，并一次性
		  传递给后面的命令，但是有一些命令不能接受过长的参数，此时命令执行会失败，
		  另一种方式可规避此问题
		      find | xargs comand

		课外作业，学习xargs命令用法
bash 脚本编程：
    #!/bin/bash
	# description :
	# version :
	# author: jerry<........@.......>
	# date:

	let VAR =$num1 op $ num2
	var = $[expr]
	var = $((expression))
	var =$(expr argu1 argu2 argu3)
	变量：
	   局部变量
	   本地变量
	   环境变量

	   位置参数变量
	   特殊变量：

	增强型
     VAR=$[$VAR+1]
	 let var+=1
	 let var++
	 +=.-=,*=,/=,%=
	 VAR=$[$VAR-1]
	 let var-=1
	 let var--


	grep "^[[:space:]]*$" /etc/rc.d/init.d/functions |wc -l

	条件测试：
	    判断某需求是否满足，需要有测试机制来实现
		如何编写测试表达式以实现所需的测试：
		   1 执行命令，并利用命令状态返回值来判断
		         0：执行
				 1-255：失败
				 who | grep "^root\>" &> /dev/null
		   2 没有命令表达：
			    1 test expression :
				2 [ exprssion ] :
				3 [[ expression ]]:
				   注意expression两端必须有空格
				例如：判断2 和 3谁大
				test 2 -gt 3
                [ 2 -gt 3 ]
                [[ 2 -gt 3 ]]

	 bash 测试类型：
	   1 数值测试
	      -eq ：等于 （equal）
		  -nq : 不等于 (no equal)
		  -gt : 大于
		  -ge ：大于等于
		  -lt ：是否小于
		  -le ：是否小于等于
	   2 字符串测试----字符串比较双中括号[[]]
	     == ：是否等于
		    [[ tom == "$name" ]]
		 > :  是否大于
		 < :  是否小于
		 != :  是否不等于
		 =~: 左侧字符串是否能够被右侧的PATTERN所匹配；

		 -z “string”：判断string字符串是否为空，空位真，不空为假
		 -n " string": 判断string字符串是否b不为空，不空位真，空为假
		   注意：
		       1 字符串要用加引号
			   2 要用[[ ]]

	    3 文件测试
		   存在性测试
		       -a FILE
			   -e FILE
			      文件存在性测试，存在为真，不存在为假
			存在性及类型测试：
			    -b FILE -是否存在并且为 快设备 文件；
				-c FILE -是否存在并且为 字符设备 文件；
				-d FILE -是否存在并且为 是否文件目录 文件；
				-f FILE -是否存在并且为 普通 文件；
				-h or -L FILE -是否存在并且为 符号链接 文件；
				-p FILE -是否存在并且为 管道 文件；
				-S FILE -是否存在并且为 套接字 文件；
			文件权限测试：
			   -r FIEL ，是否存在并且并且对当前用户 可读
			   -w FIEL ，是否存在并且并且对当前用户 可写
			   -x FIEL ，是否存在并且并且对当前用户 可执行
			 特殊权限测试：
			   -g FIEL ，是否存在并且并且拥有SGID
			   -u FIEL ，是否存在并且并且拥有SUID
			   -k FIEL ，是否存在并且并且拥有Sticky
			  文件是否有内容
			    -s FIEL ，是否有内容，有为真，没有为假
			文件时间戳测试：
			    -N file ： 文件自从上一次操作后是否被修改；
			从属关系：
			    -O FILE 当前用户是否为文件属主
				-G FILE 当前用户是否为文件属组
			双目测试：
			    FILE1 -ef FILE2 :FILE1与FILE2是否指向同一个文件系统的相同inode得到硬链接
				FILE1 -nt FILE2 :FILE1是否新于FILE2  new then
				FILE1 -ot FILE2 :FILE1是否旧于FILE2  old then
		组合测试条件：
		    逻辑预算：
			    第一种方式：
				   COMMAND1&&COMMAND2
				   COMMAND1||COMMAND2
				   !COMMAND
				 第二种方式： 、
				    [ expression1 -a expression2 ]
					[ expression1 -o expression2 ]
					![ expression1 ]

	脚本的状态返回值：
	    默认是脚本中执行的最后一个条件的状态返回值
		   自定义状态推出吗：
		        exit[n] : n 为自己制定的状态吗
				    注意：shell进程遇到exit是，即会终止，因此，脚本执行即为结束
	向脚本传递参数：
        位置参数变量
        myscript.sh argu1 argu2
             引用方式：$1 $2 .............${10},
			 轮替：shift #
		特殊变量：
		  $0 , 脚本文件路径本身
		  $# , 参数的个数
		  $* , 所有参数
		  $# , 所有参数


	过程式编程语言的代码执行顺序：
	    顺序执行：琢个运行
		选择执行：

		 单分之：

		 if 测试条件；then
		       代码分之
		 fi

		  双分支：

		  if 测试条件：then
		      条件为真是执行的分支
		  else
		      条件为假时执行的分支
		  fi

		循环执行：

======================================================================
压缩 解压缩：
=======================================================================
    压缩比：时间换空间：
	       CPU的时间-->磁盘空间
	    压缩：
		compress/uncompress ..Z
		gzip/gunzip ...gz
		bzip2/bunzip2 ...bz2
		xz/unxz  ..xz
		归档
		zip/unzip
		tar cpio

		1,gzip
		压缩和解压缩都是删除源文件
		gzip, gunzip, zcat - compress or expand files
		gzip [option] ..FILE....
		   -d: 解压缩，相对于gunzip
		   -#：指定压缩比，默认是6，数值大，压缩比越大，
		   -c：将压缩结果输出至标准输出，且保存源文件
		   gzip -c file > /path/to/somefiel.gz

		2 bzip2
		压缩和解压缩都是删除源文件
		 bzip2/bunzip2/bzcat
		 bzip2 [option] ..FILE....
		   -d: 解压缩，相对于bunzip
		   -#：指定压缩比，默认是6，数值大，压缩比越大，
		   -k：gbzip2 -k file --保留源文件
		3 xz/unxz/xzcat:
		   lzma/unlzma/lzcat
		    xz [option] ..FILE....
			-d: 解压缩，
			-#：指定压缩比，默认是6，数值大，压缩比越大，
		    -k：gbzip2 -k file
		注意：只能压缩文件，不能压缩目录

		归档：tar cpio
		    tar 命令：
			    xz [option] ..FILE....
			    1 创建归档，
				   -c -f /path/to/somefile.tar FILE....FILE [FILE 是文件或者目录]
				   案例：
				   tar -cf docker.tar secing/ volumes/ testing/ build_worksheet/
				2 展开归档
				  -xf  /path/from/somefile.tar
				  -xf  /path/from/somefile.tar -C /path/to/somedir
				  -C  指定展开文件存放的位置(必须存在的目录)
				  案例：
				   tar -xf docker.tar  -C ./docker
				3 查看归档文件的文件列表
				  -tf
				  案例：
				  tar -tf docker.tar
				4归档并压缩
				   -z：gzip2
				     -zcf /path/to/somefile.tar.gz FILE....
					 解压缩并展开归档：-zxf /path/to/somefile.tar.gz-解压缩并展开归档
					 tar -zcf volumes.zip.tar volumes/
					-j：bzip2
					 -jcf /path/to/somefile.tar.bz2 FILE....
					 -jxf /path/to/somefile.tar.bz2 解压缩并展开归档
					 tar -jcf volumes.bz2.tar volumes/
					-J:xzd
					 -Jcf /path/to/somefile.tar.xz FILE....
					 -Jxf /path/to/somefile.tar.xz-解压缩并展开归档
					  tar -Jcf volumes.xz.tar volumes/
			zip: 通用压缩工具(既能归档也能压缩)
			    .zip

=================================================================================================

	bash脚本编程之用户交互：
	    bash -n --检测脚本中语法错误
		bash -x ---调试执行脚本
	用户交互：通过键盘输入数据
	    read [option] ...[name]....
		   -p ''  提示信息
		   -t ''  超时信息

	while condition:do

bash 脚本编程：   ;

     ======================================
	 循环执行：
	   进入条件：条件满足是进入循环
	   退出条件：每一个循环应该有退出条件
	 =================================
	  for while until
	 循环控制语句：
	    continue ：提前结束本轮循环，而直接进入下一轮循环判断
		     while condition1:do
			       CMD1
				   .....
				   if condition2
				       continue
					fi
					CMD2
			 done

		break ：提前结束
	          while condition1:do
			       CMD1
				   .....
				   if condition2
				       continue
					fi
					CMD2
			   done
			   declare -i oddsum=0
			   declare -i i=0
			   declare -i i=1

			   while ture;do
			       let $oddsum+$i
				   let i+=2
				   if [ i -gt 10 ];then
				      break
				    fi
				done

				while ture;do
			       if who | grep "^logstash" >& /dev/null;then
				        break
				    fi
				    sleep 3
				done
				echo " $(date + %F T%) logstah login in"

				until who | grep "^logstash" >& /dev/null;do
				    sleep 3
				done
				echo " $(date + %F T%) logstah login in" >> /tmp/user.log
	  while 循环的特殊用法(遍历文件的行)
             while read varaible;do
			   循环体
			 done < /path/from/somefile
			 依次读取/path/from/somefile文件中的每一行，且将读入的行赋值给variable

			 实例：
			     while read line ;do
						userid=$(echo $line | cut -d: f3)
						username=$(echo $line | cut -d: f1)
						usershell=$(echo $line | cut -d: f7)
						if [ $($userid)%2 -eq 0 ];then
							echo "$userid $username $usershell"
						fi
				  done < /etc/passwd
      for 循环的特殊用法：
            for(( 控制变量初始值);条件表达式;控制变量的修正语句);do
                 循环体
             done
       	控制变量初始值：仅在循环代码开始运行时执行一次
        控制变量的修正语句：每轮循环结束会先进行变量修正运算，而后再做条件判断
	    for ((i=1,i < 10;i++));do
		    循环体
         done
	 LSIT 生成方式：
	     1 直接给出
		 2 整数列表：
		       1a{start..end}
			   seq [OPTION]... LAST
			   seq [OPTION]... FIRST LAST
			   seq [OPTION]... FIRST INCREMENT LAST
	     3 返回列表的命令：
		      ls cat
		 4 通配符：
		     for filename /var/log/*;
		 5 变量引用：
		     $@,$#
	 for :
	 两种格式：
	    (1)遍历列表格式：
		    for variable in LIST;do
			   循环体
			done
	    (2)控制变量：

	=========================================
	IF
	=========================================
	单分支：
		if condition ;then
		   if  ture--分支
		fi
		if多分支语句：
	双分支：
		if condition;then
			 if-ture--分支
		else
			 if-false--分支
		fi
	多分支的if语句
		if conditon1；then
		    条件1为真分支1
		elif condition2；then
			条件2为真分支2
		elif condition3;then
		    条件3为真分支3
		.......
		else condition n ：then
		    所有条件都不满足
		fi
   ===========================
	case
   ===========================
	    case $varaible in
		PAT1)
		     分支1
			 ;;
		PAT2)
		     分支2
			 ;;
        .............
		 *)
		    分支n
			;;
		esac


    函数 function ：
	    过程式编码，代码重用
		  模块化编程
		  结构化编程
		  把一段独立功能的代码当做一个整体，并为之去一个名字，
		   命名的代码段，此即为函数：
		     注意：定义函数的代码不会字段执行，咋调用时执行，所谓调用函数 在代码给定函数名即可
			   函数名出现的任何位置，在代码执行时，都会自动被替换为函数代码

		语法一 ：
		    functin f_name {
			    ....函数...
			}
		语法二 ：
		   f_name {
			    ....函数...
			}
		 函数调用：给函数名；

		函数可以接受参数：
		    传递参数给函数：
			    在函数体当中，可以使用$1 $@...引用传递函数的参数，还可以函数中使用$* or
				     $@传递给我函数所有的参数，$#引用传递给函数的参数的个数
				在调用函数时，在函数名后面空白符分隔给定参数利列表即可，例如，testfunc arg1 arg2 arg3 ...
		递归函数
		    函数直接或间接调用自身
		实例：
		    #/bin/bash
			#


			useradd()
			   {
			      if id $1 &> /dev/null ;then
				     reture 5
				  else
				     useradd $1
					 reval=$?
					 reture $reval
			   }
			   for i in {1..10};do
			       useradd ${1}${i}
				   retval =$?
				   if [ $retval -eq 0 ];then
				       echo "add user ${1}${i} finished"
				    elif [ $retval -eq 0 ] ; then
					      echo "add user ${1}${i} exited"
				    else
					        echo "unknow"
					fi
				 done

	   变量作用域：
            局部变量：作用域是函数生命的周期 在函数结束时被自动销毁
			          定义局部函数： local variable =value1
			本地变量： 作用域是运行的shell进程的生命周期 因此,其作用范围为当前的shell脚本程序文件
			---------------------------
			#/bin/bash
			#

			name=tom
			setname(){
			  local name=jerry
			  echo "function: $name"
			}
			setname
			echo "shell: $name"
			[root@test data]#bash scope.sh
				function: jerry
				shell: tom
			--------------------------
           #/bin/bash
			#

			name=tom
			setname(){
			   name=jerry ----变量没有声明为本地变量，那么函数体name变量和函数外变量name 是同一内存空间
			  echo "function: $name"
			}
			setname
			echo "shell: $name"
			[root@test data]#bash scope.sh
				function: jerry
				shell: jerry
			----------------------------

	递归函数：
	      函数直接或间接调用本身
		  #/bin/bash
			#

			fact () {
			   if [ $1 -eq 0 -o $1 -eq 1 ];then
					echo 1
			   else
					echo $[$1*$(fact $[$1-1])]
			   fi
			}

			fact $1

			#!/bin/bash
			#
			#

			fab() {
			   if [ $1 -eq 1 ];then
				   echo 1
			   elif [ $1 -eq 2 ];then
					echo 1
			   else
					 echo $[$(fab $[$1-1])+$(fab $[$1-2])]
			   fi
			}

			for i in $(seq 1 $1);do
				 fab $i
			done
			---------------------------
			#!/bin/bash
			#
			#

			fab() {
			   if [ $1 -eq 1 ];then
				   echo -n "1 "
			   elif [ $1 -eq 2 ];then
					echo -n "1 "
			   else
					 echo -n "$[$(fab $[$1-1])+$(fab $[$1-2])] "
			   fi
			}

			for i in $(seq 1 $1);do
				 fab $i
			done
			----------------------------------------

数组：
     程序=指令+数据：
	     指令：系统命令 以及各种关键字(if elif else fi while until for 等.....)
		 数据：变量，文件
	 数组：存储多个元素的连续的内存空间
	 变量：存储单个元素的内存空间
	 　　数组名：整个数据只有一个名字
	 　　数组索引：编号从０开始
	 　　　　数组名[索引]
	         ${array_name[Index]}
		  注意，bash-4 及之后的版本，支持自定义索引格式，而不仅仅0.1-----数据格式
		       此类数组称之为“关联数组”
	    declare -a NAME :声明一个索引数组
		declare -A NAME :声明一个关联数组
		    先声明：否则都是索引数组


	   数组中元素的赋值方式：
			 (1) 一次只赋值一个元素
				array-name[index]=value ---animals[0]=pig ,animals[1]=dog
			 (2) 一次赋值全部元素：
				array-name=("value1" "value2" "valu3") === animal=("pig" "dog" "cat")
			 (3)赋值特定元素：
					array-name=([0]="VAL1" [3]="VAL2") --稀疏格式数组
			 (4) read -a array-name：
		     [root@test data]#read -a jianghu
                yuebuqun dongfakdi qianchaodi renwoqing
	   引用数组名的元素：${array-name[INDEX]}
	       cho ${animal[1]}
	   数组的长度（数组中元素的个数）
	       ${#array-name[*]} , ${#array-name[@]}
		   echo ${#jianghu[@]}  --------------------- 数组元素的个数
		   echo ${#jianghu[*]}  --------------------- 数组元素的个数
       引用数组的所有数组元素
	       ${array-name[*]} ----- 所有的数组元素 ----echo ${animal[*]}
		   ${array-name[@]} ----- 所有的数组元素 ----echo ${jianghu[@]}

	   数组元素切片：
		     ${array-name[*]:offset:number}
			    offset  : 要跳过的元素个数
				number  ：要取出的元素个数，不写 就是剩下的所有的元素
				files=(/etc/[Pp]*)
				echo ${files[*]:5:2}
				echo ${files[*]:2}
		向非稀疏格式数组中追加元素：
		    array-name[${#array-name[*]}]
		删除数组中的某元素：
		   unset array-name[INDEX]

		关联数组：
		   declare -A array-name
		   array-name=([index_name1]='value1' [index_name2]="value2")
		   arrname=(["dog"]="dogg" ["cat"]="cat")

		------------------------------------------------------------------------
		#/bin/bash
		#

		declare -a rand
		declare -i max=0

		for in in {0..9} ;do
		   rand[i]=$RANDOM
		   echo ${rand[$i]}
		   if [ ${rand[$i]} -gt $max ] ;then
			   max=${rand[$i]}
		   fi
		done
		echo "MAX : $max"
		-------------------------------------------------------------------------
		   #/bin/bash
		   #

			declare -a files
			files=(/var/log/*.log)
			declare -i lines=0
			for i in $(seq 1 $[${#files[*]}-1]);do
				 if [ $[$i%2] -eq 0 ] ;then
					 let lines += $(wc -l ${files[$i]} | cut -d'' -f1)
				  fi
			done
			echo "lines : $lines"
		-----------------------------------------------------------------------------

	bash的内置字符串处理工具：
	    字符串切片：
		    name=jerry
		    ${var:offer:number}： 取字符串的子串
			echo ${name: -3}：    必须有空白字符
			echo ${name:2}
			[root@test data]#echo ${name:2:-1}
			rr
			[root@test data]#echo ${name:2:1}
			r
			[root@test data]#
		基于模式取子串：
		    $(var#*word): 其中word是指定的分隔符， 功能:自左而右，查找var变量所存储的字符串中， 第一次出现的word分隔符，  删除字符串开头至此分隔符之间的所有字符
			$(var##*word):其中word是指定的分隔符， 功能:自左而右，查找var变量所存储的字符串中， 第后一次出现的word分隔符，删除字符串开头至此分隔符之间的所有字符

				mypath="/etc/init.d/functions"
				[root@centos7 sh]# echo ${mypath##*/}
					 functions
			   [root@centos7 sh]# echo ${mypath#*/}
				etc/init.d/functions
				[root@centos7 sh]#

			$(var%word*): 其中word是指定的分隔符，功能: 自右而左，查找var变量所存储的字符串中，第一次出现的word分隔符，   删除此分隔符至字符串尾部之间的所有字符
			$(var%%word*):其中word是指定的分隔符，功能: 自右而左，查找var变量所存储的字符串中， 第后一次出现的word分隔符，删除此分隔符至字符串尾部之间的所有字符

					[root@centos7 sh]# echo ${mypath%%/*}
					[root@centos7 sh]# echo ${mypath%/*} --/etc/init.d

				url=http://www.magedu.com:80
				${url##*:}  -- 80
				${url%%:*}  --http

		查找替换：
		   ${var/patter/substi} : 查找var所表示的字符串中，第一次被PATTEN所匹配到的字符串，将其替换为substi所表示的字符串：
		   ${var//patter/substi} :查找var所表示的字符串中，所有被PATTEN所匹配到的字符串，将其替换为substi所表示的字符串：

		   ${var/#patter/substi} 查找var所表示的字符串中，行首被PATTEN所匹配到的字符串，将其替换为substi所表示的字符串：
		   ${var/%patter/substi} 查找var所表示的字符串中，行尾被PATTEN所匹配到的字符串，将其替换为substi所表示的字符串：

		   注意 pattern使用glob风格的通配符

		   userinfo="root:x:0:0:root admin:/root:/bin/chroot"
		   [root@test data]#echo ${userinfo/root/ROOT}
				ROOT:x:0:0:root admin:/root:/bin/chroot
				[root@test data]#echo ${userinfo//root/ROOT}
				ROOT:x:0:0:ROOT admin:/ROOT:/bin/chROOT
				[root@test data]#echo ${userinfo/#root/ROOT}
				ROOT:x:0:0:root admin:/root:/bin/chroot
				[root@test data]#echo ${userinfo/%root/ROOT}
				root:x:0:0:root admin:/root:/bin/chROOT

		查找删除：
		   ${var//patter} :查找var所表示的字符串中，所有被PATTEN所匹配到的字符串，并删除
		   ${var/patter} : 查找var所表示的字符串中，第一次PATTEN所匹配到的字符串，并删除

		   ${var/#patter} 查找var所表示的字符串中，行首被PATTEN所匹配到的字符串，并删除：
		   ${var/%patter} 查找var所表示的字符串中，行尾被PATTEN所匹配到的字符串，并删除
		      userinfo="root:x:0:0:root admin:/root:/bin/chroot"
		      [root@test data]#echo ${userinfo//root}
				:x:0:0: admin:/:/bin/ch
				[root@test data]#echo ${userinfo/root}
				:x:0:0:root admin:/root:/bin/chroot
				[root@test data]#echo ${userinfo/#root}
				:x:0:0:root admin:/root:/bin/chroot
				[root@test data]#echo ${userinfo/%root}
				root:x:0:0:root admin:/root:/bin/ch
				[root@test data]#
		字符大小写转换：
           ${var^^} 转换成大写
		   ${var,,}	转换成小写

		变量赋值：
		    ${var:-VALUE} ; 如果var变量为空，或未设置，显示结果为VALUE,否则 则返回var变量的值
			${var:=VALUE} ；如果var变量为空，或未设置，显示结果为VALUE,并且VALUE赋值给var变量 ，否则 则返回var变量的值
			${var:+VALUE}； 如果var变量为非空，返回为VALUE
			${var:?ERROR_INFO}； 如果var变量为非空，或者为设置看，返回为ERROR_INFO为提示，否则，返回var值
	   练习：写一个脚本，完成如下功能
             1 提示用户输入一个可执行命令的名称
             2 获取此命令所依赖到的所有库文件列表
             3 复制命令至某目录(例如/mnt/sysroot 即把此目录当作根)下的对应的额路劲中
                       bash /bin/bash ==> 	/mnt/sysroot/bin/bash
                       useradd /usr/sbin/useradd ==> /mnt/sysroot/usr/bin/useradd
             4 复制此命令依赖到的所有的文件至目标目录下的对应路径下
                /bin64/ld-linux-x864.so.2 ==> /mnt/sysroot/bin64/ld-linux-x864.so.2
             进一步：
              每次复制完成的一命令后，不要退出 而是提示用户继续输入要复制的其他命令，并完成复制如
                 上述的所描述的功能，找到用户输入"quit"为止

		(1) 提示用户输入一个IP地址或网络地址，获取其网络，并扫描其网段：
		  1 #!/bin/bash
			  5 cping(){
			  6     local i=0
			  7     while [$i -le 254 ];do
			  8         if ping -W 1 -c 1 $1.$i &> /dev/null;then
			  9             echo "$1.$i  is up "
			 10         else
			 11             echo "$1,$i is down "
			 12         let i++
			 13     done
			 15 }

		    #!/bin/bash
			#
			----
			#!/bin/bash
				#
				#
				#

				cping(){
					 local i=0
					 while [ $i -le 5 ];do
						  if ping -W 1 -c 1 $1.$i &> /dev/null ;then
								echo "$1.$i is up"
						  else
								echo "$1.$i is down"
						   fi
						   let i++
					 done
				}

				bping(){
					local j=0
					while [ $j -le 5 ];do
						 cping $1.$j
						 let j++
				   done

				}
				aping(){
					local k=0
					while [ $k -le 5 ];do
						 bping $1.$k
						 let k++
				   done

				}

				aping 10
			-----------------------------------------------------------
		提示用户输入一个IP地址或网络地址，获取其网络，并扫描其网段
==================================================================================================
信号捕捉：
     列出信号：
	    trap -l
		kill -l
		man 7 singal
		trap 'command' SIGNALS

		常可以进行捕捉的信号：
		    HUB,INT
在bash中使用ACSII颜色
		echo -e "\033[31m helllo\033[0m"
			 \033[31m hello \033[0m
				  ##m:
					 左侧#：
						  3：前景色
						  4：背景色
						  echo -e "\033[41;31mhelllo\033[0m"
					 右侧：颜色种类
						 1,2,3,4,5，6,7
				  #m ，加粗 闪烁等等
				  \033[3m hello \033[0m
	   多种控制符 可组合使用 批次间用分隔符
		echo -e "\033[42;35;5m hello \033[0m"
		echo -e "\033[41;34;5mhelllo\033[0m"

dialog: 可实现窗口化编程：
    1 各窗体空间使用方式
	2 获取用户选择或键入的内容
	      默认 其输出信息被定向到错误输出流
		    a=$
<高级bash编程指南>
-----------------------------------------------------------------------
	#!/bin/bash
	#
	#

	#trap 'echo "do ni wan er."'  INIT
	#trap 'echo "quit";exit 1' INT

	declare -a hosttmpfiles
	trap 'mytrap' INT

	mytrap(){
		echo "quit"
		rm -f ${hosttmpfiles[@]}
		exit 1
	}

	for i in {1..40}; do
	   tmpfiles=$(mktemp /tmp/ping.XXXXXX)
	   if ping -W 1 -c 1 192..168.187.$i &> /dev/null;then

			   echo "192.168.187.$i is up" | tee $tmpfiles
	   else
			   echo "192.168.187.$i is down" | tee $tmpfiles
		fi
		 hosttmpfiles[${#hosttmpfiles[*]}]=$tmpfiles
	done
	echo
	echo "${hosttmpfiles[@]}"
	rm -f ${hosttmpfiles[@]}

```

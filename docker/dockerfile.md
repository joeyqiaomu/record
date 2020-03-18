
## **<font color=Red>DockerFILE**
```
Dockerfile Instruction 说明：
FROM: 指定基础镜像
      FROM <repository>|<tag>
      FROM <repository>@<digest>
RUN： 构建镜像过程中需要执行的命令。可以有多条。(必须在基础镜像中支持的命令)
-----  在build镜像是用到的命令
        FROM centos:7
        ARG docroot=/var/www/html
        RUN yum makecache && \
        yum -y install httpd php php-mysql && \
        yum clean all && \
        rm -rf /var/cache/yum/*
        CMD ["/usr/sbin/httpd" ,"-DFOREGROUND"]

        (1):docker image build . -t php-httpd:v1.0
        (2):docker run --name web1-d php-httpd:v1.0 /bin/sh

CMD： 添加启动容器时需要执行的命令。多条只有最后一条生效。可以在启动容器时被覆盖和修改。
  ***********CMD 在 container 启动的时候 可以使用run 使用的ENTRYPOINT：同CMD，但这个一定会被执行，不会被覆盖修改。

			   (1):docker image build . -t php-httpd:v1.0
			   (2):docker run --name web1-d php-httpd:v1.0 /bin/sh
				FROM centos:7

					ARG docroot=/var/www/html

					RUN yum makecache && \
					   yum -y install httpd php php-mysql && \
					   yum clean all && \
					   rm -rf /var/cache/yum/*
					CMD ["/usr/sbin/httpd" ,"-DFOREGROUND"]
			--CMD定义的命令，被/bin/bash 取代
			docker run --name web1 -it --rm php-httpd:v1.0 /bin/bash
			---------------------------
			FROM centos:7
			ARG docroot=/var/www/html

			RUN yum makecache && \
			   yum -y install httpd php php-mysql && \
			   yum clean all && \
			   rm -rf /var/cache/yum/*
			ADD phpinfo.php ${docroot}

			EXPOSE 80/tcp
			VOLUME ${docroot}
			#CMD ["/usr/sbin/httpd" ,"-DFOREGROUND"]
			ENTRYPOINT ["/usr/sbin/httpd" ,"-DFOREGROUND"] ---定义ENTRYPOINT

			不能被覆盖
			docker run --name web1 -it --rm php-httpd:v1.1 /bin/bash -- /bin/bash 当作ENTRYPOINT的参数传递
			如要覆盖 再加上--entrypoint "/bin/bash" ，明确指明
			docker run --name web1 -it --rm --entrypoint "/bin/bash" php-httpd:v1.1 entrypoint用法：


LABEL ：为镜像添加对应的数据。 ---第一阶段
MLABELAINTAINER：表明镜像的作者。将被遗弃，被LABEL代替。
EXPOSE：设置对外暴露的端口。
		 EXPOSE 80/tcp
		      docker run --name t1 -it --rm -P myimg:v0.5 /bin/sh
			  [root@node01 build_worksheet]#docker container port t1
					80/tcp -> 0.0.0.0:32768
		    ---------------------------------------------------------------------
			   [root@node01 ap]#cat entrypoint.sh
				#!/bin/bash
				#
				listen_port=${LISTEN_PORT:-80}
				server_name=${SERVER_NAME:-localhost}
				doc_root=${DOC_ROOT:-/var/www/html}

				cat>/etc/httpd/conf.d/myweb.conf << EOF
				Listen $listen_port
				<VirtualHost *:${listen_port}>
				   ServerName "$server_name"
				   DocumentRoot "$doc_root"
				   <Directory "$doc_root">
					 Options none
					 AllowOverride none
					 Require all granted
					</Directory>
				</VirtualHost>
				EOF

				exec "$@" ----执行脚本代替bash的，那么这个替代进程在容器里面就有PID为的1来运行，不依赖于bash
				#/usr/sbin/httpd -DFOREGROUD

				--------------------------------------
				FROM centos:7

					ARG docroot=/var/www/html

					RUN yum makecache && \
					   yum -y install httpd php php-mysql && \
					   yum clean all && \
					   rm -rf /var/cache/yum/*
					ADD phpinfo.php ${docroot}
					ADD entrypoint.sh /bin/

					EXPOSE 80/tcp
					VOLUME ${docroot}
					CMD ["/usr/sbin/httpd" ,"-DFOREGROUND"]    ------运行应用程序 这个CMD会以参数的形式传递给entrypoin脚本 exec "$@" 执行就是CMD的内容
					#ENTRYPOINT ["/usr/sbin/httpd" ,"-DFOREGROUND"]
					ENTRYPOINT ["/bin/entrypoint.sh"]  ----一般都是执行脚本 对应用环境的运行进行配置
					#CMD ["/usr/sbin/httpd" ,"-DFOREGROUND"]
					#ENTRYPOINT ["/bin/bash" ,"-c"]
                 -------------------------------------------------------------------
				 docker run --name web1 -e LISTEN_PORT=8080 -e HI=hello --rm -P php-httpd:v1.4
                     -e 是在运行的容器的时候，把环境变量传递给容器， 那么在run这个镜像产生的容器在bash的中有ISTEN_PORT=8080，HI=hello  这个两个环境变量
					 [root@node01 build_worksheet]#docker exec -it web1 /bin/bash
                     [root@727792647c75 /]# printenv


ENV：设置执行命令时的环境变量，用于为镜像定义所需的环境变量，并可以被dockerfile文件位于其后的其它指令（如 ENV ADD COPY等）所调用
		  调用格式 ${variable_name} or $variable_name
		  在build阶段用到的变量：在dockerfile中使用
			 ENV  <key><value>
			 ENV  <key>=<value>
			    FROM busybox:latest
				ENV webhome="/data/web/html"
				LABEL maintainer="mageedu<magedu@magedu.com>"
				COPY pages  ${webhome}
				ADD  http://nginx.org/download/nginx-1.17.2.tar.gz /tmp
				WORKDIR ${webhome}
				ADD  nginx-1.16.0.tar.gz ./
				VOLUME /data/web/html/
				EXPOSE 80/tcp


ARG：设置只在构建过程中使用的环境变量，构建完成后，将消失
		   --build-arg<varname>=<value>
		   ARG webhome="/data/web/html"  ---可以在build阶段修改变量的值
		   docker image build --build-arg webhome="/webdata/htdocs". -t myimg:v0.8


ADD：将本地文件或目录拷贝到镜像的文件系统中。能解压特定格式文件，能将URL作为要拷贝的文件

		  [root@node01 build_worksheet]#cat Dockerfile
				FROM busybox:latest
				LABEL maintainer="mageedu<magedu@magedu.com>"
				COPY pages  /data/web/html/
				ADD  http://nginx.org/download/nginx-1.17.2.tar.gz /tmp --只是下载不会解压
				ADD  nginx-1.16.0.tar.gz /usr/src/  --文件被解压缩放在目标容器中
			  docker image build . -t myimg:v0.3
			  docker run --name t1 -it --rm myimg:v0.3 /bin/sh
				/ # cd /tmp/
				/tmp # ll
				/bin/sh: ll: not found
				/tmp # ls
				nginx-1.17.2.tar.gz
				/tmp # cd /usr/src/
				/usr/src # ls
				nginx-1.16.0
				/usr/src #
COPY：  将docker宿主机文件或目录[必须是dockerfile的工作目录]拷贝到镜像的文件系统中
VOLUME：添加数据卷 用于在image中创建一个挂载点目录，以挂载docker host上面的卷或其他容器上的卷

USER：指定以哪个用户的名义执行RUN, CMD 和ENTRYPOINT等命令

WORKDIR：设置guest host 工作目录 生效范围从自己的workdir到下一个workdir之间 ，也可以用变量
		  FROM busybox:latest
			LABEL maintainer="mageedu<magedu@magedu.com>"
			COPY pages  /data/web/html/
			ADD  http://nginx.org/download/nginx-1.17.2.tar.gz /tmp
			WORKDIR /usr/
			ADD  nginx-1.16.0.tar.gz src/

		ONBUILD：如果制作的镜像被另一个Dockerfile使用，将在那里被执行Docekrfile命令

		STOPSIGNAL：设置容器退出时发出的关闭信号。

		HEALTHCHECK：设置容器状态检查。
		     HEALTHCHECK CMD command
		     --interval=duration (default:30)
			 --timeout = duration (default:30)
			 --start-period=duration (default:5)
			 --teties=N (default:3)
			HEALTHCHECK --interval=5m --timeout=3s \
			   CMD curl -f http://localhost/ || exit 1

	    HEALTHCHECK --interval=3s --timeout=3s --start-period=2s CMD curl -f http://localhost/ok.html || exit 1

		SHELL：更改执行shell命令的程序。Linux的默认shell是[“/bin/sh”, “-c”]，Windows的是[“cmd”, “/S”, “/C”]。

COPY======================
	  First ：
	  [root@node01 build_worksheet]#ls
		Dockerfile  index.html
		[root@node01 build_worksheet]#cat Dockerfile
		FROM busybox:latest
		LABEL maintainer="mageedu<magedu@magedu.com>"
		COPY index.html /data/web/html/

     [root@node01 build_worksheet]#
	  [root@node01 build_worksheet]#docker image build . -t myimg:v0.1
		Sending build context to Docker daemon  3.072kB
		Step 1/3 : FROM busybox:latest
		 ---> db8ee88ad75f
		Step 2/3 : LABEL maintainer="mageedu<magedu@magedu.com>"
		 ---> Running in 04bb94f08014
		Removing intermediate container 04bb94f08014
		 ---> e714de3a3989
		Step 3/3 : COPY index.html /data/web/html/
		 ---> c812d04ffa44
		Successfully built c812d04ffa44
		Successfully tagged myimg:v0.1
		[root@node01 build_worksheet]#

		[root@node01 build_worksheet]#docker run --name t1 --rm -it myimg:v0.1 /bin/sh
			/ # ls /data/web/html/index.html
			/data/web/html/index.html
			/ # cat  /data/web/html/index.html
			<h1>this is copy </h1>
	 Second ：
		[root@node01 build_worksheet]#cat Dockerfile
			FROM busybox:latest
			LABEL maintainer="mageedu<magedu@magedu.com>"
			COPY pages  /data/web/html/	--复制文件目录
	   [root@node01 build_worksheet]#cat .dockerignore  --设置dockerignore文件，
       pages/test2.html

	   docker image build . -t myimg:v0.2
	   容器中复制主机上的pages目录的文件，但是目录没有复制，2 dockerignore文件中的test2.html也没有复制过程
     			[root@node01 pages]#docker run --name t1 --rm -it myimg:v0.2 /bin/sh
					/ # cd /data/web/html/
					/data/web/html # ls
					index.html  test.html
	创建私有仓库：
	1 打包镜像文件
	docker image save myimg:v0.6 php-httpd:v1.4 -o ./myimage.target
	2 解压缩镜像文件
	docker image load -i myimage.tar
   ==============================================================================
	创建容器：
		基于“镜像文件”，
			镜像文件有默认要运行的程序；

		注意：
			运行的容器内部必须有一个工作前台的运行的进程；
			docker的容器的通常也是仅为运行一个程序；
				要想在容器内运行多个程序，一般需要提供一个管控程序，例如supervised。

		run, create
			--name CT_NAME
			--rm：容器运行终止即自行删除
			--network BRIDGE：让容器加入的网络；
				默认为docker0；

			交互式启动一个容器：
				-i：--interactive，交互式；
				-t：Allocate a pseudo-TTY

				从终端拆除：ctrl+p, ctrl+q

		attach：附加至某运行状态的容器的终端设备；

		exec：让运行中的容器运行一个额外的程序；

		查看：
			logs：Fetch the logs of a container，容器内部程序运行时输出到终端的信息；

			ps：List containers
				-a, --all：列出所有容器；
				--filter, -f：过滤器条件显示
					name=
					status={stopped|running|paused}

			stats：动态方式显示容器的资源占用状态：

			top：Display the running processes of a container


	Docker Hub：
		docker login
		docker logout

		docker push
		docker pull
```

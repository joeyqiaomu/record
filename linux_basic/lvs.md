# **<font color=Red> LVS**
```
iptables/netfilter：
			iptables：用户空间的管理工具；
			netfilter：内核空间上的框架；
				流入：PREROUTING --> INPUT
				流出：OUTPUT --> POSTROUTING
				转发：PREROUTING --> FORWARD --> POSTROUTING

			DNAT：目标地址转换； PREROUTING；
			SNAT：源地址转换；POSTROUTING；

		lvs: ipvsadm/ipvs
			ipvsadm：用户空间的命令行工具，规则管理器，用于管理集群服务及相关的RealServer；
			ipvs：   工作于内核空间的netfilter的INPUT钩子之上的框架；

		lvs集群类型中的术语：
			vs：Virtual Server, Director, Dispatcher, Balancer
			rs：Real Server, upstream server, backend server
			CIP：Client IP, VIP: Virtual serve IP, RIP: Real server IP, DIP: Director IP
			CIP <--> VIP == DIP <--> RIP
			client[CIP]<---> [VIP]virtuall server[DIP]<-----> [RIP]real server

		lvs集群的类型：
			lvs-nat：      修改请求报文的目标IP；多目标IP的DNAT；
			lvs-dr：       操纵封装新的MAC地址；
			lvs-tun：      在原请求IP报文之外新加一个IP首部；
			lvs-fullnat：  修改请求报文的源和目标IP；

			lvs-nat：
				多目标IP的DNAT，通过将请求报文中的目标地址和目标端口修改为某挑出的RS的RIP和PORT实现转发；
```

## **<font color=Red> 算法**
```
[root@computer1 ~]# grep -i 'ip_vs' /boot/config-3.10.0-327.el7.x86_64
CONFIG_IP_VS=m
CONFIG_IP_VS_IPV6=y
# CONFIG_IP_VS_DEBUG is not set
CONFIG_IP_VS_TAB_BITS=12
CONFIG_IP_VS_PROTO_TCP=y
CONFIG_IP_VS_PROTO_UDP=y
CONFIG_IP_VS_PROTO_AH_ESP=y
CONFIG_IP_VS_PROTO_ESP=y
CONFIG_IP_VS_PROTO_AH=y
CONFIG_IP_VS_PROTO_SCTP=y
CONFIG_IP_VS_RR=m
CONFIG_IP_VS_WRR=m
CONFIG_IP_VS_LC=m
CONFIG_IP_VS_WLC=m
CONFIG_IP_VS_LBLC=m
CONFIG_IP_VS_LBLCR=m
CONFIG_IP_VS_DH=m
CONFIG_IP_VS_SH=m
CONFIG_IP_VS_SED=m
CONFIG_IP_VS_NQ=m
CONFIG_IP_VS_SH_TAB_BITS=8
CONFIG_IP_VS_FTP=m
CONFIG_IP_VS_NFCT=y
CONFIG_IP_VS_PE_SIP=m
[root@computer1 ~]#
```

```
静态算法：仅根据算法本身和请求报文特征进行计算　－起点公平
动态算：　额外考虑后端各ＲＳ的当前的负载整体　　－结果公平

静态算法：
　　 RR: round-robin 轮询　
　　 WRR:　weighted rr  加权轮询算法
    sh: source ip hading
    dh: detination ip hahing

动态算法：
　  LC:least connections
    WLC :weihted least connections overead=(activeconnes*256 + inactivconns)/weihted
    sed :
    nq :
    lblc:
    lblcr:


ipvs scheduler：
根据其调度时是否考虑各RS当前的负载状态，可分为静态方法和动态方法两种：

	静态方法：仅根据算法本身进行调度；
	RR：roundrobin，轮询；
	WRR：Weighted RR，加权轮询；
	SH：Source Hashing，实现session sticky，源IP地址hash；将来自于同一个IP地址的请求始终发往第一次挑中的RS，从而实现会话绑定；
	DH：Destination Hashing；目标地址哈希，将发往同一个目标地址的请求始终转发至第一次挑中的RS，典型使用场景是正向代理缓存场景中的负载均衡；

动态方法：主要根据每RS当前的负载状态及调度算法进行调度；
	Overhead=
LC：least connections
	Overhead=activeconns*256+inactiveconns
WLC：Weighted LC
	Overhead=(activeconns*256+inactiveconns)/weight
SED：Shortest Expection Delay
	Overhead=(activeconns+1)*256/weight
NQ：Never Queue

LBLC：Locality-Based LC，动态的DH算法；
LBLCR：LBLC with Replication，带复制功能的LBLC；

```


## **<font color=Red> LVS type**

### **<font color=Red> NAT--D-NAT**

-  通常修改请求报文的目标ＩＰ和PORT为经有调度算法挑选出的某后端ＲＳ的ＲＩＰ和ＰＯＲＴ

```
lvs-nat：
多目标IP的DNAT，通过将请求报文中的目标地址和目标端口修改为某挑出的RS的RIP和PORT实现转发；

(1）RIP和DIP必须在同一个IP网络，且应该使用私网地址；RS的网关要指向DIP；
2）请求报文和响应报文都必须经由Director转发；Director易于成为系统瓶颈；
3）支持端口映射，可修改请求报文的目标PORT；
4）vs必须是Linux系统，rs可以是任意系统


```



### **<font color=Red> DR**

- 通过在原ip报文外封装帧首部（缘MAC DMAC）完成调度，目标MAC是有调度算法挑出的某后端RS的ＭＡＣ地址



```
Direct Routing，直接路由；
通过为请求报文重新封装一个MAC首部进行转发，源MAC是DIP所在的接口的MAC，目标MAC是某挑选出的RS的RIP所在接口的MAC地址；源IP/PORT，以及目标IP/PORT均保持不变；

Director和各RS都得配置使用VIP；
  (1) 确保前端路由器将目标IP为VIP的请求报文发往Director：
	(a) 在前端网关做静态绑定；
	(b) 在RS上使用arptables；
	(c) 在RS上修改内核参数以限制arp通告及应答级别；
			arp_announce
			arp_ignore
(2) RS的RIP可以使用私网地址，也可以是公网地址；RIP与DIP在同一IP网络；RIP的网关不能指向DIP，以确保响应报文不会经由Director；
(3) RS跟Director要在同一个物理网络；
(4) 请求报文要经由Director，但响应不能经由Director，而是由RS直接发往Client；
(5) 不支持端口映射；


```

### **<font color=Red> TUN**
- 通过在原ＩＰ报文外在封装一个新的ＩＰ首部（CIP:VIP）外再封装一个新的首部(DIP:VIP）完成调度

```
lvs-tun：
转发方式：不修改请求报文的IP首部（源IP为CIP，目标IP为VIP），而是在原IP报文之外再封装一个IP首部（源IP是DIP，目标IP是RIP），将报文发往挑选出的目标RS；RS直接响应给客户端（源IP是VIP，目标IP是CIP）；

	(1) DIP, VIP, RIP都应该是公网地址；
	(2) RS的网关不能，也不可能指向DIP；
	(3) 请求报文要经由Director，但响应不能经由Director；
	(4) 不支持端口映射；
	(5) RS的OS得支持隧道功能；
```


### **<font color=Red> FULLNAT**
- 通常修改请求报文的目标ＩＰ和原目的ＩＰ和目标ＩＰ（ＶＩＰ－》ＲＩＰ）完成调度

```
lvs-fullnat：
通过同时修改请求报文的源IP地址和目标IP地址进行转发；
		CIP <--> DIP
		VIP <--> RIP
(1) VIP是公网地址，RIP和DIP是私网地址，且通常不在同一IP网络；因此，RIP的网关一般不会指向DIP；
(2) RS收到的请求报文源地址是DIP，因此，只能响应给DIP；但Director还要将其发往Client；
(3) 请求和响应报文都经由Director；
(4) 支持端口映射；

注意：此类型默认不支持；
```

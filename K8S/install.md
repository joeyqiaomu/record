# **<font color=Red> k8s**

## **<font color=Red> install**


```

具体步骤：
1. master 和 node 先安装 kubelet，docker，kubeadm
2. master 节点运行 kubeadm init 初始化命令
3. 验证 master
4. Node 节点使用 kubeadm 加入 k8s master
5. 验证 node
6．启动容器测试访问
------------------------------------------
禁止下面的服务：
	ufw disable
	swapoff -a 禁止swap  /etc/fstab
	selinux
```
### **<font color=Red> install docker**

```

1：安装 docker:

	# step 1: 安装必要的一些系统工具
	sudo apt-get update
	sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
	# step 2: 安装GPG证书
	curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
	# Step 3: 写入软件源信息
	sudo add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
	sudo apt-get -y update
	# Step 4: 更新并安装Docker-CE

	 安装指定版本的Docker-CE:
	 Step 1: 查找Docker-CE的版本:
	 apt-cache madison docker-ce
	 docker-ce | 17.03.1~ce-0~ubuntu-xenial | https://mirrors.aliyun.com/docker-ce/linux/ubuntu xenial/stable amd64 Packages
	 docker-ce | 17.03.0~ce-0~ubuntu-xenial | https://mirrors.aliyun.com/docker-ce/linux/ubuntu xenial/stable amd64 Packages
	 Step 2: 安装指定版本的Docker-CE: (VERSION例如上面的17.03.1~ce-0~ubuntu-xenial)
	 sudo apt-get -y install docker-ce=[VERSION]
	 sudo apt-get -y install docker-ce
	 systemctl start docker
	 systemctl enable docker


	阿里镜像加速器：
	 mkdir -p /etc/docker
	tee /etc/docker/daemon.json <<-'EOF'
	{
	  "registry-mirrors": ["https://okgsfi45.mirror.aliyuncs.com"]
	}
	EOF
	systemctl daemon-reload
	systemctl restart docker
```


### **<font color=Red> 2:安装 k8s kubelet kubeadm kubectl**


```

配置阿里云仓库地址:
配置阿里云镜像的 kubernetes 源(用于安装 kubelet kubeadm kubectl 命令)

apt-get update
apt-get install -y apt-transport-https
curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | apt-key add -
cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main
EOF
apt-get update

安装指定版本 kubeadm
  apt-cache madison kubeadm #查看版本信息 -------
  kubeadm --help  查看kubeadm 是否完成

apt-get install kubeadm=1.14.1-00 kubelet=1.14.1-00 kubectl=1.14.1-00



验证版本：
# kubeadm version #查看当前 kubeadm 版本
# kubeadm config images list --kubernetes-version v1.14.1 #查看安装指定版本 k8s需要的镜像有哪些
k8s.gcr.io/kube-apiserver:v1.14.1
k8s.gcr.io/kube-controller-manager:v1.14.1
k8s.gcr.io/kube-scheduler:v1.14.1
k8s.gcr.io/kube-proxy:v1.14.1
k8s.gcr.io/pause:3.1
k8s.gcr.io/etcd:3.3.10
k8s.gcr.io/coredns:1.3.1


```
### **<font color=Red> master节点初始化：**



```
3：master节点初始化：

kubeadm init --apiserver-advertise-address=192.168.101.201 --apiserver-bind-port=6443 --kubernetes-version=v1.14.1 --pod-network-cidr=10.10.0.0/16 --service-cidr=10.200.0.0/16 --service-dns-domain=linux36.local --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers --ignore-preflight-errors=swap



[addons] Applied essential addon: kube-proxy

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.101.201:6443 --token aqkwlz.xdezix15w4pxhuik \
    --discovery-token-ca-cert-hash sha256:88522e4383bf8599fd94fa676a4297aa32569a888096253ae84f2aff27d8b174
root@k8s-master:~#

```
### **<font color=Red> 4;网络初始化**

```

在masster节点进行下面配置：node节点不用配置，
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

node：
添加两个 node 节点：
  各 node 节点都要安装 docker kubeadm kubelet ，因此都要执行步骤 1-2，即配置 apt 仓库、配置 docker 加速器、安装命令、启动 kubelet 服务。
root@docker-node2:~# systemctl start docker kubelet
root@docker-node2:~# systemctl enable docker kubelet

kubeadm join 192.168.101.201:6443 --token aqkwlz.xdezix15w4pxhuik \
    --discovery-token-ca-cert-hash sha256:88522e4383bf8599fd94fa676a4297aa32569a888096253ae84f2aff27d8b174
```

### **<font color=Red> 查看命令**

```

#命令：

kubectl get node
kubectl get pods --all-namespaces
kubectl get pods -o wide -n kube-system

```
### **<font color=Red> 升级**


```

kubeadm 升级 k8s 集群:
升级 k8s 集群必须 先升级 kubeadm 版本到目的 k8s 版本
1:验证当 k8s 前版本:
root@k8s-master:~# kubeadm version


2:安装指定版本 kubeadm:
root@docker-node1:~# apt-cache madison kubeadm
root@docker-node1:~# apt-get install kubeadm=1.14.3-00　apt-get install kubelet=1.14.3-00 kubectl=1.14.3-00
#查看具体版本
install kubeadm=1.１４.３-00
#安装具体版本
root@docker-node1:~# kubeadm version #验证版本
kubeadm version: &version.Info{Major:"1", Minor:"14", GitVersion:"v1.14.3", GitCommit:"5e53fd6bc17c0dec8434817e69b04a25d8ae0ff0", GitTreeState:"clean", BuildDate:"2019-06-06T01:41:54Z", GoVersion:"go1.12.5", Compiler:"gc", Platform:"linux/amd64"}


3:kubeadm 升级命令使用帮助:
root@docker-node1:~# kubeadm upgrade　--help

kubeadm upgrade plan --help
root@k8s-master:~# kubeadm upgrade plan ----检查升级
[preflight] Running pre-flight checks.
[upgrade] Making sure the cluster is healthy:
[upgrade/config] Making sure the configuration is correct:
[upgrade/config] Reading configuration from the cluster...
[upgrade/config] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
[upgrade] Fetching available versions to upgrade to
[upgrade/versions] Cluster version: v1.14.1
[upgrade/versions] kubeadm version: v1.14.3
I0301 06:56:51.119306  129525 version.go:240] remote version is much newer: v1.17.3; falling back to: stable-1.14
[upgrade/versions] Latest stable version: v1.14.10
[upgrade/versions] Latest version in the v1.14 series: v1.14.10

Components that must be upgraded manually after you have upgraded the control plane with 'kubeadm upgrade apply':
COMPONENT   CURRENT       AVAILABLE
Kubelet     3 x v1.14.1   v1.14.10

Upgrade to the latest version in the v1.14 series:

COMPONENT            CURRENT   AVAILABLE
API Server           v1.14.1   v1.14.10
Controller Manager   v1.14.1   v1.14.10
Scheduler            v1.14.1   v1.14.10
Kube Proxy           v1.14.1   v1.14.10
CoreDNS              1.3.1     1.3.1
Etcd                 3.3.10    3.3.10

You can now apply the upgrade by executing the following command:

        kubeadm upgrade apply v1.14.10

Note: Before you can perform this upgrade, you have to update kubeadm to v1.14.10.

升级：
root@k8s-master:~# kubeadm upgrade apply v1.14.3


root@k8s-master:~# kubeadm upgrade node config --kubelet-version 1.14.3
[kubelet-start] Downloading configuration for the kubelet from the "kubelet-config-1.14" ConfigMap in the kube-system namespace
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[upgrade] The configuration for this node was successfully updated!
[upgrade] Now you should go ahead and upgrade the kubelet package using your package manager.
root@k8s-master:~#


node节点：
apt-get install kubeadm=1.14.3-00　
apt-get install kubelet=1.14.3-00 kubectl=1.14.3-00

```

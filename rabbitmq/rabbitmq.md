# **<font color=Red> rabbitmq**

## **<font color=Red>  工作模式**
```python
import pika
from pika.credentials import PlainCredentials
para = pika.URLParameters('amqp://qiaomu:joey123@192.168.5.200:5672/test')
# 用户名：密码：//地址：端号/虚拟主机
param = pika.ConnectionParameters('192.168.5.200')
connection = pika.BlockingConnection(para)
channel = connection.channel()
# switch like router
queun_name = 'hello'
#queue
channel.queue_declare(queue='hello')
with connection:
    #发送消息
    for i in range(10):
        msg = 'data-{}'.format(i)

        channel.basic_publish(exchange='', # 缺省swicth
                              routing_key=queun_name,
                              body=msg)
        print(" [x] Sent 'Hello World!'")



import pika
from pika.credentials import PlainCredentials
para = pika.URLParameters('amqp://qiaomu:joey123@192.168.5.200:5672/test')
connection = pika.BlockingConnection(para)
channel = connection.channel()
# switch like router
#queue
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" msg = {} ".format(body))

def callback1(ch, method, properties, body):
    print(" msg1 = {} ".format(body))


with connection:
    # 消费者 每一个消费者使用一个basic consume
    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)
    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback1)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming() #启动所有消费，知道所有消费结束 才能推出，阻塞的


D:\python_code\venv\Scripts\python.exe D:/test/rabbitmq/r_cu.py
 [*] Waiting for messages. To exit press CTRL+C
 msg = b'data-0'
 msg1 = b'data-1'
 msg = b'data-2'
 msg1 = b'data-3'
 msg = b'data-4'
 msg1 = b'data-5'
 msg = b'data-6'
 msg1 = b'data-7'
 msg = b'data-8'
 msg1 = b'data-9'
```

## **<font color=Red>  发布与订阅**
```python
---------生产者
import pika
from pika.credentials import PlainCredentials
para = pika.URLParameters('amqp://qiaomu:joey123@192.168.5.200:5672/test')
# 用户名：密码：//地址：端号/虚拟主机
param = pika.ConnectionParameters('192.168.5.200')
connection = pika.BlockingConnection(para)
channel = connection.channel()
# switch like router
exchange_name = 'logs'

#q = channel.queue_declare(queue='') #不指定名称 queue名称随机生成，（生产者和消费者都可以生成queue）,
#取名称 q.method,queue

channel.exchange_declare(exchange=exchange_name, #指定交换机
                         exchange_type='fanout') # 广播 扇出
with connection:
    #发送消息
    for i in range(10):
        msg = 'data-{}'.format(i)
        channel.basic_publish(exchange=exchange_name,  # swicth
                              routing_key='',
                              body=msg)

        print(" [x] Sent 'Hello World!'")

-----------------消费者（队列在消费者生成 也可以在生产者生成，但是名称要固定下来）
import pika
from pika.credentials import PlainCredentials
para = pika.URLParameters('amqp://qiaomu:joey123@192.168.5.200:5672/test')
connection = pika.BlockingConnection(para)
channel = connection.channel()


# switch like router
exchange_name = 'logs'
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout') # 广播 扇出

#queue
q1 = channel.queue_declare(queue='', exclusive=True)#exclusive 在断开实时 会queue删除
q2 = channel.queue_declare(queue='', exclusive=True)#exclusive 在断开实时 会queue删除
q1name = q1.method.queue
q2name = q2.method.queue
#bind
channel.queue_bind(exchange='logs',
                   queue=q1name) #将队列和某一个交换机关联

channel.queue_bind(exchange='logs',
                   queue=q2name) #将队列和某一个交换机关联


def callback(ch, method, properties, body):
    print(" msg = {} ".format(body))

def callback1(ch, method, properties, body):
    print(" msg1 = {} ".format(body))


with connection:
    # 消费者 每一个消费者使用一个basic consume
    channel.basic_consume(queue=q1name,
                          auto_ack=True,
                          on_message_callback=callback)
    channel.basic_consume(queue=q2name,
                          auto_ack=True,
                          on_message_callback=callback1)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming() #启动所有消费，知道所有消费结束 才能推出，阻塞的

```

## **<font color=Red>  路由模式**

```python

-----------productor

import pika
import random
from pika.credentials import PlainCredentials
para = pika.URLParameters('amqp://qiaomu:joey123@192.168.5.200:5672/test')
# 用户名：密码：//地址：端号/虚拟主机
param = pika.ConnectionParameters('192.168.5.200')
connection = pika.BlockingConnection(para)
channel = connection.channel()
# switch like router
exchange_name = 'color'
colors =('orange','black','green')

#q = channel.queue_declare(queue='') #不指定名称 queue名称随机生成，（生产者和消费者都可以生成queue）,
#取名称 q.method,queue

channel.exchange_declare(exchange=exchange_name, #指定交换机
                         exchange_type='direct') # 广播 扇出
with connection:
    #发送消息
    for i in range(20):
        rk = random.choice(colors)
        msg = '{}:data-{}'.format(rk,i)
        channel.basic_publish(exchange=exchange_name,  # swicth
                              routing_key=rk,
                              body=msg)

        print(" [x] Sent 'Hello World!'")

------------------consumer

import pika
from pika.credentials import PlainCredentials
para = pika.URLParameters('amqp://qiaomu:joey123@192.168.5.200:5672/test')
connection = pika.BlockingConnection(para)
channel = connection.channel()


# switch like router
exchange_name = 'color'
colors =('orange','black','green')
channel.exchange_declare(exchange=exchange_name,
                         exchange_type='direct') # 广播 扇出

#queue
q1 = channel.queue_declare(queue='', exclusive=True)#exclusive 在断开实时 会queue删除
q2 = channel.queue_declare(queue='', exclusive=True)#exclusive 在断开实时 会queue删除
q1name = q1.method.queue
q2name = q2.method.queue
#bind
channel.queue_bind(exchange=exchange_name,
                   queue=q1name,
                   routing_key=colors[0]) #将队列和某一个交换机关联

channel.queue_bind(exchange=exchange_name,
                   queue=q2name,
                   routing_key=colors[1]) #将队列和某一个交换机关联

channel.queue_bind(exchange=exchange_name,
                   queue=q2name,
                   routing_key=colors[2]) #将队列和某一个交换机关联

def callback(ch, method, properties, body):
    print(" msg = {} ".format(body),method)

def callback1(ch, method, properties, body):
    print(" msg1 = {} ".format(body),method)


with connection:
    # 消费者 每一个消费者使用一个basic consume
    channel.basic_consume(queue=q1name,
                          auto_ack=True,
                          on_message_callback=callback)
    channel.basic_consume(queue=q2name,
                          auto_ack=True,
                          on_message_callback=callback1)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming() #启动所有消费，知道所有消费结束 才能推出，阻塞的


```

## **<font color=Red>  topic**

```python
topic 就是更高级的路由 支持模式匹配而已
-----------------------productor
import pika
import random
from pika.credentials import PlainCredentials
para = pika.URLParameters('amqp://qiaomu:joey123@192.168.5.200:5672/test')
# 用户名：密码：//地址：端号/虚拟主机
param = pika.ConnectionParameters('192.168.5.200')
connection = pika.BlockingConnection(para)
channel = connection.channel()
# switch like router
exchange_name = 'product'
colors =('orange', 'black', 'red')
topic = ('phone.*', '*.red') # *表示一个单词
products = ('phone','pc','tv')

#q = channel.queue_declare(queue='') #不指定名称 queue名称随机生成，（生产者和消费者都可以生成queue）,
#取名称 q.method,queue

channel.exchange_declare(exchange=exchange_name, #指定交换机
                         exchange_type='topic') # 广播 扇出
with connection:
    #发送消息
    for i in range(20):
        rk = '{}.{}'.format(
            random.choice(products),
            random.choice(colors))
        msg = '{}:data-{}'.format(rk,i)
        channel.basic_publish(exchange=exchange_name,  # swicth
                              routing_key=rk,
                              body=msg)
        print(" [x] Sent 'Hello World!'")


-----------------------consume
import pika
from pika.credentials import PlainCredentials
para = pika.URLParameters('amqp://qiaomu:joey123@192.168.5.200:5672/test')
connection = pika.BlockingConnection(para)
channel = connection.channel()


# switch like router
exchange_name = 'product'
colors =('orange', 'black', 'red')
topic = ('phone.*', '*.red') # *表示一个单词
products = ('phone','pc','tv')
channel.exchange_declare(exchange=exchange_name,
                         exchange_type='topic') # 话题

#queue
q1 = channel.queue_declare(queue='', exclusive=True)#exclusive 在断开实时 会queue删除
q2 = channel.queue_declare(queue='', exclusive=True)#exclusive 在断开实时 会queue删除
q1name = q1.method.queue
q2name = q2.method.queue
#bind
channel.queue_bind(exchange=exchange_name,
                   queue=q1name,
                   routing_key=topic[0]) #将队列和某一个交换机关联

channel.queue_bind(exchange=exchange_name,
                   queue=q2name,
                   routing_key=topic[1]) #将队列和某一个交换机关联


def callback(ch, method, properties, body):
    print(" msg = {} ".format(body),method)

def callback1(ch, method, properties, body):
    print(" msg1 = {} ".format(body),method)


with connection:
    # 消费者 每一个消费者使用一个basic consume
    channel.basic_consume(queue=q1name,
                          auto_ack=True,
                          on_message_callback=callback)
    channel.basic_consume(queue=q2name,
                          auto_ack=True,
                          on_message_callback=callback1)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming() #启动所有消费，知道所有消费结束 才能推出，阻塞的


```

## **<font color=Red>  普通模式**
```python

import pika
from pika.credentials import PlainCredentials
para = pika.URLParameters('amqp://qiaomu:joey123@192.168.5.200:5672/test')
# 用户名：密码：//地址：端号/虚拟主机
param = pika.ConnectionParameters('192.168.5.200')
connection = pika.BlockingConnection(para)
channel = connection.channel()
# switch like router
queun_name = 'hello'
#queue
channel.queue_declare(queue='hello')
with connection:
    #发送消息
    for i in range(10):
        msg = 'data-{}'.format(i)

        channel.basic_publish(exchange='', # swicth
                              routing_key=queun_name,
                              body=msg)
        print(" [x] Sent 'Hello World!'")



import pika
from pika.credentials import PlainCredentials
#para = pika.URLParameters('amqp://qiaomu:joey123@192.168.5.200:5672/test')
param = pika.ConnectionParameters('192.168.5.200')
connection = pika.BlockingConnection(param)
channel = connection.channel()
# switch like router
#queue
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

with connection:
    # 消费者 每一个消费者使用一个basic consume
    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming() #启动所有消费，知道所有消费结束 才能推出，阻塞的



```

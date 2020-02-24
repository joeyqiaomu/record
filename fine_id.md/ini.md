### **<font color=Red> configparser**

```python

import configparser

cfg = configparser.ConfigParser()
bgp_ini = cfg.read('bgp.ini')
print(bgp_ini,type(cfg))

print(cfg.sections(),cfg.default_section)

print(cfg._sections.keys())
print("---------------------------------------")
print(cfg.items())

for k,x in cfg.items():
    print(type(x),x,type(k),k)
print("---------------------------------------")
for k,v in cfg.items('BGP_ONE'):
    print(type(v),v,type(k),k)

x = cfg.get('BGP_TWO','a')

y = cfg.getint('BGP_ONE','LOCAL_AS')

print(type(x),x)
print(type(y),y)
print("---------------------------------------")

#  写文件
with open('test.ini') as f
    cfg.write(f)


```

```python
import configparser

cfg = configparser.ConfigParser()
bgp_ini = cfg.read('bgp.ini')
print(bgp_ini,type(cfg))

print(cfg.sections(),cfg.default_section)

print(cfg._sections.keys())
print("---------------------------------------")
print(cfg.items())

for k,x in cfg.items():
    print(type(x),x,type(k),k)
print("---------------------------------------")
for k,v in cfg.items('BGP_ONE'):
    print(type(v),v,type(k),k)

x = cfg.get('BGP_TWO','a')

y = cfg.getint('BGP_ONE','LOCAL_AS')

print(type(x),x)
print(type(y),y)
print("---------------------------------------")



print("=======================================")
# 字典修改
#print(cfg['BGP_ONE']['b'])

if cfg.has_section('test'):
    #cfg.add_section('test')
    cfg.remove_section('test')

#cfg['test'] = {}
cfg['test'] = {'test1':100}
cfg['test']['test2'] = "True"

if cfg.has_option('test','test1'):
    cfg.remove_option('test','test1')

print('test1' in cfg)


 #写文件
with open('bgp.ini','w') as f:
    print("+++++++++++++++")
    cfg.write(f)
```

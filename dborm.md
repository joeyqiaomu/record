# **ORM**


```python
import sqlalchemy
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html

IP ='192.168.6.2'
USERNAME = 'joey'
PASSWORD ='joey'
DBNAME = 'test'
PORT = 3306


#ORM Mapping
Base = declarative_base() #基类


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)#定义字段类型和属性
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "<{} id={} ,name={} ,age={} ".format(
                                 __class__.__name__,self.name, self.fullname, self.nickname)
print(Student.__dict__)
print(Student.__table__)
print(repr(Student.__table__))

#mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
print(sqlalchemy.__version__)

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,IP,PORT,DBNAME), echo=True)#lazy

print(engine)
#Base.metadata.drop_all(engine)
#Base.metadata.create_all(engine)


```

## **add**
```python
import sqlalchemy
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html

IP ='192.168.6.2'
USERNAME = 'joey'
PASSWORD ='joey'
DBNAME = 'test'
PORT = 3306


#mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
print(sqlalchemy.__version__)
#lazy 连接池
engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,IP,PORT,DBNAME), echo=True)



#ORM Mapping
Base = declarative_base() #基类


class Student(Base):
    __tablename__ = "student" # 类和student表对应
    id = Column(Integer, primary_key=True, autoincrement=True)#定义字段类型和属性
    name = Column(String(64), nullable=False)
    age = Column(Integer)
    #Column和属性对应

    def __repr__(self):
        return "<{} id={} ,name={} ,age={} ".format(
                                 __class__.__name__,self.id, self.name, self.age)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
#print(engine)
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

############################################################################

Seesion = sessionmaker(bind=engine)
session = Seesion()#线程不安全
print(session,type(session))

#增加



#实例和表中每行进行mapping 一一对应
student = Student(name='jerry')
student.name = 'tom'
student.age = 20

session.add(student)
session.commit()

print(student)

try:
    student.name = 'ben'
    session.add_all([student])
    session.commit()
    print("+++++++++++++++++++++++")
except:
    session.rollback()
    print("~~~~~~~~~~~~~~")

```



## **查询**

```python
import sqlalchemy
from sqlalchemy import create_engine,Column,String,Integer,Date,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html

IP ='192.168.6.2'
USERNAME = 'joey'
PASSWORD ='joey'
DBNAME = 'test'
PORT = 3306


#mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
print(sqlalchemy.__version__)
#lazy 连接池
engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,IP,PORT,DBNAME), echo=True)

#ORM Mapping
Base = declarative_base() #基类

import enum
class GenderEnum(enum.Enum):
    M = "M"
    F = "F"

class Emplopee(Base):

    __tablename__ = 'employees'
    emp_no = Column(Integer,primary_key=True)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(GenderEnum), nullable=False)
    hire_date = Column(Date,nullable=False)

    def __repr__(self):
        return "<{} no={} ,name={} {} ,gender={} ".format(
            __class__.__name__, self.emp_no, self.first_name,self.last_name, self.gender.value)

from sqlalchemy.orm.session import Session
from sqlalchemy.orm.state import InstanceState
seesion:Session = sessionmaker(bind=engine)()
print(seesion,type(seesion))

def show(emps):
    for x in emps:
        print(x)
##########################################################################
emps = seesion.query(Emplopee).filter(Emplopee.emp_no >10015)
print(emps)
show(emps)Object oriented advanced Object oriented advanced
```

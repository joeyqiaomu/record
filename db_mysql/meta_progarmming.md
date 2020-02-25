# **<font color=Red> Meta programming**



```python


def __init__(self):
    self.x = 100


def show(self):
    print(self.x)


XClass = type('X',(object,),{'a':100,'b':200,
                             '__init__':__init__,
                             'show':show})
                              # a b 是实例的属性
print(XClass)
print(XClass.__name__)
print(XClass.__base__)
print(XClass.__mro__)
print(XClass.a,XClass.b)
print(XClass.__dict__)
print(XClass().x)
XClass().show()

print(type(XClass))

```

```python
class Meta(type):
    def __new__(cls, *args, **kwargs):
        print(cls) # who
        print(args) # ?
        print(kwargs)
        print()
        return super().__new__(cls,*args,**kwargs)

print("-----------------------------------------------------")

class A(metaclass=Meta):
    pass
print(type(A))
print(A.__bases__)
```


# **<font color=Red>  构建元类**
- 一个类可以继承自type类。注意不是继承自object类了
- 继承自type,ModelMeta就是元类,它可以创建出其它类

```
class ModelMeta(type):
def __new__(cls, *args, **kwargs):
print(cls)
print(args)
print(kwargs)
return super().__new__(cls, *args,**kwargs)
```

## **<font color=Red> 元类的使用方式**
```python
#meta元类的类（创造元类的类）
class Meta(type):
    def __new__(cls, name,bases,attrs:dict):
        print(name) # ?
        print(bases)
        print(attrs)
        attrs['a']=100
        print()
        return super().__new__(cls, name,bases,attrs)

print("-----------------------------------------------------")

class A(metaclass=Meta):
    pass
print(type(A))
print(A.__bases__)
print(A.__dict__)

----------------------

#meta元类的类（构造类的类）
class Meta(type):
    def __new__(cls, name,bases,attrs:dict):
        print(name) # ?
        print(bases)
        print(attrs)
        attrs['id']=200
        print()
        return super().__new__(cls, name+'123',bases,attrs)

print("-----------------------------------------------------")

class A(metaclass=Meta):

    id = 2000

    def __init__(self):
        print('A.init--------------')

print(type(A))
print(A.__bases__)
print(A.__dict__)
print(A.__name__) # A123
print("==========================================")
class B(A):#A 继承时　将元类也一样
    pass


print(type(B),B.__bases__)
print(B.__dict__)
print(B.__name__)


/home/joey/python/code/venv/bin/python /home/joey/python/code/t6.py
-----------------------------------------------------
A
()
{'__module__': '__main__', '__qualname__': 'A', 'id': 2000, '__init__': <function A.__init__ at 0x7ffafc0339d8>}

<class '__main__.Meta'>
(<class 'object'>,)
{'__module__': '__main__', 'id': 200, '__init__': <function A.__init__ at 0x7ffafc0339d8>, '__dict__': <attribute '__dict__' of 'A123' objects>, '__weakref__': <attribute '__weakref__' of 'A123' objects>, '__doc__': None}
A123
==========================================
B
(<class '__main__.A'>,)
{'__module__': '__main__', '__qualname__': 'B'}

<class '__main__.Meta'> (<class '__main__.A'>,)
{'__module__': '__main__', 'id': 200, '__doc__': None}
B123

```

```python
#meta元类的类（构造类的类）
class Meta(type):
    def __new__(cls, name,bases,attrs:dict):
        print(name) # ?
        print(bases)
        print(attrs)
        attrs['id']=200
        print()
        return super().__new__(cls, name+'123',bases,attrs)

print("-----------------------------------------------------")

class A(metaclass=Meta):

    id = 2000

    def __init__(self):
        print('A.init--------------')

print(type(A))
print(A.__bases__)
print(A.__dict__)
print(A.__name__) # A123
print("==========================================")
class B(A):#A 继承时　将元类也一样
    pass


print(type(B),B.__bases__)
print(B.__dict__)
print(B.__name__)
print("++++++++++++++++++++++++++++++++++++++++++++")
C = Meta('C',(),{})

print(type(A),A.__bases__)
print(type(B),B.__bases__)
print(type(C),C.__bases__)
print(C.__dict__)
print(C.__name__)

print("+++++=========================++++++++++")

class D:pass
E = type('E',(),{})

print(type(D),D.__bases__)
print(type(E),E.__bases__)

print("+++++=======~~~~~~~~~~~~~~~~~~~~~~~~~`===++++++++++")
class F(Meta):pass #继承　Ｆ 是元类

print(type(F),F.__bases__)

```

# **<font color=Red>元类的应用**



```python
class Column:
  def __init__(self, fieldname=None, pk=False, nullable=False):
    self.fieldname = fieldname
    self.pk = pk
    self.nullable = nullable
    def __repr__(self):
    return "<{} {}>".format(__class__.__name__, self.fieldname)
class ModelMeta(type):
  def __new__(cls, name, bases, attrs:dict):
    print(cls)
    print(name, bases, attrs)
    if '__tablename__' not in attrs:
    attrs['__tablename__'] = name.lower() # 添加表名
    primarykeys = []
    for k, v in attrs.items():
      if isinstance(v, Column):
        if v.fieldname is None or v.fieldname.strip() == '':
        v.fieldname = k # 字段没有名字使用属性名
    if v.pk:
    primarykeys.append(v)
    attrs['__primarykeys__'] = primarykeys
  return super().__new__(cls, name, bases, attrs)
class Base(metaclass=ModelMeta):
"""从ModelBase继承的类的类型都是ModelMeta"""
class Student(Base):
  id = Column(pk=True, nullable=False)
  name = Column('username', nullable=False)
  age = Column()
  print('-' * 30)
  print(Student.__dict__)
```
# **<font color=Red>作业**


```python

'''
使用SqlAlchemy
10009号员工的工号、姓名、所有的头衔title
10010号员工的工号、姓名、所在部门名称
'''
import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer,Date,Enum,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

# "mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DBNAME),
                       echo=True)  # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))


##################################################################################

# ORM Mapping
Base = declarative_base()
import enum
class GenderEnum(enum.Enum):
    M = 'M'
    F = 'F'


# class Student(Base):
#
#     __tablename__ = 'student'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)  # 定义字段类型和属性
#     name = Column(String(64), nullable=False)
#     age = Column(Integer)
#
#     def __repr__(self):
#         return "{} id ={},name={},age={}".format(
#
#             __class__.__name__, self.id, self.name, self.age
#         )


class Employee(Base):

    __tablename__ = 'employees'

    emp_no = Column(Integer,primary_key=True)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(GenderEnum),nullable=False)
    hire_date = Column(Date,nullable=False)

    departments = relationship('Dept_emp')
    titles = relationship('Title')

    def __repr__(self):
        return "<{} no ={},birth_date={},first_name={},last_name={},gender={},hird_date={}".format(
            __class__.__name__, self.emp_no, self.birth_date, self.first_name,self.last_name,self.gender.value,self.hire_date
        )


class Department(Base):

    __tablename__ = 'departments'

    dept_no = Column(String(4),primary_key=True)
    dept_name = Column(String(40),nullable=False,unique=True)

    def __repr__(self):
        return "<{} dept_no ={},dept_name={}>".format(
            __class__.__name__, self.dept_no, self.dept_name
        )



class Dept_emp(Base):
    __tablename__ = 'dept_emp'

    emp_no = Column(Integer,ForeignKey('employees.emp_no',ondelete='CASCADE'), primary_key=True)
    dept_no = Column(String(4),ForeignKey('departments.dept_no',ondelete='CASCADE'), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    department = relationship('Department')
    def __repr__(self):
        return "<{} emp_no ={},dept_no={},>".format(
            __class__.__name__, self.emp_no, self.dept_no
        )


class Title(Base):
    __tablename__ = 'titles'

    emp_no = Column(Integer,ForeignKey('employees.emp_no',ondelete='CASCADE'), primary_key=True)
    title = Column(String,primary_key=True)
    from_date=Column(Date,primary_key=True)
    to_date = Column(Date)

    def __repr__(self):
        return "<{} emp_no ={},title={} ".format(
            __class__.__name__, self.emp_no, self.title
        )


from sqlalchemy.orm.session import Session
session: Session = sessionmaker(bind=engine)()

def show(emps):
    for i in emps:
        print(i)
    print(end='\n\n')

#emps = session.query(Employee.emp_no,Employee.first_name,Title.title).join(Employee,Title.emp_no == Employee.emp_no).filter(Title.emp_no == 10009).all()
#emps = session.query(Employee.emp_no,Employee.first_name,Title.title).filter((Title.emp_no == Employee.emp_no)&(Title.emp_no == 10009)).all()
# for no,name,title in emps:
#     print(no,name,title)
# emps = session.query(Employee).get(10009)
# print(emps.emp_no,emps.first_name,[t.title for t in emps.titles])


###########################################################################
emps = session.query(Employee).get(10010)
print([d.department for d in emps.departments])

# results = session.query(Employee,Department.dept_no,Department.dept_name).join(Dept_emp,(Employee.emp_no == Dept_emp.emp_no) &(Employee.emp_no==10010)).join(Department,Dept_emp.dept_no == Department.dept_no).all()
#
# for x in results:
#     print(x)
#     print(x.Employee.first_name)
#     print(x.dept_no)
#     print(x.dept_name)

results = session.query(Employee.emp_no,Employee.first_name,Department.dept_no,Department.dept_name).join(Dept_emp,(Employee.emp_no == Dept_emp.emp_no) &(Employee.emp_no==10010)).join(Department,Dept_emp.dept_no == Department.dept_no).all()

for m,n,o,p in results:
    print(m,n,o,p)
```

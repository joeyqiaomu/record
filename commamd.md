
## 命令分发器

```python

def command_dispatcher():
    commands = {}

    def reg(name):
        def wrapper(fn):
            commands[name] = fn #,args,kwargs
            # x3=> fool,() {x:1,y:2}
            # x2=> fool,(100,200) {}
            # x1=> fool,(200,300) {}
            return fn
        return wrapper

    def default_func():
        print("unknown command")


    def dispatcher(*args,**kwargs):
        while True:
            cmd = input(">>>>>>>>>>>>>")
            if cmd.strip() == '':
                return

            fname, *params = cmd.replace(",", " ").split()
            args = []
            kwargs = {}
            for i in params:
                x = i.split('=',maxsplit=1)
                if len(x) == 1:
                    args.append(int(x[0]))
                elif len(x) == 2:
                    kwargs[x[0]] = int(x[1])

            commands.get(fname, default_func)(*args,**kwargs)
    return reg, dispatcher


reg, dispatcher = command_dispatcher()



@reg("f1")
def foo1(x:int, y:int):
    print("fool~~~~~~~~~~~~~~~~~~~",x,y,x+y)


@reg("f2")
def foo2(a,b=20):
    print("foo2~~~~~~~~~~~~~~~~~~~")


dispatcher()
```

```python

def command_dispatcher():
    commands = {}

    def reg(name,*args, **kwargs):
        def wrapper(fn):
            commands[name] = fn,args,kwargs
            # x3=> fool,() {x:1,y:2}
            # x2=> fool,(100,200) {}
            # x1=> fool,(200,300) {}
            return fn
        return wrapper

    def default_func(*args, **kwargs):
        print("unknown command")


    def dispatcher():
        while True:
            cmd = input(">>>>>>>>>>>>>")
            if cmd.strip() == '':
                break
            fn,args,kwargs = commands.get(cmd, (default_func, (), {}))
            fn(*args,**kwargs)
    return reg, dispatcher


reg, dispatcher = command_dispatcher()


@reg("x1", 100, 200)
@reg("x2", 100, 200)
@reg("x3", x=1, y=2)
def foo1(x,y):
    print("fool~~~~~~~~~~~~~~~~~~~",x,y,x+y)


@reg("f2")
def foo2(a,b=20):
    print("foo2~~~~~~~~~~~~~~~~~~~")


dispatcher()
```

```python

def command_dispatcher():
    commands = {}

    def reg(name):
        def wrapper(fn):
            commands[name] = fn
            return fn
        return wrapper

    def default_func():
        print("unknown command")

    def dispatcher():
        while True:
            cmd = input(">>>>>>>>>>>>>")
            if cmd.strip() == '':
                break
            commands.get(cmd, default_func)()

    return reg, dispatcher


reg, dispatcher = command_dispatcher()


@reg("f1")
def foo1():
    print("fool~~~~~~~~~~~~~~~~~~~")


@reg("f2")
def foo2():
    print("foo2~~~~~~~~~~~~~~~~~~~")


dispatcher()
```

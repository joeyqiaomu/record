## **<font color=Red> argparse**

```python


import argparse
from pathlib import  Path
import datetime
# ls -a
parser = argparse.ArgumentParser(prog='ls',description='list paramters.',add_help=False)
parser.add_argument('path',nargs='?',default='.',help='path help') # ａ是参数
parser.add_argument('-l',action='store_true',help='usr a long listing format') #--b 选项　选项后面也需要参数　tar -x -f src (-f后面必须有参数，tar -xf  如果参数　tar -fx 那么错误，－ｆ必须放在后面)
#[-b B] Ｂ选项的需要参数
parser.add_argument('-a','-all',action='store_true',help='list the . file') # ａ是参数
parser.add_argument('-h','--human readable',action='store_true',help='for readable ',dest='human') # ａ是参数
parser.print_help()
args = parser.parse_args(('/home/joey/python/code','-alh')) #解析提供的参数是否满足现在的定义
# print(args.accumulate(args.integers))
# print(args)
# print(args.path,args.l,args.a,args.human)


def listdir(path,detail=False,all = False,human=False):
    modestr = list('rwx'*3)
    def _getmodestr(mode:int):
        mstr = ''
        for i in range(8,-1,-1):
             mstr += modestr[8-i] if mode >> i & 1 else '-'
        return mstr

    def _gethumansite(size:int,):
        #units = ['','K','M','G','T','P']
        units =" KMGTP" # 字面常量
        index = 0
        while size >= 1000 and index + 1 < len(units):
            size = size // 1000
            index += 1
        return "{} {}".format(size,units[index])

    import stat

    def _listdir(path,detail=False,all = False,human=False):
        P = Path(path)
        if not P.exists() or not P.is_dir():
            return
        ret = []
        for f in P.iterdir():
            if not all  and f.name.startswith('.'):
                continue
            if not detail:
                #ret.append((f.name,))
                yield f.name
            else:
                print(type(f), f, f.name)
                st = f.stat()
                typ = stat.filemode(st.st_mode)
                #f.owner()
                mode = _getmodestr(st.st_mode)
                dt = datetime.datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%D %H:%M:%S')
                size = _gethumansite(st.st_size) if human else st.st_size
                #ret.append((typ,f.name,mode,dt,st.st_nlink,st.st_uid,st.st_gid,size))
                yield (mode,st.st_nlink,st.st_uid,st.st_gid,size,dt,f.name)
        #filelist = _listdir(path, detail,all,human)
        #return (sorted(_listdir(path, detail,all,human),key=lambda x:x[-1]))
    #print(sorted(_listdir(path, detail,all,human),key=lambda x:x[-1]))
    yield from sorted(_listdir(path, detail,all,human),key=lambda x:x[-1])


if __name__ == "__main__":
    args = parser.parse_args()  # 解析提供的参数是否满足现在的定义
    print(args)
    print(args.path,args.l,args.a,args.human)
    g = listdir(args.path,args.l,args.a,args.human)
    print(g)
    for x in g:
        print(x)



```

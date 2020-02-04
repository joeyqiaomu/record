## base64 实现Base64编码

```python

alphabet = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def b64encode(src:str):
    ret = bytearray()
    if isinstance(src,str):
        _src = src.encode()
    else:
        return

    length = len(_src)
    print(length)
    offset = 0
    for offset in range(0, length, 3):#每次取三个字节
        triple = _src[offset:offset+3]
        print(triple)
        r = 3 - len(triple) #如果不满足三个字符，凑满足字符
        if r:
            triple = triple + b'\x00'*r
        print(triple)

        x = int.from_bytes(triple, "big")

        for i in range(18,-1,-6):
            index = x >> i & 0x3F
            ret.append(alphabet[index])

        # for i in range(r):
        #     ret[-i-1] = 61
        #if r:
        print(ret)
        if r:
            ret[-r:] = b'=' * r
        print(ret)
    return bytes(ret)


b64encode("abcdc")
```


# **<font color=Red> WSGI web server gateway interface**




```python
from wsgiref.simple_server import make_server,demo_app

return_as = b'abc~~~~~~~~~~'

def app(envrion,start_response):
    start_response("200 OK", [('Content-Type','text/plain; charset=utf-8')])
    return [b'mn~~~~~`',b'ops']

class App:

    def __init__(self,envrion,start_response):
        self.e = envrion
        self.sr = start_response
    def __iter__(self):
        self.sr("200 OK", [('Content-Type','text/plain; charset=utf-8')])
        yield from [b'mn~~~~~`',b'ops']


class Application:

    def __call__(self, envrion,start_response):
        start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
        return []


ws = make_server('127.0.0.1',9999,app)
ws.serve_forever()
```

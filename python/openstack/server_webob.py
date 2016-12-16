from wsgiref.simple_server import make_server
from webob import Request, Response

def application(environ, start_response):
    req = Request(environ)
    res = Response()
    res.status = 200
    res.headerlist = [('Content-Type','text/html')]
    res.body = "<h1>Hello World!<h1>"
    return res(environ, start_response)

httpd = make_server('', 8080, application)  
httpd.serve_forever() 

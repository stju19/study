'using webob to create a simple web server used to monitor a HTTP request'

from wsgiref.simple_server import make_server  
from webob import Request, Response  
from webob.dec import *  
 
@wsgify  
def test(req):  
    res = Response()  
    res.status = 200
    res.body = "<h1>hello World!<h1>stju19"
    return res  
  
#class MyApp:  
#    def __call__(self, environ, start_response):
#        #req = Request(environ)
#        return test(environ, start_response)  
          
#application = MyApp()  

application = test
  
httpd = make_server('', 8081, application)    
httpd.serve_forever()   


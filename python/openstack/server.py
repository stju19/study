#!/usr/bin
'create a simple web server used to monitor a HTTP request'

from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('', 8000, application)

print 'serving HTTP on port 8000...'
httpd.serve_forever()

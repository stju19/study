#!/usr/bin/env python
__author__ = '10183988'
import httplib
import json

class _HTTPClient(object):
    def __init__(self):
        self.client = None

    def connect(self, host, **kwargs):
        if self.client:
            self.client.close()
        self.client = httplib.HTTPConnection(host, timeout=30, **kwargs)

    def request(self, method, url, **kwargs):
        kwargs.setdefault('headers', kwargs.get('headers', {}))
        kwargs['headers']['Accept'] = 'application/json'
        if 'body' in kwargs:
            kwargs['headers']['Content-Type'] = 'application/json'
            kwargs['data'] = json.dumps(kwargs['body'])
            del kwargs['body']

        self.client.request(method, url)
        resp = self.client.getresponse()
        if resp:
            try:
                body = json.loads(resp.read())
            except ValueError:
                body = None
        else:
            body = None

        return resp, body

    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('POST', url, **kwargs)

test = _HTTPClient()
test.connect('10.43.211.62:8080')
resp, body = test.post('/rest/v1/')
# resp, body = test.get('/rest/v1/Drawers/7/ComputeModules/14/')
print resp
print body
print type(body)
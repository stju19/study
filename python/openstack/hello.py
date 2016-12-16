def application(environ, start_responce):
    start_responce('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello World!<h1>'

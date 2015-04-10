#!/usr/bin/env python3

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def greet(request):
    name = request.matchdict['name'] or 'World'
    return Response('Hello %s!' % name)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('root', '/{name:.*}')
    config.add_view(greet, route_name='root')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()

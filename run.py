from math_joke import create_app

def runServer(app, port):
    from gevent.wsgi import WSGIServer
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()

if __name__ == '__main__':
    env = 'dev'
    app = create_app('app.settings.DevConfig' , env=env)
    port = 9527
    runServer(app,port)


import bottle

@bottle.route('/')
def home_page():
        return bottle.template('index',message='hello world')

bottle.debug(True)
bottle.run(host='localhost', port=8080)



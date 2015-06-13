import bottle

@bottle.route('/')
def home_page():
        return "<html><body><b>Hello world</b></body></html>"

@bottle.route('/testpage')
def test_page():
        return 'test page'

# bottle.debug(True)
bottle.run(host='localhost', port=8080)


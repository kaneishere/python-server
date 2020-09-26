from flask import Flask
import flaskext.xmlrpc

app = Flask(__name__)

handler = XMLRPCHandler('api')
handler.connect(app, '/api')

@handler.register
def hello(name="world"):
    if not name:
        raise Fault("unknown_recipient", "I need someone to greet!")
    return "Hello, %s!" % name

app.run()
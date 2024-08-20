"""test Flask with this"""
print("Iniciando")
import pip

try:
    import flask
except ImportError:

    pip.main(["install", "flask"])
    import flask
'''
try:
    import venv
except ImportError:

    pip.main(["install", "venv"])
    import venv
'''

print("linea 21")
try:
    import flask_restful
except ImportError:

    pip.main(["install", "flask_restful"])
    import flask_restful

print("LINEA 28 ")

try:
    import waitress
except ImportError:

    pip.main(["install", "waitress"])
    import waitress

print("LINEA 37")

print("version2127")

from flask import Flask, request

print("linea 43")

##from flask_restful import Resource, Api
import sys
import os
print("linea 36")

##from flask import Flask

try:
    from flask import  render_template
except ImportError:
     
    pip.main(["install","render_template"])

    from flask import  render_template  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main240820c__':
     app.run(debug=True)

app = Flask(__name__)
'''
@app.route("/")
def index():
    return "<h1>Hello!</h1>"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
'''
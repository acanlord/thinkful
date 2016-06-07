from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
	return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    return "Hello {}!".format[:3](name.title())

@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname,lastname):
    return lastname[0:3]+firstname[0:2]

if __name__ == "__main__":
	app.run(host=environ['IP'],
		port=int(environ['PORT']))

def twist(twister):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            print(twister)
            function(*args, **kwargs)
        return wrapper
    return decorator

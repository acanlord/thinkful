from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
	return "Hello World!"

@app.route("/hello/<name>")
def hi_person(name):
    return "Hello {}!".format(name.title())

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

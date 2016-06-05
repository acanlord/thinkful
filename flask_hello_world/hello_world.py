from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
	return "Hello World!"

@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname,lastname):
    return "Your jedi name is " + lastname[0:3]+firstname[0:2]

@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())

if __name__ == "__main__":
	app.run(host=environ['IP'],
		port=int(environ['PORT']))

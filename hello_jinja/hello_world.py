#from flask import Flask
#from os import environ

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
	return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

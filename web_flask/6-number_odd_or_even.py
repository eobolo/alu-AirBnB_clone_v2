#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display Hello HBNB!
/hbnb: display HBNB
You must use the option strict_slashes=False in your route definition
"""


from flask import Flask, url_for, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root_display():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_display():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_display(text):
    text_str = " ".join(text.split("_"))
    return "C {0}".format(text_str)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_display(text="is cool"):
    text_str = " ".join(text.split("_"))
    return "Python {0}".format(text_str)


@app.route("/number/<int:n>", strict_slashes=False)
def number_display(n):
    return "{0} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_display(n):
    return render_template("5-number.html", name=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd_template_display(n):
    outcome = "even" if n%2 == 0 else "odd"
    return render_template(
	"6-number_odd_or_even.html",
	name=n,
	outcome=outcome,
    )

if __name__ == "__main__":
    # specify IP address and port number
    app.run(host="0.0.0.0", port=5000)

from application import app
from flask import render_template, url_for
from application.forms import LoginForm
from werkzeug.utils import cached_property

@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    return render_template("index.html", form = form)

@app.route("/dungeon")
def dungeon():
    return render_template("dungeon.html")

@app.route("/room")
def room():
    return render_template("room.html")
from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/dungeon")
def dungeon():
    return render_template("dungeon.html")

@app.route("/room")
def room():
    return render_template("room.html")
import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "badkey"
messages = []

def add_messages(username, message):
    """Add messages to messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append("({})  {}: {}".format(now, username, message))

def get_all_messages():
    """Get all of messages and seperate with BR"""
    return "<br>".join(messages)

@app.route('/', methods = ["GET", "POST"])
def index():
    """Main Page with instructions"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")

@app.route('/<username>')
def user(username):
    """Display user messages"""
    return "<h1>Welcome, {}</h1>{}".format(username, get_all_messages())

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
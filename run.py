import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to messages list"""
    messages.append("{}: {}".format(username, message))

def get_all_messages():
    """Get all of messages and seperate with BR"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main Page with instructions"""
    return "to send a message use /USERNAME/MESSAGE"

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
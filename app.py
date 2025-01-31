from flask import Flask, render_template, make_response, redirect
from flask_socketio import SocketIO, send, emit
import os

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return "<center><h1>Welcome to Just Google It</h1></center>"

@app.route('/<user>')
def index(user):
    return render_template('index.html', user=user)

@socketio.on("message")
def handleMessage(data):
    emit("new_message",data,broadcast=True)
    
if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5004)



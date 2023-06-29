from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room

from assistant import Assistant

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DyadChurchlessTech'
socketio = SocketIO(app)

assistants = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def on_connect():
    assistant = Assistant()
    assistants[request.sid] = assistant
    socketio.emit('response', {'message': "Hello there! I am Dyad, a virtual assistant."}, room=request.sid)
    join_room(request.sid)

@socketio.on('message')
def on_message(data):
    user_input = data['message']
    assistant = assistants[request.sid]
    response = assistant.complete(user_input)
    socketio.emit('response', {'message': response}, room=request.sid)

@socketio.on('disconnect')
def on_disconnect():
    assistant = assistants.pop(request.sid, None)
    leave_room(request.sid)
    del assistant

if __name__ == '__main__':
    socketio.run(app, debug=True)

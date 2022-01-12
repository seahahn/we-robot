from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room
from chatbot import model
from langdetect import detect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cd_s4p_chatbot!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# 사용자가 보낸 메시지를 받아서 챗봇에게 전달
# 이와 함께 사용자의 채팅창에 사용자가 보낸 메시지 출력하기
@socketio.on('send')
def make_conversation(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    msg = json['message']
    detected = detect(msg)
    room = request.sid
    if detected == 'ko':
        socketio.emit('response', json, to=room) # 사용자 메시지 출력

        chatbot_resp = model.chat(msg) # 챗봇 메시지 요청하기
        # chatbot_resp = "챗봇의 메시지가 도착했다!"
        json = {
            'user_name': 'We-robot',
            'message': chatbot_resp
            }
        socketio.emit('response', json, to=room) # 챗봇 메시지 출력
    else:
        socketio.emit('response', json, to=room) # 사용자 메시지 출력
        json = {
            'user_name': '안내 : ',
            'message': '챗봇과 대화하시려면 한글로 입력해주세요.'
            }
        socketio.emit('response', json, to=room)

# 사용자 입장 시 방 생성하기
@socketio.on('join')
def on_join(data):
    room = request.sid
    join_room(room)
    socketio.emit('user_state', data, to=room)

    json = {
            'user_name': 'We-robot',
            'message': '안녕하세요! 저는 당신을 위한 We-robot 입니다.'
            }
    socketio.emit('response', json, to=room) # 사용자 입장 시 챗봇의 환영 메시지 출력
    print('user in: ' + str(room))

# 사용자 연결 종료 시 방 없애기
@socketio.on('disconnect')
def on_disconnect():
    room = request.sid
    leave_room(room)
    print('user out: ' + str(room))

if __name__ == '__main__':
    socketio.run(app, debug=True)
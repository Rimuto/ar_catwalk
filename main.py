import os
from flask import Flask, render_template, request, g, session, make_response, current_app, redirect, url_for



#cap=cv2.VideoCapture(0)  ##when removing debug=True or using gevent or eventlet uncomment this line and comment the cap=cv2.VideoCapture(0) in gen(json)
app = Flask(__name__)
app.config['SECRET_KEY'] = '78581099#lkjh'
path_to_videos = ['Videos/remote_server_client1.mp4', 'Videos/remote_server_client2.mp4', 'Videos/yH.gif',
                  'Videos/v_01.mov', 'Videos/v_02.mov', 'Videos/AlphaTestVideo.webm']


@app.route('/')
def index():
    video_path = path_to_videos[5]
    return render_template('index.html', video_path=video_path)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)#host="0.0.0.0"
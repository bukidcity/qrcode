from flask import Flask, render_template, Response
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import socket

camera = cv2.VideoCapture(0)
#camera.set(3,640)
#camera.set(4,480)

app = Flask(__name__)


@app.route('/x')
def index():
	return render_template('index.html')

@app.route('/')
def scanner():
	return render_template('html5-qrcode.html')

def gen_frames():  
	while True:
		success, frame = camera.read()  # read the camera frame
		if not success:
			break
		else:
			ret, buffer = cv2.imencode('.jpg', frame)
			for barcode in decode(frame):
				myData = barcode.data.decode('utf-8')
				print(myData)

				#put some traps here	

			frame = buffer.tobytes() #add a gif scanner image html css
			yield (b'--frame\r\n'	
						b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
	return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run( debug=True)
	#app.run(host="0.0.0.0", port = "80", debug=True)
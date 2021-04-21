from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def scanner():
	return render_template('html5-qrcode.html')

if __name__ == '__main__':
	#app.run( debug=True)
	app.run(host="0.0.0.0", port = "80", debug=True)

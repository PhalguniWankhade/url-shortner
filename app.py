from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello flask'

@app.route('/about')
def about():
	return 'The is a url shortner.'

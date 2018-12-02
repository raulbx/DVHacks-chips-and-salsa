import requests
import flask
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/test", methods=['GET', 'POST'])
def receive_message():
    return "Going to the test page"

@app.route("/dashboard", methods=['GET', 'POST'])
def send_response():
    #output = request.get_json()
    print("--Going to the dashboard--")
    return flask.render_template('dashboard.html')
    '''
    return jsonify(
        speech='This is Google god speaking. Dialog flow is working',
        displayText='This is Google god speaking. Dialog flow is working'
    )'''

@app.route("/", methods=['GET', 'POST'])
def index():
	return flask.render_template('index.html')
    
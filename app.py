#!flask/bin/python
from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/hello/<value>')
def hello_world(value):
    response = 'Hello ' + value + ' from ' + str(socket.gethostname())
    return jsonify({'message': response})

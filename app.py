#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello/<value>')
def hello_world(value):
    response = 'Hello ' + value
    return jsonify({'message': response})

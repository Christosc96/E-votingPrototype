import hashlib
import json
from datetime import datetime

from flask import Flask, request
from flask import jsonify
from node import Node
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/vote/odd', methods=['POST'])
def cast_vote_odd():
    # get form params
    data = request.json

    id = data.get('id')
    name = data.get('name')
    surname = data.get('surname')

    vote = data.get('vote')
    vote_id = data.get('vote_id')

    vote_time = datetime.now()
    vote_time = vote_time.strftime("%d-%m-%Y %H:%M:%S")

    # TODO: insert through node
    # insert to witness db ( synchronous, must wait for the isnertion to be complete)

    mNode.insert(vote, vote_id, id, name, surname)

    # insert to other databases( asynchronous, don't wait for the isnertion to be complete)

    b1Node.insert_async(vote, vote_id, id, name, surname)
    b2Node.insert_async(vote, vote_id, id, name, surname)
    b3Node.insert_async(vote, vote_id, id, name, surname)

    resp = jsonify(success=True)
    return resp


@app.route('/vote/even', methods=['POST'])
def cast_vote_even():
    # get form params
    data = request.json

    id = data.get('id')
    name = data.get('name')
    surname = data.get('surname')

    vote = data.get('vote')
    vote_id = data.get('vote_id')

    vote_time = datetime.now()
    vote_time = vote_time.strftime("%d-%m-%Y %H:%M:%S")

    # TODO: insert through node
    # insert to witness db ( synchronous, must wait for the isnertion to be complete)

    mNode.insert(vote, vote_id, id, name, surname)

    # insert to other databases( asynchronous, don't wait for the isnertion to be complete)

    # TODO: Nodes for odd or even dbs

    resp = jsonify(success=True)
    return resp


if __name__ == '__main__':
    mNode = Node('postgres', 'root', 'mNode', mode='sync')
    b1Node = Node('postgres', 'root', 'b1Node', mode='async')
    b2Node = Node('postgres', 'root', 'b2Node', mode='async')
    b3Node = Node('postgres', 'root', 'b3Node', mode='async')

    # TODO: Nodes for odd or even dbs

    app.run(host='127.0.0.1', port=5000, debug=False)

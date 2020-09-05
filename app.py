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
    data = request.form

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

    b1Node.insert_async(vote, vote_id, id, name, surname, test=True)
    b2Node.insert_async(vote, vote_id, id, name, surname, test=True)
    b3Node.insert_async(vote, vote_id, id, name, surname, test=True)

    resp = jsonify(success=True)
    return resp


@app.route('/vote/even', methods=['POST'])
def cast_vote_even():
    # get form params
    data = request.json
    data = request.form


    id = data.get('id')
    name = data.get('name')
    surname = data.get('surname')

    vote = data.get('vote')
    vote_id = data.get('vote_id')

    vote_time = datetime.now()
    vote_time = vote_time.strftime("%d-%m-%Y %H:%M:%S")

    # TODO: insert through node
    # insert to witness db ( synchronous, must wait for the isnertion to be complete)

    m2Node.insert(vote, vote_id, id, name, surname)

    # insert to other databases( asynchronous, don't wait for the isnertion to be complete)

    b4Node.insert_async(vote, vote_id, id, name, surname)
    b5Node.insert_async(vote, vote_id, id, name, surname)
    b6Node.insert_async(vote, vote_id, id, name, surname)

    # TODO: Nodes for odd or even dbs

    resp = jsonify(success=True)
    return resp


if __name__ == '__main__':
    mNode = Node('postgres', 'pass', 'mNode', mode='sync')
    b1Node = Node('postgres', 'pass', 'b1Node', mode='async')
    b2Node = Node('postgres', 'pass', 'b2Node', mode='async')
    b3Node = Node('postgres', 'pass', 'b3Node', mode='async')

    # TODO: Nodes for odd or even dbs 

    m2Node = Node('postgres', 'pass', 'm2Node', mode='sync')
    b4Node = Node('postgres', 'pass', 'b4Node', mode='async')
    b5Node = Node('postgres', 'pass', 'b5Node', mode='async')
    b6Node = Node('postgres', 'pass', 'b6Node', mode='async')

    app.run(host='127.0.0.1', port=5000, debug=False)

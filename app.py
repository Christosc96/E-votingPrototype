from datetime import datetime

from flask import Flask, request
from flask import jsonify
from node import Node
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/vote', methods=['POST'])
def cast_vote():
    # get form params
    id = request.form.get('id')
    name = request.form.get('name')
    surname = request.form.get('surname')

    vote = request.form.get('vote')
    vote_id = request.form.get('vote_id')

    vote_time = datetime.now()
    vote_time = vote_time.strftime("%d-%m-%Y %H:%M:%S")

    # TODO: insert through node
    #insert to witness db ( synchronous, must wait for the isnertion to be complete)

    mNode.insert(vote, vote_id, id, name, surname)

    #insert to other databases( asynchronous, don't wait for the isnertion to be complete)

    b1Node.insert_async(vote, vote_id, id, name, surname)
    b2Node.insert_async(vote, vote_id, id, name, surname)
    b3Node.insert_async(vote, vote_id, id, name, surname)

    resp = jsonify(success=True)
    return resp 



if __name__ == '__main__':

    mNode = Node('postgres', 'pass', 'mNode', mode='sync')
    b1Node = Node('postgres', 'pass', 'b1Node', mode='async')
    b2Node = Node('postgres', 'pass', 'b2Node', mode='async')
    b3Node = Node('postgres', 'pass', 'b3Node', mode='async')
    app.run(host='127.0.0.1',port=5000,debug=False)

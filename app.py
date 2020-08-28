import datetime

from flask import Flask, request

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


if __name__ == '__main__':
    app.run()

#!/usr/bin/python3

from flask import Flask


app = Flask(__name__)


@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'


@app.route('/hello/<username>')  # Dynamic route.
def hello_user(username):
    return 'Why Hello %s!\n' % username


@app.route('/hey/<username>')  # Dynamic route.
def hello_user(username):
    return 'Hey %s!\n It is great to see you!!!' % username


@app.route('/well/<username>')  # Dynamic route.
def hello_user(username):
    return 'Well, well, well %s!\n How have you been?' % username


if __name__ == '__main__':
    app.run(host='0.0.0.0')      # Open for everyone.

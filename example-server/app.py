from pprint import pprint

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    pprint(request.headers)
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
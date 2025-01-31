# -*- coding: utf-8 -*-

from flask import Flask, request, redirect
import json
import controller as co

app = Flask(__name__)
#CORS(app)


@app.route('/', methods=['POST'])
def account():
    content = request.get_json()
    text = content['text']
    #print(text)
    result = co.classi_spam(text)
    return result, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/json/images')
def json_images():
    original = os.listdir('static/images/original')
    thumbs = os.listdir('static/images/thumbs')
    return jsonify([original, thumbs])


if __name__ == '__main__':
    app.run()
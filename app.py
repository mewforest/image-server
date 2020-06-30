from flask import Flask, jsonify, url_for, request, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/json/images')
def json_images():
    json = []
    image_names = os.listdir('static/images/original')
    for index, name in enumerate(image_names):
        json.append({
            'id': index,
            'title': name.replace('.jpg', ''),
            'url': request.url_root + url_for('static', filename=f'images/original/{name}'),
            'thumbnailUrl': request.url_root + url_for('static', filename=f'images/thumbs/{name}'),
        })
    return jsonify(json)


if __name__ == '__main__':
    app.run()
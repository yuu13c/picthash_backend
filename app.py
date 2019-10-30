import os, io
import urllib.request
from flask import Flask, jsonify, request
from PIL import Image
import imagehash

app = Flask(__name__)

@app.route('/digest', methods=['POST'])
def digest():
    # Json
    data = request.json
    url = data['url']

    # img DL
    img_in = urllib.request.urlopen(url).read()
    img_bin = io.BytesIO(img_in)

    # imagehash
    hash = imagehash.dhash(Image.open(img_bin))
    s_hash = str(hash)

    return jsonify({
            'url':url,
            'digest':s_hash
        })

if __name__ == '__main__':
    app.run()
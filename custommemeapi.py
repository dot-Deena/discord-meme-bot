from flask import jsonify, Flask, request
import random

app = Flask(__name__)

# list of diddy memes
memes = [
    "/static/memes/diddy1.png",
    "/static/memes/diddy2.png",
    "/static/memes/diddy3.png",
    "/static/memes/diddy4.png",
    "/static/memes/diddy5.png",
    "/static/memes/diddy6.png",
    "/static/memes/diddy7.png",
    "/static/memes/diddy8.png",
    "/static/memes/diddy9.png",
    "/static/memes/diddy10.png",
]

# route to get single random meme
@app.route('/meme', methods=['GET'])
def get_meme():
    return jsonify({'url': request.host_url + random.choice(memes)})

# route to get customer number of memes
@app.route('/memes/<int:count>', methods=['GET'])
def get_memes(count):
    random_memes = random.sample(memes, min(count, len(memes)))
    return jsonify([{"url":request.host_url + meme} for meme in random_memes])

if __name__ == '__main__':
    app.run(debug=True)

import random
import os
import requests

from collections import defaultdict

from flask import Flask, render_template, abort, request, jsonify

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                './_data/DogQuotes/DogQuotesDOCX.docx',
                './_data/DogQuotes/DogQuotesPDF.pdf',
                './_data/DogQuotes/DogQuotesCSV.csv']

def setup():
    """ Load all resources """
    quotes = defaultdict(list)
    for fi in quote_files:
        quotes[fi] = Ingestor.parse(fi)
    images_path = "./_data/photos/dog/"
    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, fi) for fi in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    random_file_type = random.choice(quote_files)
    quote = random.choice(quotes[random_file_type])
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    try:
        img = "./static/creator.jpg"
        url = request.form.get('image_url')
        content = requests.get(url, stream=True).content
        body = request.form.get("body", "You didn't place a body, so Iron Man Rules")
        author = request.form.get("author", "Iron Man")
        
        with open(img, 'wb') as f:
            f.write(content)

        path = meme.make_meme(img, body, author)
        os.remove(img)

        return render_template('meme.html', path=path)
    except:
        return jsonify({"message": "Invalid Url. Please enter url of a jpg image"}), 400


if __name__ == "__main__":
    app.run(debug=True)

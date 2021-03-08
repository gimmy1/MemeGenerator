import os
import random

from argparse import ArgumentParser

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel

def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None
    
    images = "./_data/photos/dog/" if path is None else path
    
    imgs = []
    for root, _, files in os.walk(images):
        imgs = [os.path.join(root, name) for name in files]
    img = random.choice(imgs)

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)
    
    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path

def dir_path(string):
    if os.path.isdir(string):
        return string
    raise NotADirectoryError("Please enter a valid directory")

if __name__ == "__main__":
    parser = ArgumentParser(prog="meme",
                            description="Meme Me")
    # parser.add_argument("--author", type=str, default=None, help="Who is the author, pal?")
    parser.add_argument("--author", type=str, help="Who is the author, pal?")
    parser.add_argument("--body", type=str, help="Motivate me, pal")
    parser.add_argument("--path", metavar="path", type=dir_path, help="Please provide a directory of images?")
    
    args = parser.parse_args()
    path = args.path
    body = args.body
    author = args.author
    
    print(path, body, author)
    print(generate_meme(path, body, author))

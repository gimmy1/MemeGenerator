# Meme Generation

A simple meme generation tool which can be run as either a cli or webapp.

## Overview

At a high-level, The application interacts with a variety of file types (PDF, CSV, Text, Docx) and load quotes.
Once parsing, it will load, manipulate, and save images with the the quotes overlayed. The application can also accept
dynamic user input through a command-line tool and a webservice.


### Get Started (Mac Users)
1. Git clone
2. `cd` to clone repository
3. `export FLASK_APP=app.py`
4. `brew install poppler`
4. `pip3 install -r requirements.txt`
5. `python3 app.py`

### Tools and Dependencies
* [Python3](https://www.python.org/downloads/)
* [Flask](https://pypi.org/project/Flask/)
* [Homebrew](https://brew.sh/)
* [pdftotext](https://pypi.org/project/pdftotext/)


### To run
1. `cd` to repository

* AS CLI
2. `python3 meme.py --help`
** NOTE Please provide a directory of images


* As Webapp
2. `python3 app.py`
** Open your browser and navigate to http://127.0.0.1:5000/



from flask import Flask, render_template
import csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from ML import RecommendModel

app = Flask(__name__)

# remove stop words like the/a
tfidf = TfidfVectorizer(stop_words='english')

@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/movies/<title>')
def getMovies(title='Joker'):
    movieslist = RecommendModel.get_recommendations(title)
    return render_template('movies.html', movieslist=movieslist)


if __name__ == '__main__' :
    app.run(debug=True)
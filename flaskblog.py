from flask import Flask, render_template
import csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# remove stop words like the/a
tfidf = TfidfVectorizer(stop_words='english')

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/movies')
def getMovies():
        data = pd.read_csv('movies.csv')
        # replace nan with empty string
        data['overview'] = data['overview'].fillna('')
        matrix = tfidf.fit_transform(data['overview'])
        # Compute the cosine similarity matrix
        cosineSim = linear_kernel(matrix, matrix)
        #Construct a reverse map of indices and movie titles
        indices = pd.Series(data.index, index=data['title']).drop_duplicates()

        # GET Recommendations
        index = indices['The Dark Knight Rises']
        # Get the pairwsie similarity scores of all movies with that movie
        simScores = list(enumerate(cosineSim[index]))
        # Sort the movies based on the similarity scores
        simScores = sorted(simScores, key=lambda x: x[1], reverse=True)
        # Get the scores of the 10 most similar movies
        simScores = simScores[1:11]
        # Get the movie indices
        movieIndices = [i[0] for i in simScores]
        # Return the top 10 most similar movies
        print(data['title'].iloc[movieIndices])
        movieslist = list(data['title'].iloc[movieIndices])
        return render_template('movies.html', movieslist=movieslist)


if __name__ == '__main__' :
    app.run(debug=True)
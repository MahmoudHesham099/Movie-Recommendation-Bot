import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

import os
# SET CURRENT DIRECTORY
cd = os.path.dirname(os.path.abspath(__file__))


tfidf = TfidfVectorizer(stop_words='english')
data = pd.read_csv(os.path.join(cd, 'inputs/movies.csv'))
# replace nan with empty string
data['overview'] = data['overview'].fillna('')
matrix = tfidf.fit_transform(data['overview'])
# Compute the cosine similarity matrix
cosineSim = linear_kernel(matrix, matrix)
# Construct a reverse map of indices and movie titles
indices = pd.Series(data.index, index=data['title']).drop_duplicates()


def get_recommendations(title):
    index = indices[title]
    # Get the pairwsie similarity scores of all movies with that movie
    simScores = list(enumerate(cosineSim[index]))
    # Sort the movies based on the similarity scores
    simScores = sorted(simScores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar movies
    simScores = simScores[1:11]
    # Get the movie indices
    movieIndices = [i[0] for i in simScores]
    # Return the top 10 most similar movies
    movieslist = list(data['title'].iloc[movieIndices])
    return movieslist

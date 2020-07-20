import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

import os
# SET CURRENT DIRECTORY
cd = os.path.dirname(os.path.abspath(__file__))


# df1=pd.read_csv(os.path.join(cd, 'inputs/tmdb_5000_credits.csv'))
# df2=pd.read_csv(os.path.join(cd, 'inputs/tmdb_5000_movies.csv'))
#
# tfidf = TfidfVectorizer(stop_words='english')
#
# #Replace NaN with an empty string
# df2['overview'] = df2['overview'].fillna('')
#
# #Construct the required TF-IDF matrix by fitting and transforming the data
# tfidf_matrix = tfidf.fit_transform(df2['overview'])
#
# #Output the shape of tfidf_matrix
# tfidf_matrix.shape
#
# indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()
#
# # Compute the cosine similarity matrix
# cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
# indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()
#
# def get_recommendations(title, cosine_sim=cosine_sim):
#     # Get the index of the movie that matches the title
#     idx = indices[title]
#
#     # Get the pairwsie similarity scores of all movies with that movie
#     sim_scores = list(enumerate(cosine_sim[idx]))
#
#     # Sort the movies based on the similarity scores
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#
#     # Get the scores of the 10 most similar movies
#     sim_scores = sim_scores[1:11]
#
#     # Get the movie indices
#     movie_indices = [i[0] for i in sim_scores]
#
#     # Return the top 10 most similar movies
#     return df2['title'].iloc[movie_indices]
#
#
# print(get_recommendations('Zodiac'))

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

from flask import Flask, render_template, request,redirect,url_for
import csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from ML import RecommendModel
import bot

app = Flask(__name__)



# remove stop words like the/a
tfidf = TfidfVectorizer(stop_words='english')

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/getMovies', methods = ['POST', 'GET'])
def getMovies(title='Zodiac'):

    if request.method == "POST":
        rf = request.form
        print(rf)
        for key in rf.keys():
            title = key
    print(title)
    global SavedMoviesList
    SavedMoviesList = RecommendModel.get_recommendations(title)
    return render_template('movies.html', movieslist=SavedMoviesList)



@app.route('/showMovies', methods = ['GET'])
def showMovies():

    print(SavedMoviesList)

    return render_template('movies.html', movieslist=SavedMoviesList)




@app.route("/get", methods=["POST"])
def chat():
    if request.method == "POST":
        rf = request.form
        for key in rf.keys():
            message = key
        status, response = bot.chat(str(message))
        data = {}

        if status == 0:
            data["reply"] = response
            data["status"] = 'Sucess'
            return data
        else:
            data["reply"] = response
            data["status"] = 'Failed'
            return data


if __name__ == '__main__' :
    app.run(debug=True)


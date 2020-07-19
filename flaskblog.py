from flask import Flask, render_template
import csv
import pandas as pd
import numpy as np
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/movies')
def getMovies():
        data = pd.read_csv('movies.csv')
        movieslist = list(data.values)
        return render_template('movies.html', movieslist=movieslist)


if __name__ == '__main__' :
    app.run(debug=True)
from flask import Flask, render_template, request,redirect,url_for,jsonify

from sklearn.feature_extraction.text import TfidfVectorizer

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
        request_data = request.form.to_dict()
        print(request_data)
        title = request_data['Movies']

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
        request_data = request.form.to_dict()
        print(request_data)
        message = request_data['message']
        print(message)
        status, response = bot.chat(str(message))
        data = {}

        if status == 0:
            data["reply"] = response
            data["status"] = 'Sucess'
            return jsonify(data)
        else:
            data["reply"] = response
            data["status"] = 'Failed'
            return jsonify(data)



if __name__ == '__main__' :
    app.run(debug=True)


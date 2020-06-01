from flask import Flask, render_template, jsonify, request, url_for
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home() :
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def poke() :
    if request.method == 'POST' :
        film = str(request.form['filmFav']).lower()

        def recommend(film) :                     
            filmIndex = dfImdb_clean.index.get_loc(dfImdb_clean[dfImdb_clean.title == film].index[0])
            similarMovies = list(enumerate(similarity_distance[filmIndex]))
            similarMovies = [i for i in similarMovies if i[0] != filmIndex]
            similarMovies = sorted(similarMovies, key=lambda x: x[1], reverse=False)
            
            similarMoviesList = []
            for i in similarMovies[:5]:
                similarMoviesList.append(dfImdb_clean.iloc[i[0]])
                
            dfSimilarMovies = pd.DataFrame(similarMoviesList)
            return [i for i in dfSimilarMovies.index]

        result = recommend(film)
        return render_template('hasil_film.html', result=result, df=dfImdb_clean)

if __name__ == '__main__' :
    similarity_distance = joblib.load('./simDistance')
    dfImdb_clean = joblib.load('./dfImdb_clean')
    app.run(debug = True)
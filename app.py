from flask import Flask, render_template, jsonify, request, url_for
import requests
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home() :
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def film() :
    if request.method == 'POST' :
        film = str(request.form['filmFav']).lower()
        inputYear = str(request.form['filmYear'])
        inputRating = str(request.form['filmRating'])

        if dfImdb_clean.title.str.contains(film.lower()).any() :
            def recommend(film, inputYear, inputRating) :                     
                filmIndex = dfImdb_clean.index.get_loc(dfImdb_clean[dfImdb_clean.title == film].index[0])
                similarMovies = list(enumerate(cos_similarity[filmIndex]))
                similarMovies = [i for i in similarMovies if i[0] != filmIndex]
                similarMovies = sorted(similarMovies, key=lambda x: x[1], reverse=True)

                similarMoviesIndexList = []
                for i in similarMovies:
                    similarMoviesIndexList.append(i[0])
            
                dfSimilarMovies = dfImdb_clean.iloc[similarMoviesIndexList]

                if inputYear == "anyYear" :
                    if inputRating == "anyRating" :
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "three" :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 3.0]
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "five" :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 5.0]
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "seven" : 
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 7.0]
                        top_five = dfSimilarMovies.index[:6]
                    else :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 8.0]
                        top_five = dfSimilarMovies.index[:6]
                elif inputYear == "nineties" :
                    dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.year >= 1990]
                    if inputRating == "anyRating" :
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "three" :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 3.0]
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "five" :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 5.0]
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "seven" : 
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 7.0]
                        top_five = dfSimilarMovies.index[:6]
                    else :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 8.0]
                        top_five = dfSimilarMovies.index[:6]
                elif inputYear == "thousands" :
                    dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.year >= 2000]
                    if inputRating == "anyRating" :
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "three" :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 3.0]
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "five" :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 5.0]
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "seven" : 
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 7.0]
                        top_five = dfSimilarMovies.index[:6]
                    else :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 8.0]
                        top_five = dfSimilarMovies.index[:6]
                else :
                    dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.year >= 2000]
                    if inputRating == "anyRating" :
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "three" :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 3.0]
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "five" :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 5.0]
                        top_five = dfSimilarMovies.index[:6]
                    elif inputRating == "seven" : 
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 7.0]
                        top_five = dfSimilarMovies.index[:6]
                    else :
                        dfSimilarMovies = dfSimilarMovies[dfSimilarMovies.avg_vote >= 8.0]
                        top_five = dfSimilarMovies.index[:6]
            
                return [i for i in top_five]

            result = recommend(film, inputYear, inputRating)
            apiKey = 'fa8dc43324e24b7ebd112927fe4fdffd'

            gambar0_url = requests.get('https://api.themoviedb.org/3/find/{}?api_key={}&language=en-US&external_source=imdb_id'.format(dfImdb_clean.loc[result[0]].imdb_title_id, apiKey))
            gambar1_url = requests.get('https://api.themoviedb.org/3/find/{}?api_key={}&language=en-US&external_source=imdb_id'.format(dfImdb_clean.loc[result[1]].imdb_title_id, apiKey))
            gambar2_url = requests.get('https://api.themoviedb.org/3/find/{}?api_key={}&language=en-US&external_source=imdb_id'.format(dfImdb_clean.loc[result[2]].imdb_title_id, apiKey))
            gambar3_url = requests.get('https://api.themoviedb.org/3/find/{}?api_key={}&language=en-US&external_source=imdb_id'.format(dfImdb_clean.loc[result[3]].imdb_title_id, apiKey))
            gambar4_url = requests.get('https://api.themoviedb.org/3/find/{}?api_key={}&language=en-US&external_source=imdb_id'.format(dfImdb_clean.loc[result[4]].imdb_title_id, apiKey))

            gambar0 = '-' if not gambar0_url.json()['movie_results'] else gambar0_url.json()['movie_results'][0]['poster_path']
            gambar1 = '-' if not gambar1_url.json()['movie_results'] else gambar1_url.json()['movie_results'][0]['poster_path']
            gambar2 = '-' if not gambar2_url.json()['movie_results'] else gambar2_url.json()['movie_results'][0]['poster_path']
            gambar3 = '-' if not gambar3_url.json()['movie_results'] else gambar3_url.json()['movie_results'][0]['poster_path']
            gambar4 = '-' if not gambar4_url.json()['movie_results'] else gambar4_url.json()['movie_results'][0]['poster_path']
        
            return render_template('hasil_film.html', result=result, df=dfImdb_clean, gambar0=gambar0, gambar1=gambar1, gambar2=gambar2, gambar3=gambar3, gambar4=gambar4) 
        
        else :
            return render_template('error.html')

if __name__ == '__main__' :
    dfImdb_clean = joblib.load('./dfImdb_clean')
    cos_similarity = joblib.load('./cosSim')
    app.run(debug = True)

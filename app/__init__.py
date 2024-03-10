from flask import Flask, render_template
import requests
import asyncio

app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/index')
def home():
    return render_template('base.html')

@app.route('/gardening')
def gardening_info():
    return render_template('gardening.html')

@app.route('/cooking')
def cooking_details():
    cookbook=["Betty's cupcakes", "Wilma's Dinosaur steaks", "Fred's afternoon snack", "Barney's sleepy time tea"]
    return render_template('cooking.html', cookbook=cookbook)

@app.route('/sci-fi')
def sci_fi_world():
    url = 'https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc'
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZjRmMTkxNjQ1NGMxNjk2Y2E4NmZmZDE0NDRiMTRhMSIsInN1YiI6IjY1ZWNmMmNlMWFjMjkyMDE4NjY4ZWJkNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vS7qTle2cHBZBUEtnsVxIg57xctHdW0Oo_tGK1TQwl4'
    }
    response = requests.get(url, headers=headers)
    movie_list = []

    if response.status_code == 200:
        movies = response.json()['results']

        for movie in movies:
            if 878 in movie['genre_ids']:
                movie_list.append(movie['original_title'])

    else:
        print(f"Request failed with status code {response.status_code}")

    return render_template('sci_fi.html', title="Sci-Fi Movie List", movie_list=movie_list)



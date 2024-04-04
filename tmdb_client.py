import requests
from flask import Flask


app = Flask(__name__)


def get_popular_movies():
    token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwY2UxNjg4OGI0NGZlZjM4ZDIwMDdjZDEwNDhjYWI2MiIsInN1YiI6IjY2MDFiMzU2NzcwNzAwMDE3YzBmOTE4OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TRhuUz1qAjH3037RxEcujn46ABN1Xs02BnScPtTEbx0"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get('https://api.themoviedb.org//3//movie//popular', headers=headers)
    result = response.json()
    return result


def get_poster_url(poster_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    poster_url = base_url + size + poster_path
    return poster_url


def get_movie_info(title, poster_url):
    movie_info = {'title': title, 'poster_url': poster_url}
    return movie_info


def get_movies(how_many):
    data = get_popular_movies()
    return data['results'][:how_many]



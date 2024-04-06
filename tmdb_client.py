import requests
from flask import Flask


app = Flask(__name__)


API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwY2UxNjg4OGI0NGZlZjM4ZDIwMDdjZDEwNDhjYWI2MiIsInN1YiI6IjY2MDFiMzU2NzcwNzAwMDE3YzBmOTE4OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TRhuUz1qAjH3037RxEcujn46ABN1Xs02BnScPtTEbx0"


def get_movies_list(list_type='popular'):    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
        }
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_path, size='w342'):
    base_url = "https://image.tmdb.org/t/p/"
    poster_url = base_url + size + poster_path
    return poster_url


def get_movie_info(title, poster_url):
    movie_info = {'title': title, 'poster_url': poster_url}
    return movie_info


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data['results'][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)   
    return response.json()["cast"]


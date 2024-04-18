from flask import Flask, render_template, request, redirect, url_for
import tmdb_client

app = Flask(__name__)


AVAILABLE_LISTS = [
    {"name": "Now playing", "value": "now_playing"},
    {"name": "Popular", "value": "popular"},
    {"name": "Top rated", "value": "top_rated"},
    {"name": "Upcoming", "value": "upcoming"},    
]


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {'tmdb_image_url': tmdb_image_url}


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in [list_item['value'] for list_item in AVAILABLE_LISTS]:
        return redirect(url_for('homepage', list_type='popular'))
    
    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template('homepage.html', movies=movies, movie_details='movie_details', available_lists=AVAILABLE_LISTS, active_list=selected_list)


@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    print(cast)
    return render_template('movie_details.html', movie=details, cast=cast)


if __name__ == '__main__':
    app.run(debug=True)
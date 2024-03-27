from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = [{"title": "Film 1", "description": "Opis filmu 1", "image_url": "link_do_obrazka1.jpg"},
    {"title": "Film 2", "description": "Opis filmu 2", "image_url": "link_do_obrazka2.jpg"},
    {"title": "Film 3", "description": "Opis filmu 3", "image_url": "link_do_obrazka3.jpg"},
]
    return render_template('homepage.html', movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
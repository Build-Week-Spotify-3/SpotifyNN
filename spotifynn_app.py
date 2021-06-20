from flask import Flask, render_template, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from spotify_data_model import songs, DB
import random
from forms import SongRaterForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bw_db.sqlite3'
DB.init_app(app)

""" Basic landing page"""
@app.route('/')
def landing_page():
    return render_template('landing_page.html')

""" Select song page will display 10 songs to the user and allow them to rate each of them 1 of 3 ratings"""
@app.route('/select_song', methods=['GET', 'POST'])
def song_input():
    num_songs = songs.query.count()
    # Generate 10 random song IDs from the songs table
    ids = random.sample(range(num_songs), 10)
    ten_song_names = []
    for i in ids:
        name = songs.query.filter_by(id=i).first()
        ten_song_names.append(name.name)

    # Load in the form I made
    """ ISSUE I'M HAVING: form returns only the rating of the first song not all 10"""
    selector = SongRaterForm(request.form)
    if request.method == 'POST':
        return display_songs(selector)

    return render_template('song_selector.html', your_list=ten_song_names, form=selector)

""" Eventually this page will display 10 new songs as recomendations, however currently I am using this as a 
test page to display the ratings the user selected on the previous page"""
@app.route('/display_songs')
def display_songs(selector):
    results = []
    selector_list = selector.data
    return selector_list


if __name__ == '__main__':
    app.run()


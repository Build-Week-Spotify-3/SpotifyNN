from flask import Flask, render_template, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from spotify_data_model import songs, DB, RATINGS
import random
from forms import SongsForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bw_db.sqlite3'
DB.init_app(app)

""" Basic landing page"""
@app.route('/')
def landing_page():
    DB.session.query(RATINGS).delete()
    DB.session.commit()
    return render_template('landing_page.html')

""" Select song page will display 10 songs to the user and allow them to rate each of them 1 of 3 ratings"""
@app.route('/select_song', methods=['GET', 'POST'])
def song_input():
    """ MODEL to replace this chunk of code eventually"""
    num_songs = songs.query.count()
    # Generate 10 random song IDs from the songs table
    ids = random.sample(range(num_songs), 10)
    ten_song_names = {}
    for i in ids:
        name = songs.query.filter_by(id=i).first()
        ten_song_names[name.name] = name.name
    songs_list = []
    for i in ids:
        name = songs.query.filter_by(id=i).first()
        songs_list.append(name.name)

    songs_form = SongsForm(request.form, songs=ten_song_names)

    if request.method == 'POST':
        """ The following section takes the song ratings and names, and stores them in the database in the form of
        a string "song_name rating" """
        """ CURRENT ISSUE: the songs it saves in the database aren't the songs the user selects from - it's as if
        it generates another 10 random songs here. Will leave for now and once model is in will evaluate"""
        songs_ratings = songs_form.songs.data
        ratings = [i['select'] for i in songs_ratings]
        list_strings = []
        for i in range(10):
            list_strings.append(str(songs_list[i]) +' ' + str(ratings[i]))
        ratings = RATINGS(song1=list_strings[0], song2=list_strings[1], song3=list_strings[2], song4=list_strings[3],
                           song5=list_strings[4], song6=list_strings[5], song7=list_strings[6], song8=list_strings[7],
                           song9=list_strings[8], song10=list_strings[9])
        DB.session.add(ratings)
        DB.session.commit()
        return redirect(request.url)

    return render_template('song_selector.html', form=songs_form, ten_song_names=songs_list)

if __name__ == '__main__':
    app.run()


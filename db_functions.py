from spotify_data_model import songs, DB
import pandas as pd
import sqlite3
from flask import Flask

df = pd.read_csv('Data/trimmed_songs.csv')

def insert_encoding(songs_df):
    """ A script that we should run one time that inserts the encodings of each song into our songs table"""
    pass


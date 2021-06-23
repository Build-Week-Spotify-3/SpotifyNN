from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class songs(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.Text, nullable=False)
    encoding = DB.Column(item_type=DB.ARRAY)

class RATINGS(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    song1 = DB.Column(DB.Text, nullable=False)
    song2 = DB.Column(DB.Text, nullable=False)
    song3 = DB.Column(DB.Text, nullable=False)
    song4 = DB.Column(DB.Text, nullable=False)
    song5 = DB.Column(DB.Text, nullable=False)
    song6 = DB.Column(DB.Text, nullable=False)
    song7 = DB.Column(DB.Text, nullable=False)
    song8 = DB.Column(DB.Text, nullable=False)
    song9 = DB.Column(DB.Text, nullable=False)
    song10 = DB.Column(DB.Text, nullable=False)
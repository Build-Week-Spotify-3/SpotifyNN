from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class songs(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    name = DB.Column(DB.Text, nullable=False)
    encoding = DB.Column(item_type=DB.ARRAY)
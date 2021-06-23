from wtforms import Form, StringField, SelectField

class SongRaterForm(Form):
    choices = [('-1', 'Dislike'),
               ('0', 'OK'),
               ('1', 'Like')]
    songs = []
    select = SelectField('Rate this song:', choices=choices)
    select2 = SelectField('Rate this song:', choices=choices, id="test")
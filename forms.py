from wtforms import Form, StringField, SelectField, FormField, FieldList

class SongForm(Form):
    choices = [('-1', 'Dislike'),
               ('0', 'OK'),
               ('1', 'Like')]
    select = SelectField('Rate this song:', choices=choices)

class SongsForm(Form):
    songs = FieldList(FormField(SongForm), min_entries=10)

# class Form2(Form):
#     choices = [('-1', 'Dislike'),
#                ('0', 'OK'),
#                ('1', 'Like')]
#     songs = []
#     select = SelectField('Rate this song:', choices=choices)
#
# class Form3(Form):
#     choices = [('-1', 'Dislike'),
#                ('0', 'OK'),
#                ('1', 'Like')]
#     songs = []
#     select = SelectField('Rate this song:', choices=choices)
#
# class Form4(Form):
#     choices = [('-1', 'Dislike'),
#                ('0', 'OK'),
#                ('1', 'Like')]
#     songs = []
#     select = SelectField('Rate this song:', choices=choices)
#
# class Form5(Form):
#     choices = [('-1', 'Dislike'),
#                ('0', 'OK'),
#                ('1', 'Like')]
#     songs = []
#     select = SelectField('Rate this song:', choices=choices)
#
# class Form6(Form):
#     choices = [('-1', 'Dislike'),
#                ('0', 'OK'),
#                ('1', 'Like')]
#     songs = []
#     select = SelectField('Rate this song:', choices=choices)
#
# class Form7(Form):
#     choices = [('-1', 'Dislike'),
#                ('0', 'OK'),
#                ('1', 'Like')]
#     songs = []
#     select = SelectField('Rate this song:', choices=choices)
#
# class Form8(Form):
#     choices = [('-1', 'Dislike'),
#                ('0', 'OK'),
#                ('1', 'Like')]
#     songs = []
#     select = SelectField('Rate this song:', choices=choices)
#
# class Form9(Form):
#     choices = [('-1', 'Dislike'),
#                ('0', 'OK'),
#                ('1', 'Like')]
#     songs = []
#     select = SelectField('Rate this song:', choices=choices)
#
# class Form10(Form):
#     choices = [('-1', 'Dislike'),
#                ('0', 'OK'),
#                ('1', 'Like')]
#     songs = []
#     select = SelectField('Rate this song:', choices=choices)
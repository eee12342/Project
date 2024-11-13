from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


CONTENT_CHOICES = ["Book", "TV Show", "Movie", "Video Game"]


# FORMS
class ContentType(FlaskForm):
    content_type = SelectField(label='Content Type', choices=CONTENT_CHOICES)
    submit = SubmitField(label="Submit", )
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import ValidationError, DataRequired
from app.models import Users, Problems


class QuestionForm(FlaskForm):
    title = StringField("Question title", validators=[DataRequired()])
    question = TextAreaField("Question content", validators=[DataRequired()])
    version = IntegerField("Version number")
    solution = TextAreaField("Solution", validators=[DataRequired()])
    submit = SubmitField('Submit')

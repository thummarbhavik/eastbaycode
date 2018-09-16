from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, FieldList, FormField
from wtforms.validators import ValidationError, DataRequired
from app.models import Users, Problems

class TestCaseForm(FlaskForm):
    input = TextAreaField("Input", validators=[DataRequired()])


class QuestionForm(FlaskForm):
    title = StringField("Question title", validators=[DataRequired()])
    question = TextAreaField("Question content", validators=[DataRequired()])
    version = IntegerField("Version number")
    solution = TextAreaField("Solution", validators=[DataRequired()])
    testcases = FieldList(FormField(TestCaseForm), min_entries=2)
    submit = SubmitField('Submit')

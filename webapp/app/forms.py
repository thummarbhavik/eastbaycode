from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, FieldList, FormField
from wtforms import DateField, SelectField, SelectMultipleField, widgets
from wtforms.validators import ValidationError, DataRequired
from app.models import Users, Problems

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class TestCaseForm(FlaskForm):
    input = TextAreaField("Input", validators=[DataRequired()])

class ExamplesForm(FlaskForm):
    input = TextAreaField("Input", validators=[DataRequired()])
    output = TextAreaField("Output", validators=[DataRequired()])

class ItemForm(FlaskForm):
    type = SelectField('item type', choices=[('none', 'None'),
                                             ('integer', 'Integer'),
                                             ('float', 'Float'),
                                             ('string', 'String'),
                                             ('list', 'List'),
                                             ('dict', 'Dictionary'),
                                             ('array', 'Array'),
                                             ('tuple', 'Tuple'),
                                             ('set', 'Set'),
                                             ('bool', 'Boolean')])

class ArgsForm(FlaskForm):
    name = StringField('arg name')
    type = SelectField('arg type',
                        choices=[('none', 'None'),
                                 ('integer', 'Integer'),
                                 ('float', 'Float'),
                                 ('string', 'String'),
                                 ('list', 'List'),
                                 ('dict', 'Dictionary'),
                                 ('array', 'Array'),
                                 ('tuple', 'Tuple'),
                                 ('set', 'Set'),
                                 ('bool', 'Boolean')])
    items = FieldList(FormField(ItemForm), min_entries=1)

class PrototypeForm(FlaskForm):
    name = StringField('function name', validators=[DataRequired()])
    type = SelectField('return type', choices=[('none', 'None'),
                                             ('integer', 'Integer'),
                                             ('float', 'Float'),
                                             ('string', 'String'),
                                             ('list', 'List'),
                                             ('dict', 'Dictionary'),
                                             ('array', 'Array'),
                                             ('tuple', 'Tuple'),
                                             ('set', 'Set'),
                                             ('bool', 'Boolean')])
    items = SelectField('return item type', choices=[('none', 'None'),
                                                     ('integer', 'Integer'),
                                                     ('float', 'Float'),
                                                     ('string', 'String'),
                                                     ('list', 'List'),
                                                     ('dict', 'Dictionary'),
                                                     ('array', 'Array'),
                                                     ('tuple', 'Tuple'),
                                                     ('set', 'Set'),
                                                     ('bool', 'Boolean')])
    numArgs = IntegerField('No of args')
    args = FieldList(FormField(ArgsForm), min_entries=2)
    # submit = SubmitField('Submit')

class QuestionForm(FlaskForm):
    title = StringField("Question title", validators=[DataRequired()])
    question = TextAreaField("Question content", validators=[DataRequired()], render_kw={'rows': 6})
    version = IntegerField("Version number")
    solution = TextAreaField("Solution", validators=[DataRequired()])
    # examples = FieldList(FormField(ExamplesForm), min_entries=1)
    # testcases = FieldList(FormField(TestCaseForm), min_entries=2)
    submit = SubmitField('Submit')

class CourseForm(FlaskForm):
    title = StringField("Course title", validators=[DataRequired()])
    startdate = DateField("Start date (mm/dd/yyyy)", format='%m/%d/%Y')
    enddate = DateField("End date (mm/dd/yyyy)", format='%m/%d/%Y')
    semester = StringField("Semester (Fall 2018)")
    submit = SubmitField('Submit')

class AssignmentForm(FlaskForm):
    # problem = SelectMultipleField("Problems")
    problem = MultiCheckboxField("Problems")
    startdate = DateField("Start date (mm/dd/yyyy)", format='%m/%d/%Y')
    enddate = DateField("End date (mm/dd/yyyy)", format='%m/%d/%Y')
    submit = SubmitField('Submit')

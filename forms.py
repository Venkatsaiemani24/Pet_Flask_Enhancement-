from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class PetForm(FlaskForm):
    name = StringField('Pet Name', validators=[DataRequired()])
    age = IntegerField('Pet Age', validators=[DataRequired()])
    type = StringField('Pet Type', validators=[DataRequired()])
    submit = SubmitField('Add Pet')

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[DataRequired(), Length(min=2, max=100)])
    age = IntegerField('Pet Age', validators=[DataRequired()])
    pet_type = SelectField('Pet Type', choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Other', 'Other')], validators=[DataRequired()])
    breed = StringField('Breed (Optional)', validators=[Length(max=100)])
    submit = SubmitField('Add Pet')

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
# from app.models import User, Entry

class AddressForm(FlaskForm):
	address = StringField('Full Address', validators=[DataRequired()])
	submit = SubmitField('Get Geocode')

class WikiEntryForm(FlaskForm):
	entry_author = SelectField('Author', choices = [('ccocuzzo','Chris Cocuzzo Test'),('cocuzzo','Chris Cocuzzo')])
	entry_type = SelectField('Entry Type', choices = [('question','Question'),('article','Article'),('tutorial','Tutorial')])
	entry_body = TextAreaField('Entry Information')
	submit = SubmitField('Submit To Wiki Database')
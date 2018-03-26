from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddressForm(FlaskForm):
	address = StringField('Full Address', validators=[DataRequired()])
	submit = SubmitField('Get Geocode')	
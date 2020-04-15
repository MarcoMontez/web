from flask_wtf import FlaskForm
from wtforms import FloatField,StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class ValueForm(FlaskForm):
	value = FloatField('Predict Value', validators=[DataRequired()])
	submit = SubmitField('Send Value')
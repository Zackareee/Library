from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, FieldList,FormField,RadioField,DecimalField
from wtforms.validators import InputRequired,Optional
from wtforms.fields.html5 import DateField
import os

if os.name == 'nt':
    s = "#"
else:
    s = "-"


class BookForm(FlaskForm):
  name =  StringField(validators=[InputRequired()], render_kw={'class':'form-control', 'placeholder':'One Piece'})
  link =  StringField(render_kw={'class':'form-control', 'placeholder':'https://google'})
  volume = DecimalField(validators=[Optional()],render_kw={'class': 'form-control', 'placeholder':'001'})
  submit = SubmitField('Test', render_kw={'class':'btn btn-primary'})

import os

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField, DecimalField, HiddenField
from wtforms.validators import InputRequired, Optional

if os.name == 'nt':
    s = "#"
else:
    s = "-"


class BookForm(FlaskForm):
  name =  StringField(validators=[InputRequired()], render_kw={'class':'form-control', 'placeholder':'One Piece'})
  link =  StringField(render_kw={'class':'form-control', 'placeholder':'https://google'})
  volume = DecimalField(validators=[Optional()],render_kw={'class': 'form-control', 'placeholder':'001'})
  submit = SubmitField('Submit', render_kw={'class':'btn btn-primary'})

class EditForm(FlaskForm):
  Eid = HiddenField()
  Ename =  StringField(validators=[InputRequired()], render_kw={'class':'form-control', 'placeholder':'One Piece' })
  Evolume = DecimalField(validators=[Optional()],render_kw={'class': 'form-control', 'placeholder':'001'})
  Esubmit = SubmitField('Submit', render_kw={'class':'btn btn-primary'})

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed, FileRequired

class DbUploadForm(FlaskForm):
	csvfile = FileField('Select File', validators=[FileAllowed(['csv'], 'CSV format only')])
	submit = SubmitField('Upload')

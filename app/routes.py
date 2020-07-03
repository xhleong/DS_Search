from flask import render_template, redirect, flash
from app import app
from app.forms import DbUploadForm

def CheckFile(filename):
	return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() == 'csv'


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/upload', methods = ['GET','POST'])
def upload():
	form = DbUploadForm()
	if form.validate_on_submit():
		csvfile = form.csvfile
		if not csvfile.data or not CheckFile(csvfile.data):
			flash('Please select and upload a CSV file')
			return redirect('/upload')
		
	return render_template('upload.html', title='Data Upload', form=form)
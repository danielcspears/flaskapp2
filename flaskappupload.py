from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json

 
UPLOAD_FOLDER = '/Users/danielspears/Downloads/flaskapp2/uploads'
ALLOWED_EXTENSIONS = set(['csv', 'xls', 'xlsx'])

 
application = Flask(__name__)   
 
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@application.route("/")
def home():
    return render_template("dcshome.html")
  
@application.route("/dcsabout")
def about():
    return render_template("dcsabout.html")

@application.route("/dcssuccess")
def success():
	return render_template("success.html")


# @application.route('/chart', methods = ['GET','POST'])          
# def chart_maker():
# 	filename = secure_filename(request.args.get('filename'))
# 	try:
# 		if filename and allowed_filename(filename):
# 			with open(os.path.join(application.config['UPLOAD_FOLDER'], filename)) as f:
# 				colnames=['Date', 'Value']
# 				f  = request.files['file']
# 				x = pd.read_csv(f.stream, names=colnames, header=None)
# 				x['Date'] = pd.to_datetime(x['Date'])
# 				x['Date'] = x['Date'].apply(lambda x: x.strftime('%m%y'))
# 				chart_data = x.to_json(orient='records')
# 				data1 = {'chart_data': chart_data}
# 				return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover "), data1 = data1)
# 	except IOError:
# 		pass
# 	return "Unable to read file"

@application.route('/chart', methods = ['GET','POST'])          
def chart_maker(filename):
		filename = secure_filename(request.args.get('filename'))
		colnames=['Date', 'Value']
		x = pd.read_csv(os.path.join(application.config['UPLOAD_FOLDER']) + filename, names=colnames, header=None, skiprows=1)
		x['Date'] = pd.to_datetime(x['Date'])
		x['Date'] = x['Date'].apply(lambda x: x.strftime('%m%y'))
		chart_data = x.to_json(orient='records')
		data1 = {'chart_data': chart_data}
		return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover "), data1 = data1)





def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@application.route('/upload')
def upload_file1():
    return render_template('dcsupload.html')
    
    
@application.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(url_for('upload_file1'))
        file = request.files['file']
        if file.filename == '':
            #flash('No selected file')
            return redirect(url_for('upload_file1'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
            with open(os.path.join(application.config['UPLOAD_FOLDER'], filename)) as f:
            	file_content = f.read()
            return redirect(url_for('success',filename = file_content))
           
   		###next two lines uploads file to directory###
 #     f = request.files['file']
 #     f.save(secure_filename(f.filename))
 		###next line doesn't upload but reads file directly from open###
#             x = pd.read_excel(data)
#            return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover table table-condensed").replace('<th>','<th style = "background-color: aliceblue">').replace('<tr>','<tr style="text-align: center;">'))
       
if __name__ == "__main__":
    application.run(debug=True)

  
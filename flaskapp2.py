from flask import Flask, render_template, request
from werkzeug import secure_filename
import pandas as pd
import numpy as np
import sys
import os 



 
application = Flask(__name__)      


@application.route("/")
def home():
    return render_template("dcshome.html")
  
@application.route("/dcsabout")
def about():
    return render_template("dcsabout.html")



@application.route('/analysis')
def analysis():
    x = pd.DataFrame(np.random.randint(-20,20,size=(20, 7)), columns=list('ABCDEFG'))
    df = x['A'].mean()
    return render_template("dcsanalysis.html", tables = x.to_html(classes="table table-striped table table-hover table table-condensed").replace('<th>','<th style = "background-color: aliceblue">').replace('<tr>','<tr style="text-align: center;">'), df = df)	
	
@application.route('/upload')
def upload_file1():
    return render_template('dcsupload.html')
	
@application.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        data = request.files.get('file')
        ext = os.path.splitext(data)[-1].lower()
        if not data:
            return "No File"
        if ext == ".csv":
            x = pd.read_csv(data)
   		###next two lines uploads file to directory###
 #     f = request.files['file']
 #     f.save(secure_filename(f.filename))
 		###next line doesn't upload but reads file directly from open###
#             x = pd.read_excel(data)
#            return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover table table-condensed").replace('<th>','<th style = "background-color: aliceblue">').replace('<tr>','<tr style="text-align: center;">'))
            return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover table table-condensed"))
 
if __name__ == "__main__":
  application.run(debug=True)
  
  
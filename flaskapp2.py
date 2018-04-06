from flask import Flask, render_template, request, session
from werkzeug import secure_filename
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json

 
application = Flask(__name__)      


@application.route("/")
def home():
    return render_template("dcshome.html")
  
@application.route("/dcsabout")
def about():
    return render_template("dcsabout.html")


# @application.route('/analysis')
# def analysis():
#     x = pd.DataFrame(np.random.randint(-20,20,size=(20, 7)), columns=list('ABCDEFG'))
#     df = x['A'].mean()
#     return render_template("dcsanalysis.html", tables = x.to_html(classes="table table-striped table table-hover table table-condensed").replace('<th>','<th style = "background-color: aliceblue">').replace('<tr>','<tr style="text-align: center;">'), df = df)	


@application.route('/upload')
def upload_file1():
    return render_template('dcsupload.html')
    

@application.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        data = request.files.get('file')
        if not data:
            return "No File"
        if data.filename.endswith((".csv")):
            colnames=['Date', 'Value'] 
            x = pd.read_csv(data, names=colnames, header=None, skiprows = 1)
           # x.rename(columns={'ASPS': 'Thousands'}, inplace=True)
            x['Date'] = pd.to_datetime(x['Date'])
            x = x[['Date','Value']]
            x['Date'] = x['Date'].apply(lambda x: x.strftime('%m%y'))
            chart_data = x.to_json(orient='records')
            #chart_data = x.to_dict(orient='records')
            #chart_data = json.dumps(chart_data, indent=2)
            data1 = {'chart_data': chart_data}
        else:
            colnames=['Date', 'Value']
            x = pd.read_excel(data, names=colnames, header=None, skiprows = 11)
            x['Date'] = pd.to_datetime(x['Date'])
            x = x[['Date','Value']]
            x['Date'] = x['Date'].apply(lambda x: x.strftime('%m%y'))
            chart_data = x.to_json(orient='records')
            #chart_data = json.dumps(chart_data, indent=2)
            data1 = {'chart_data': chart_data}
            return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover "), data1 = data1)

@application.route('/chart', methods = ['GET', 'POST'])          
def chart_maker(data1):
            return render_template("dcschart.html", data1 = data1)


   		###next two lines uploads file to directory###
 #     f = request.files['file']
 #     f.save(secure_filename(f.filename))
 		###next line doesn't upload but reads file directly from open###
#             x = pd.read_excel(data)
#            return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover table table-condensed").replace('<th>','<th style = "background-color: aliceblue">').replace('<tr>','<tr style="text-align: center;">'))
       
if __name__ == "__main__":
  application.run(debug=True)
  
  
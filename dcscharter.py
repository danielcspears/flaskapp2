from flask import Flask, Blueprint, render_template, request, session
from werkzeug import secure_filename
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json



chart_maker_blueprint = Blueprint('uploader', __name__)
@chart_maker_blueprint.route('/uploader', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        if request.form['action'] == 'Brush':
            data = request.files.get('file')
            skrows = int(request.form['skrows'])
            chart_title = request.form['chart_title']
            if not data:
                return "No File"
            if data.filename.endswith((".csv")):
                colnames=['Date', 'Value'] 
                x = pd.read_csv(data, names=colnames, header=None, skiprows = skrows)
                x['Date'] = pd.to_datetime(x['Date'])
                x = x[['Date','Value']]
                x['Date'] = x['Date'].apply(lambda x: x.strftime('%m%y'))
                chart_data = x.to_json(orient='records')
                #chart_data = x.to_dict(orient='records')
                #chart_data = json.dumps(chart_data, indent=2)
                data1 = {'chart_data': chart_data}
            else:
                colnames=['Date', 'Value']
                x = pd.read_excel(data, names=colnames, header=None, skiprows = skrows)
                x['Date'] = pd.to_datetime(x['Date'])
                x = x[['Date','Value']]
                x['Date'] = x['Date'].apply(lambda x: x.strftime('%m%y'))
                chart_data = x.to_json(orient='records')
                #chart_data = json.dumps(chart_data, indent=2)
                data1 = {'chart_data': chart_data}
    ###next two lines uploads file to directory###
    #           f = request.files['file']
    #           f.save(secure_filename(f.filename))
    #           return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover table table-condensed").replace('<th>','<th style = "background-color: aliceblue">').replace('<tr>','<tr style="text-align: center;">'))          
            return render_template("dcsanalysis3.html", tables = x.to_html(classes="table table-striped table table-hover "), data1 = data1, chart_title = chart_title)
        else:
            data = request.files.get('file')
            skrows = int(request.form['skrows'])
            chart_title = request.form['chart_title']
            if not data:
                return "No File"
            if data.filename.endswith((".csv")):
                colnames=['Date', 'Value'] 
                x = pd.read_csv(data, names=colnames, header=None, skiprows = skrows)
                x['Date'] = pd.to_datetime(x['Date'])
                x = x[['Date','Value']]
                x['Date'] = x['Date'].apply(lambda x: x.strftime('%m%y'))
                chart_data = x.to_json(orient='records')
                #chart_data = x.to_dict(orient='records')
                #chart_data = json.dumps(chart_data, indent=2)
                data1 = {'chart_data': chart_data}
            else:
                colnames=['Date', 'Value']
                x = pd.read_excel(data, names=colnames, header=None, skiprows = skrows)
                x['Date'] = pd.to_datetime(x['Date'])
                x = x[['Date','Value']]
                x['Date'] = x['Date'].apply(lambda x: x.strftime('%m%y'))
                chart_data = x.to_json(orient='records')
                #chart_data = json.dumps(chart_data, indent=2)
                data1 = {'chart_data': chart_data}
    ###next two lines uploads file to directory###
    #           f = request.files['file']
    #           f.save(secure_filename(f.filename))
    ###next line doesn't upload but reads file directly from open###
    #           x = pd.read_excel(data)
    #           return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover table table-condensed").replace('<th>','<th style = "background-color: aliceblue">').replace('<tr>','<tr style="text-align: center;">'))          
            return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover "), data1 = data1, chart_title = chart_title)
            
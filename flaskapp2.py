from flask import Flask, render_template, request, session
from werkzeug import secure_filename
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json
from dcscasenote import case_note_blueprint
from dcscharter import chart_maker_blueprint


application = Flask(__name__)      
application.register_blueprint(case_note_blueprint)
application.register_blueprint(chart_maker_blueprint)


@application.route("/")
def home():
    return render_template("dcshome.html")


  
@application.route("/dcsabout")
def about():
    return render_template("dcsabout.html")



@application.endpoint('static')
def static(filename):
    static_url = application.config.get('STATIC_URL')

    if static_url:
        return redirect(urljoin(static_url, filename))

    return application.send_static_file(filename)


# @application.route('/analysis')
# def analysis():
#     x = pd.DataFrame(np.random.randint(-20,20,size=(20, 7)), columns=list('ABCDEFG'))
#     df = x['A'].mean()
#     return render_template("dcsanalysis.html", tables = x.to_html(classes="table table-striped table table-hover table table-condensed").replace('<th>','<th style = "background-color: aliceblue">').replace('<tr>','<tr style="text-align: center;">'), df = df)	


@application.route('/upload')
def upload_file1():
    return render_template('dcsupload.html')
    

    
@application.route('/chart', methods = ['GET', 'POST'])          
def chart_maker(data1):
            return render_template("dcschart.html", data1 = data1)


    
@application.route('/form', methods = ['GET', 'POST'])          
def f_maker():
            return render_template("form.html")


    

if __name__ == "__main__":
    application.run(debug=True)
  
from flask import Flask, render_template, request, session
from werkzeug import secure_filename
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json
import random
from srttemp import template1, template2, template3, template4, template5, template6, template7, boom1, boom2, boom3, boom4, doom1, doom2, doom3, doom4
 
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
    

@application.route('/uploader', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        data = request.files.get('file')
        skrows = int(request.form['skrows'])
        chart_title = request.form['chart_title']
        if not data:
            return "No File"
        if data.filename.endswith((".csv")):
            colnames=['Date', 'Value'] 
            x = pd.read_csv(data, names=colnames, header=None, skiprows = skrows)
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
            x = pd.read_excel(data, names=colnames, header=None, skiprows = skrows)
            x['Date'] = pd.to_datetime(x['Date'])
            x = x[['Date','Value']]
            x['Date'] = x['Date'].apply(lambda x: x.strftime('%m%y'))
            chart_data = x.to_json(orient='records')
            #chart_data = json.dumps(chart_data, indent=2)
            data1 = {'chart_data': chart_data}
        return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover "), data1 = data1, chart_title = chart_title)

    
    
@application.route('/chart', methods = ['GET', 'POST'])          
def chart_maker(data1):
            return render_template("dcschart.html", data1 = data1)




@application.route('/casenote', methods = ['POST'])          
def case_note():
    casenote = {}
    if request.method == 'POST':
        casenote['firstname'] = request.form['firstname'].capitalize()
        casenote['lastname'] = request.form['lastname'].capitalize()
        casenote['job_title'] = request.form['job_title']
        casenote['des_title'] = request.form['des_title']
        casenote['gender'] = request.form['gender'].lower()
        casenote['company'] = request.form['company'].capitalize()
        casenote["industry"] =  request.form['industry'].lower()
        casenote['years'] = int(request.form['years'])
        casenote["hour_wage"] = float(request.form['hour_wage'])
        casenote["exp_wage"] = float( request.form['exp_wage'])
        casenote["referrals"] = request.form['referrals'].casefold()
        casenote["strengths"] = request.form.getlist('strength')
        casenote["strengths"] = str(", ".join(casenote["strengths"]))
        casenote["barriers"] = request.form.getlist('barrier')
        casenote["barriers"] = str(", ".join(casenote['barriers']))
        casenote["comments"] = request.form['comments'].capitalize()
        casenote["zip"] = int(request.form['zipcode'])
        casenote["relocate"] = request.form.getlist('willing')
        
        if not casenote['relocate']:
            casenote['relocate']="no"
        

        
        if casenote['lastname'].endswith(('s')):
            casenote['poss'] = casenote['lastname'] +"'"
        elif casenote['lastname'].endswith(('z')):
            casenote['poss'] = casenote['lastname'] +"'"
        else:
            casenote['poss'] = casenote['lastname'] +"'s"

        if casenote['gender'] == "male":
            casenote['gen'] = "Mr. " 
        else:   
            casenote['gen'] = "Ms. " 

        if casenote['gender'] == "male":
            casenote['gen1'] = "his "
        else:   
            casenote['gen1'] = "her "

        if casenote['gender'] == "male":
            casenote['gen2'] = "He "
        else:   
            casenote['gen2'] = "She "


        if casenote['job_title'].endswith(('^[aeiou].*')):
            casenote['indef'] = " as an "
        else:
            casenote['indef'] = " as a "


        if casenote['des_title'].endswith(('^[aeiou].*')):
            casenote['indef'] = " as an "
        else:
            casenote['indef'] = " as a "    


        if casenote['job_title'] == casenote['des_title']:
            casenote['sent'] = "will continue looking for " + casenote['indef'] + casenote['des_title']
        else:
            casenote['sent'] = "is looking to transition to another occupation"


        if casenote['hour_wage'] == casenote['exp_wage']:
            casenote['wag'] = "has expectations of earning around the same wage of"
        elif casenote['hour_wage'] < casenote['exp_wage']:
            casenote['wag'] = "has expectations of earning a higher wage of"
        else:
            casenote['wag'] =  "would like to retain a strategic open/negotiable position regarding future salary expectations.  "


        if  not casenote['referrals']:
            casenote['refs'] = "No referrals were made at this service point."
        else:
            casenote['refs'] = "A job referral was made to:  " + casenote['referrals']


        if not casenote['barriers']:
            casenote['bars'] = "No barriers were identified in this assessment."
        else:
            casenote['bars'] = "The following barriers were identified during the course of this assessment: " + casenote['barriers']

        if not casenote['strengths']:
            casenote['stren'] = "Easily identifiable strengths proved elusive in this discovery process."
        else:
            casenote['stren']="The following strengths were identified during the course of this assessment: " + casenote['strengths']                     +"."

       
        if casenote['relocate'] == 'yes':
            casenote['zipc'] = casenote['gen2'] + " is willing to relocate for the right position but would prefer opportunities within a                 25 mile radius of " + str(casenote['zip']) +"."
        else:
            casenote['zipc']= casenote['gen2'] + " is not willing to relocate and is searching for job opportunities within a 25 mile                     radius of " + str(casenote['zip']) +"."

            
#        template1 = '''This is temp1 <br> %(strengths)s'''
#        template2 = '''This is temp2 <br>%(strengths)s'''
#        template3 = '''This is temp3 <br>%(strengths)s'''
#        boom1 = '''This is boom1<br>'''
#        boom2 = '''This is boom2<br>'''
#        boom3 = '''This is boom3<br>'''
#        doom1 = '''This is doom1<br>'''
#        doom2 = '''This is doom2<br>'''
#        doom3 = '''This is doom3<br>'''
#        
#        x = random.randint(1,9)
#        y = random.randint(1,3)
#        z = random.randint(1,3)
#
#        if y == 1:
#            doome = doom1
#        elif y == 2:
#            doome = doom2
#        elif y ==3:
#            doome = doom3
#        else:
#            doome = doom4
#        
#
#        if z == 1:
#            boome = boom1
#        elif z == 2:
#            boome = boom2
#        else:
#            boome = boom3
#
#        if x <= 3:
#            lettuce = ((template1 % casenote) +  (doome % casenote) + (boome % casenote))
#        elif x <= 6 & x >= 4:
#            lettuce = ((template2 % casenote)+(doome % casenote)+ (boome % casenote))
#        else:
#            lettuce = ((template3 % casenote)+(doome % casenote)+ (boome % casenote))
#        
#        




        x = random.randint(1,21)
        y = random.randint(1,4)
        z = random.randint(1,3)

        if y == 1:
            doome = doom1
        elif y == 2:
            doome = doom2
        elif y == 3:
            doome = doom3
        else:
            doome = doom4

        if z == 1:
            boome = boom1
        elif z == 2:
            boome = boom2
        elif z== 3:
            boome = boom3
        else:
            boome = boom4

        if x <= 3:
            lettuce = ((template1 % casenote) +(doome % casenote)+ (boome % casenote))
        elif x <= 6 & x >= 4:
            lettuce = ((template2 % casenote)+(doome % casenote)+ (boome % casenote))
        elif x <= 9 & x >= 7:
            lettuce = ((template3 % casenote)+(doome % casenote)+ (boome % casenote))
        elif x <= 12 & x >= 10:
            lettuce = ((template4 % casenote)+(doome % casenote)+ (boome % casenote))
        elif x <= 15 & x >= 13:
            lettuce = ((template5 % casenote)+(doome % casenote)+ (boome % casenote))
        elif x <= 18 & x >= 16:
            lettuce = ((template6 % casenote)+(doome % casenote)+ (boome % casenote))
        else:
            lettuce = ((template7 % casenote)+(doome % casenote)+ (boome % casenote))

    return render_template("makenote.html", casenote=casenote, lettuce = lettuce)

        
        
@application.route('/form', methods = ['GET', 'POST'])          
def f_maker():
            return render_template("form.html")


    
    
    
###next two lines uploads file to directory###
#     f = request.files['file']
#     f.save(secure_filename(f.filename))
###next line doesn't upload but reads file directly from open###
#             x = pd.read_excel(data)
#            return render_template("dcsanalysis2.html", tables = x.to_html(classes="table table-striped table table-hover table table-condensed").replace('<th>','<th style = "background-color: aliceblue">').replace('<tr>','<tr style="text-align: center;">'))


if __name__ == "__main__":
    application.run(debug=True)
  
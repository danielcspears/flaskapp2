from flask import Flask, Response, render_template, request, jsonify, session, Response, flash
import json
from wtforms import TextField, SelectField,Form, validators
from werkzeug import secure_filename
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from states import states

from jobs import jobs
from flask_sqlalchemy import SQLAlchemy 

application = Flask(__name__)   
application.config.update(dict(
    DEBUG=True,
))

from sqlalchemy import *
from sqlalchemy import MetaData, Table
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
 

    
class SearchForm(Form):
    autojob = TextField('Enter Job Title',[validators.Required("Please Enter the First Job Title:")], id='job_autocomplete')
    autojob2 = TextField('Enter Job Title',[validators.Required("Please Enter the Second Job Title:")], id='job_autocomplete1')
    autojob3 = TextField('Enter Job Title:', id='job_autocomplete2')
    company = TextField('Enter Company Name:', id ="company")
    compcity = TextField('Enter Company City:', id ="compcity")
    compstate = SelectField('Enter Company State:',choices=states.items(),  default='LA')
    compyears = TextField('Enter Years Worked:  (ex: 1985-1888)', id ="compyears")
    company2 = TextField('Enter Company Name:', id ="company2")
    compcity2 = TextField('Enter Company City:', id ="compcity2")
    compstate2 = SelectField('Enter Company State:',choices=states.items(), default='LA')
    compyears2 = TextField('Enter Years Worked:', id ="compyears2")
    company3 = TextField('Enter Company Name:', id ="company3")
    compcity3 = TextField('Enter Company City:', id ="compcity3")
    compstate3 = TextField('Enter Company State:', id ="compstate3")
    compyears3 = TextField('Enter Years Worked:', id ="compyears3")
    
@application.route('/_autocomplete', methods=['GET'])
def autocomplete():
    return Response(json.dumps(jobs), mimetype='application/json')

@application.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm(request.form)
    return render_template("html5.html", form=form)


from sqlalchemy import *
from sqlalchemy import MetaData, Table
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

db_name = "tasksx.db"
table_name = "TASK"

engine = create_engine("sqlite:///%s" % db_name, execution_options={"sqlite_raw_colnames": True})
metadata = MetaData(bind=engine)  

Base = declarative_base(engine)

class Tasks(Base):
    __tablename__ = table_name
    __table_args__ = {'autoload': True}
    id = Column(Integer, primary_key=True)

def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == "__main__":
    session = loadSession()
    application.secret_key = 'super secret key'
    application.config['SESSION_TYPE'] = 'filesystem'


@application.route("/joblook", methods = ['POST'])
def job_look():
    form = SearchForm(request.form)
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('html5.html', form = form)
        else:
            jobname = request.form['autojob']
            company = request.form['company'].title()
            compcity = request.form['compcity'].title()
            compstate = request.form['compstate']
            compyears = request.form['compyears']
            jobname2 = request.form['autojob2']
            company2 = request.form['company2'].title()
            compcity2 = request.form['compcity2'].title()
            compstate2 = request.form['compstate2']
            compyears2 = request.form['compyears2']
    #        jobname = request.form['autocomp3']
    #        company3 = request.form['company3']
    #        compcity3 = request.form['compcity3']
    #        compstate3 = request.form['compstate3']
    #        compyears3 = request.form['compyears3']
    # 

            qry = session.query(Tasks.Task).filter(Tasks.Job.ilike('%'+jobname+'%'))
            results =  [item[0] for item in qry.all()]
            
            bullet = "<li class=\"list-group-item\">"
            msg = bullet+"<li class=\"list-group-item\">".join([str(i) for i in results])

            qry2 = session.query(Tasks.Task).filter(Tasks.Job.ilike('%'+jobname2+'%'))
            results2 =   [item[0] for item in qry2.all()]
            bullet = "<li class=\"list-group-item\">"
            msg2 = bullet + '<li class="list-group-item">'.join([str(i) for i in results2])

    return render_template("makeresu.html", results=msg, jobname = jobname, company=company, compcity=compcity, compstate= compstate, compyears=compyears, jobname2=jobname2,company2=company2, compcity2=compcity2, compstate2= compstate2, compyears2=compyears2, results2 = msg2)


if __name__ == '__main__':
    application.run(debug=True)
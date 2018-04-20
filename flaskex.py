# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, session, jsonify
from werkzeug import secure_filename
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import json
from jobs import jobs
from flask_sqlalchemy import SQLAlchemy 

application = Flask(__name__)   
application.config.update(dict(
    DEBUG=True,
))



@application.route("/")
def index():
    return render_template("html5.html") # render the page

#@application.route("/search")
#def search():
#	text = request.args['searchText'] # get the text to search for
#	# create an array with the elements of jobs that contains the string
#	# the case is ignored
#	result = [c for c in jobs if str(text).lower() in c.lower()]
#	# return as JSON
#	return json.dumps({"results":result}) 



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
#    res = session.query(Tasks).all()
#    print (res[1].Task)

#for instance in session.query(Tasks).order_by(Tasks.id):
#    print(instance.Job, instance.Task)

#@application.route("/joblook", methods = ['POST'])
#def job_look():
#    if request.method == 'POST':
#        filename = request.form['Job']
##    result = session.query.with_entities(Tasks.Job, Tasks.Tasks)).filter(Tasks.Job.ilike('%'+filename+'%'))
##        qry = session.query(Tasks.Job, Tasks.Task).filter(Tasks.Job.ilike('%'+filename+'%'))
#        qry = session.query(Tasks.Task).filter(Tasks.Job.ilike('%'+filename+'%'))
#        results = [item[0] for item in qry.all()]
##        df = pd.DataFrame([results])
#        msg = '<br>'.join([str(i) for i in results])
#    return render_template("makeresu.html", results=msg)

@application.route("/autocomplete", methods=["GET"])
def autocomplete():
    results = []
    search = request.args.get("autocomplete")
    for mv in session.query(Tasks.Task).filter(Tasks.Job.like('%'+str(search)+'%')).all():
        results.append(mv[0])
    return jsonify(json_list=results) 


if __name__ == "__main__":
    application.run()
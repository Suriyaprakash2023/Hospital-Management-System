from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy






# MY db connection

app = Flask(__name__)
app.config['SECRET_KEY']="e567890bcsmcdfq8977iyghj"
# app.config['SQLALCHEMY_DATABASE_URL']='mysql://username:password@localhost/databas_table_name'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hospital.db'
db=SQLAlchemy(app)
app.app_context().push()

from hospital import routes
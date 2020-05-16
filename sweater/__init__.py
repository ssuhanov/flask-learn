from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# for PostgreSQL:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://user_name:password@host(localhost)/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fl_learn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from sweater import models, routes


# db.create_all()

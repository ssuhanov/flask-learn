from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = 'some_secret_salt'
# for PostgreSQL:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://user_name:password@host(localhost)/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fl_learn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)


from sweater import models, routes


# db.create_all()

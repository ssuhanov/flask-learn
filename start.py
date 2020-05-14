from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# for PostgreSQL:
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://user_name:password@host(localhost)/db_name'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fl_learn.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# db.create_all()


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)

    def __init__(self, text, tags):
        self.text = text.strip()
        self.tags = [
            Tag(text=tag.strip()) for tag in tags.split(',')
        ]


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))


# @app.before_first_request
# def create_tables():
#     db.create_all()


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/main', methods=['GET'])
def main():
    return render_template('main.html', messages=Message.query.all())


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    db.session.add(Message(text, tag))
    db.session.commit()

    return redirect(url_for('main'))

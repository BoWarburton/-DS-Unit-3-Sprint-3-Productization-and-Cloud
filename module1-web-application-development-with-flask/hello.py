#!/usr/env/bin Python

# def hello():
#     return "Hello World!"

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DB = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////hello.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(app)


class Visit(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    count = DB.Column(DB.Integer)

    def __init__(self):
        self.count = 0


@app.route('/')
def hello():
    v = Visit.query.first()
    if not v:
        v = Visit()
        v.count += 1
        DB.session.add(v)
    v.count += 1
    DB.session.commit()
    return v.count


if __name__ == "__main__":
    app.run(debug=True)

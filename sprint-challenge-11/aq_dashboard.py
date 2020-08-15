"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import openaq

APP = Flask(__name__)
api = openaq.OpenAQ()

APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)

@APP.route('/')
def root():
    """Base view."""
    # status, body = api.measurements(city='Los Angeles', parameter='pm25')
    # return str(body)
    # create a list of tuples
    # my_list = []
    # for i in range(len(body['results'])):
    #     my_list.append(((body['results'][i]['date']['utc']), (body['results'][i]['value'])))
    # return str(my_list)
    Record.query.filter(Record.value < 10).all()

class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '[id {} datetime {} value {}]'.format(self.id, self.datetime, self.value)

@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
#    db_record = Record(id=1, datetime=body['results'][0]['date']['utc'], value=body['results'][0]['value'])
#    DB.session.add(db_record)
    for i in range(len(body['results'])):
        db_record = Record(id=i, datetime=body['results'][i]['date']['utc'], value=body['results'][i]['value'])
        DB.session.add(db_record)
    DB.session.commit()
    return 'Data refreshed!'

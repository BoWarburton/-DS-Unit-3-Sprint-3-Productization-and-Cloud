""" Sprint Challenge OpenAQ Air Quality Dashboard with Flask
The main route return a dashboard page with three buttons:
Cities is the stretch goal for part 2, add another interesting request
Refresh pulls fresh data and replaces the existing data
10+ shows datetime and readings where PM 2.5 is >= 10"""

"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import openaq


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.init_app(app)
    api = openaq.OpenAQ()

    @app.route('/')
    def root():
        return render_template('base.html', title='Home', cities=get_api_cities())

    #     return """<!DOCTYPE html>

    # """

    @app.route('/risky')
    def risky():
        """Datetime, reading where value >= 10"""
        return 'Potentially risky PM2.5 readings<br />' \
               '{}'.format(Record.query.filter(Record.value >= 10).all())

    @app.route('/aq')
    def get_api_data(city='Los Angeles', parameter='pm25'):
        status, body = api.measurements(city=city, parameter=parameter)
        my_list = []
        for date, result in zip(body['results'], body['results']):
            my_list.append(((date['date']['utc']), (result['value'])))
        return my_list

    class Record(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        datetime = db.Column(db.String(25))
        value = db.Column(db.Float, nullable=False)

        def __repr__(self):
            return '-Time {} Reading {}-<br />'.format(self.datetime, self.value)

    @app.route('/refresh')
    def refresh():
        """Pull fresh data from Open AQ and replace existing data."""
        db.drop_all()
        db.create_all()
        new_data = get_api_data()
        for result in new_data:
            db_record = Record(datetime=result[0], value=result[1])
            DB.session.add(db_record)
        db.session.commit()
        return 'Data refreshed!'

    @app.route('/cities')
    def get_api_cities(country="NL", limit=50):
        """ Returns list of dictionaries with city, country, count, number of locations """
        status, body = api.cities(country=country, limit=limit)
        cities_list = []
        for city in body['results']:
            cities_list.append(city['name'])
        return str(cities_list)

    return app

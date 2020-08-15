"""SQLAlchemy models and utility functions for aq_dashboard"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Record(DB.Model):
    """Time and air pollution level for Los Angeles, Costa Rica"""
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '[id {} datetime {} value {}]'.format(self.id, self.datetime, self.value)


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
from app.models import app, database
from app.queries import get_data
from flask import request, jsonify
from datetime import datetime


database_session = database.session


@app.route('/analytics', methods=['GET'])
def analytics():
    """
        Endpoint to calculate daily sales analytics for the provided dataset.
    """
    date = request.args.get('date') or '2019-08-01'

    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError as e:
        return "Incorrect date format, please use YYYY-MM-DD"

    response = get_data(database_session, date)
    return jsonify(response)

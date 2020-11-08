from app.models import app, database
from app.queries import get_data
from flask import request, jsonify
from datetime import datetime


database_session = database.session


@app.route("/analytics", methods=["GET"])
def analytics():
    """
        Endpoint to calculate daily sales analytics for the provided dataset. If the provided date can be mapped to
        the YYYY-MM-DD format, the data will be processed. Otherwise, the endpoint will return an incorrect date format
        message.
    """
    date = request.args.get("date") or "2019-08-01"

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError as e:
        return jsonify("Incorrect date format, please use YYYY-MM-DD")

    response = get_data(database_session, date)
    return response

import unittest
from app.routes import app, database
from app.queries import customers, aggregated_metrics, get_data


date = "2019-08-01"


class TestApi(unittest.TestCase):
    def setUp(self):
        """
        Function called when the class is initialized.
        """
        self.session = database.session
        self.app = app

        with app.app_context():
            self.get_data_response = get_data(self.session, date)
            self.aggregated_metrics_response = aggregated_metrics(self.session, date)
            self.customer_response = customers(self.session, date)

    def test_endpoint_analytics(self):
        """
        Testing the database functions'. Assert statements that must be true.
        """
        assert self.get_data_response.status_code == 200, "Wrong status code."
        assert self.get_data_response.json != {}, "Empty response"
        assert (
            len(self.aggregated_metrics_response) == 6
        ), "incorrect query response length"
        assert self.aggregated_metrics_response[3] >= 0, "total discount must be >= 0"
        assert self.customer_response >= 0, "customers must be an integer that's > 0"
        assert type(self.customer_response) == int, "customers must be an integer"

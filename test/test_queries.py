import unittest
import os, sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.routes import app, database
from app.queries import customers, aggregated_metrics, get_data


date = '2019-08-01'


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
        import pdb; pdb.set_trace()

    def test_endpoint_analytics(self):
        """
        Testing the database functions'.
        """
        assert self.get_data_response.status_code == 200, "Wrong status code."
        assert self.get_data_response.json != {}, "Empty response"
        assert len(self.aggregated_metrics_response) == 6, "incorrect query response length"
        assert self.aggregated_metrics_response[3] >= 0, "total discount must be >= 0"

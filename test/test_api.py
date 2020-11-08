import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.routes import app


class TestApi(unittest.TestCase):
    def setUp(self):
        """
        Function called when the class is initialized. Generates responses using the application test client for
        various endpoint inputs.
        """
        test_app = app.test_client()
        self.response_no_date_given = test_app.get('/analytics')
        self.response_date_given = test_app.get('/analytics?date=2019-08-01')
        # Try a Malformed date
        self.response_bad_date_given = test_app.get('/analytics?date=20219-028-222')

    def test_endpoint_analytics(self):
        """
        Testing the endpoint '/analytics' for combinations of date types.
        """
        assert self.response_no_date_given.status_code == 200, "Wrong status code."
        assert len(self.response_no_date_given.json) > 0, "Ensure data is returned"
        assert self.response_no_date_given.content_type == 'application/json', "Check content_type"
        assert self.response_date_given.status_code == 200, "Wrong status code."
        assert len(self.response_date_given.json) > 0, "Ensure data is returned"
        assert self.response_date_given.content_type == 'application/json', "Check content_type"
        assert type(self.response_bad_date_given.get_data()) == bytes


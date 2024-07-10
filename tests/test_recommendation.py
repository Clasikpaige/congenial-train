import unittest
import json
from recommendation.api.recommendation_api import app

class RecommendationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_recommendations(self):
        response = self.app.get('/recommend?user_id=1')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)

    def test_invalid_user_id(self):
        response = self.app.get('/recommend?user_id=9999')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)  # Depending on how your model handles unknown users

if __name__ == '__main__':
    unittest.main()

from ums import app
import unittest
import json

class TestUMS(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_add_user(self):
        tester = app.test_client(self)
        response = tester.post("/add_users", data=dict(firstName="Mike", lastName="Chen", email="mikechen@gmail.com", dob="1234567892"), follow_redirects=True)
        self.assertEqual(response.status_code, 302)

    def test_update_user(self):
        tester = app.test_client(self)
        response = tester.post("/update_users", data=dict(userID="1", firstName="Mike", lastName="Chen", email="mikechen@gmail.com", dob="1234567892"), follow_redirects=True)
        self.assertEqual(response.status_code, 302)


if __name__ == "__main__":
    unittest.main()
from ums import app
import unittest

class TestUMS(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def add_user(self, firstName, lastName, email, dob):
        tester = app.test_client(self)
        return tester.post("/add_users", data=dict(firstName=firstName, lastName=lastName, email=email, dob=dob), follow_redirects=True)

if __name__ == "__main__":
    unittest.main()
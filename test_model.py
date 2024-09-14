import unittest
from model.cow import Cow
from model.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database('test_data.json')
        self.cow = Cow(id=12345678, breed="white", age_years=3, age_months=6)
        self.db.add_cow(self.cow)

    def test_get_cow(self):
        cow = self.db.get_cow(12345678)
        self.assertEqual(cow.id, 12345678)
        self.assertEqual(cow.breed, "white")

    def test_milk_cow(self):
        result = self.cow.milk()
        self.assertIn(result, ["Plain milk", "BSOD: Soy milk cannot be produced"])

    def tearDown(self):
        import os
        os.remove('test_data.json')

if __name__ == '__main__':
    unittest.main()

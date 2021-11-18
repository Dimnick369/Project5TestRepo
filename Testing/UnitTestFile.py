import unittest
from MyFunc import formatted_name

class MyTestCase(unittest.TestCase):
    def test_first_last_name(self):
        result = formatted_name("pete", "seeger")
        self.assertEqual(result, "Pete Seeger")

    def test_first_last_middle_name(self):
        result = formatted_name("raymond", "reddington", "red")
        self.assertEqual(result, "Raymond Red Reddington")

if __name__ == '__main__':
    unittest.main()




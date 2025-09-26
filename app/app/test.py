from django.test import SimpleTestCase

from app import calc

class CalTest(SimpleTestCase):

    def test_cal(self):
        result = calc.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        result = calc.subtract(1, 2)
        self.assertEqual(result, 1)

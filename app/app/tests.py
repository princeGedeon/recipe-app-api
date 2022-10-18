from django.test import SimpleTestCase
from .calc import add,substract
class ViewCalc(SimpleTestCase):
    def test_add(self):
       res=add(4,5)
       self.assertEqual(res , 9)

    def test_substract(self):
        res=substract(15,10)
        self.assertEqual(res,5)

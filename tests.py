import unittest
import task
from datetime import date

class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testareaofCircle(self):
        self.radius = 2
        self.area = task.areaofCircle(self.radius)
        self.assertEqual(12.56, self.area)

    def testfirstandlastofList(self):
        self.list = [1, 2, 3, 4]
        self.firstandLast = task.firstandlastofList(self.list)
        self.assertEqual([1, 4], self.firstandLast)

    def testnumberofDays(self):
        self.date1 = date(2020, 4, 9)
        self.date2 = date(2020, 2, 26)
        self.num = task.numberofDays(self.date1, self.date2)
        self.assertEqual(43, self.num)

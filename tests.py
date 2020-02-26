import unittest
import task


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

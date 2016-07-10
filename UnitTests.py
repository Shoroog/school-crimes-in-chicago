import unittest
import CrimeNearSchool
import os
import csv


class Test(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(True)

    def setUp(self):
        self.testdata = open('Schools.csv').read()

    def test_type(self):
        crimeType = []
        with open('Crimes-2015.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                crimeType.append(row[5])
        self.assertFalse(not crimeType)
        self.assertTrue('THEFT' in crimeType)

    def test_district(self):
        district = []
        with open('Crimes-2015.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                district.append(row[11])
        self.assertFalse(not district)
        self.assertTrue('011' in district)


if __name__ == '__main__':
    unittest.main()

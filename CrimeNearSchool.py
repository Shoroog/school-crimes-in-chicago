import csv
import os
from array import array
import collections
from collections import Counter


def main():

    crimetype()
    districtCrime()


def crimetype():

    os.system('clear')
    print('Crimes Type')
    crimes = []
    with open('Crimes-2015.csv') as f:
        reader = csv.reader(f)
        for row in reader:
          crimes.append(row[5])
    crimeCounts = Counter(crimes)
    x = input('Please enter the first top results by entering the amount or 0 for all data: ')
    print('The most common crimes happened in Chicago city in 2015')
    if x == 0:
        for types, count in crimeCounts.most_common():

            print ('%s: %d times.' % (types, count))
    else:
        for types, count in crimeCounts.most_common(x):
            print ('%s: %d times.' % (types, count))
    os.system('clear')


def districtCrime():

    os.system('clear')
    print('Crimes in Specific District ')
    district = []
    with open('Crimes-2015.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            district.append(row[11])
    disCounts = Counter(district)
    x = input('Please enter the first top results by entering the amount or 0 for all data: ')
    print('The most common crimes happened in these districts ')

    if x == 0:

         for types, count in disCounts.most_common():
            print ('%s: %d times.' % (types, count))
    else:
        for types, count in disCounts.most_common(x):
            print ('%s: %d times.' % (types, count))

    os.system('clear')


main()
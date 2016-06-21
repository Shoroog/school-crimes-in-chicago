import csv
import os
from array import array
import collections
from collections import Counter


# read crimes.csv
out = open("Crimes-2015.csv","rb")
data = csv.reader(out)
data = [row for row in data]
out.close()

# read school.csv
out2 = open("schools.csv","rb")
data2 = csv.reader(out2)
data2 = [row for row in data2]
out2.close()

dataSchoolLocation= [[row[2]]for row in data2]
dataCrimeLocation= [[row[3]] for row in data]

#writing crime location in file
outFile= open("crime_location.csv","wb")
output= csv.writer(outFile)
for row in dataCrimeLocation:
  output.writerow(row)
outFile.close()

#writing school location in file
outFile2= open("school_location.csv","wb")
output2= csv.writer(outFile2)
for row in dataSchoolLocation:
  output2.writerow(row)
outFile2.close()

# read crimes.csv
out3 = open("crime_location.csv","rb")
data3 = csv.reader(out3)
data3 = [row for row in data3]
out3.close()

# read school.csv
out4 = open("school_location.csv","rb")
data4 = csv.reader(out4)
data4 = [row for row in data4]
out4.close()

dataCrimeLocation2= [[row[0]] for row in data3]
dataSchoolLocation2= [[row[0]]for row in data4]

dataCrimeType= [[row[5]] for row in data]
#writing school location in file
outFile4= open("crime_type.csv","wb")
output4= csv.writer(outFile4)
for row in dataCrimeType:
  output4.writerow(row)

outFile4.close()

#criminal Time
dataCrimeTime= [[row[2]] for row in data]


def main():

    crimetype()
    timeCrime()


def crimetype():

    os.system('clear')
    print('Crimes Type')
    crimes = []
    with open('crime_type.csv') as f:
        reader = csv.reader(f)
        for row in reader:
          crimes.append(row[0])
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


def timeCrime():


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

    if x==0:

         for types, count in disCounts.most_common():
            print ('%s: %d times.' % (types, count))
    else:
        for types, count in disCounts.most_common(x):
            print ('%s: %d times.' % (types, count))

    os.system('clear')



main()
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
# define reg x then define arrays


#address location for schools
# define it as an array
dataSchoolLocation= [[row[2]]for row in data2]


#address location for crimes
# define it as an array
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
#Criminal time type and location
dataCrimeLocationTimeType= [[row[2],row[3],row[5]] for row in data]
#criminal Time
dataCrimeTime= [[row[2]] for row in data]

#writing crime location in file
outFile3= open("crime_time_location_type.csv","wb")
output3= csv.writer(outFile3)
for row in dataCrimeLocationTimeType:
  output3.writerow(row)

outFile3.close()


def main():

    crimetype()
    timeCrime()


def crimetype():

    os.system('clear')
    print('The most common crimes happened in Chicago city in 2015')
    crimes = []
    with open('crime_type.csv') as f:
        reader = csv.reader(f)
        for row in reader:
          crimes.append(row[0])
    crimeCounts = Counter(crimes)
    x = input('Please enter the first top results by entering the amount or 0 for all data: ')
    if x == 0:
        for types, count in crimeCounts.most_common():
            print ('%s: %d times.' % (types, count))
    else:
        for types, count in crimeCounts.most_common(x):
            print ('%s: %d times.' % (types, count))
    os.system('clear')


def timeCrime():

    os.system('clear')
    print('The most common crimes time and dates that happened in Chicago city in 2015')
    time = []
    with open('Crimes-2015.csv') as f:
        reader = csv.reader(f)
        for row in reader:
           time.append(row[2])
    timeCounts = Counter(time)

    for types, count in timeCounts.most_common():
            print ('%s: %d times.' % (types, count))

    os.system('clear')

main()
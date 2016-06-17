import csv
import pandas as pd
import re
from array import array

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


#readlines = dataCrimeLocation.readlines()
readLines = dataCrimeLocation.readlines()
for line in readLines:

    str = line.split()
   # str[1:]
   # s = " ".join(str)

print str[1:]

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


variable= []

#print (re.findall(r'\d{1,5}', 'dhjg543 main st.lkfh'))
#if (dataCrimeLocation2 == dataSchoolLocation2):

 #   print ('There are some location matches..', dataSchoolLocation2)
#else:
  #  print('no matches..')





#Criminal type
dataCrimeType= [[row[5]] for row in data]
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

s= "Shoroog Tala Alhuthaifi"
s.split()
keywords = ["Tala","Lama"]

words = s.split()
for w in words:
    if w in keywords:
       print("matches")

#use regex and match




import csv
import pandas as pd
import re

# read crimes.csv
out = open("Crimes-2015.csv","rb")
data = csv.reader(out)
data = [row for row in data]
out.close()

# read school.csv
out2 = open("schools.csv","rb")
data2 = csv.reader(out2)
data2 = [row for row in data2]
out.close()
# define reg x then define arrays


#address location for crimes
# define it as an array
dataCrimeLocation= [[row[3]] for row in data]


#address location for schools
# define it as an array
dataSchoolLocation= [[row[2]]for row in data2]

#print (re.findall(r'\d{1,5}', 'dhjg543 main st.lkfh'))
if (dataCrimeLocation == dataSchoolLocation):

    print ('There are some location matches..', dataCrimeLocation)
else:
    print('no matches..')

#Criminal type
dataCrimeType= [[row[5]] for row in data]

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


#criminal Time
dataCrimeTime= [[row[2]] for row in data]



import csv
import rpy2.robjects as ro
import pandas as pd

out = open("Crimes-2015.csv","rb")
data = csv.reader(out)
data = [row for row in data]
out.close()

out2 = open("schools.csv","rb")
data2 = csv.reader(out2)
data2 = [row for row in data2]
out.close()

#address location for crimes
dataCrimeLocation= [[row[3]] for row in data]

#address location for schools
dataSchoolLocation= [[row[2]]for row in data2]

print dataCrimeLocation

#Criminal type
dataCrimeType= [[row[5]] for row in data]

#writing data in file
out= open("new_data.csv","wb")
output= csv.writer(out)
for row in new_data
    output.writerow(row)

    out.close()


#criminal Time
dataCrimeTime= [[row[2]] for row in data]



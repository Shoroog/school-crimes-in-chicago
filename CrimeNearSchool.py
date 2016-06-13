import csv

out = open("Crimes-2015.csv","rb")
data = csv.reader(out)
data = [row for row in data]
out.close()

out2 = open("schools.csv","rb")
data2 = csv.reader(out2)
data2 = [row for row in data2]
out.close()

print data2


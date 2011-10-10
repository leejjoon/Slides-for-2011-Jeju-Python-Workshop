import csv

for row in csv.reader(open("test.csv")):
    print row[0], ":".join(row[1:4]), ":".join(row[4:])
    

from coords import Position
for row in csv.reader(open("test.csv")):
    p = Position("%s %s" % (":".join(row[1:4]), ":".join(row[4:])))
    print row[0], p.galactic()
    

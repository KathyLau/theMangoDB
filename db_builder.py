from pymongo import MongoClient
import csv       #facilitates CSV I/O

server = MongoClient('127.0.0.1')
db = server.theMangoDB


d=csv.DictReader(open("peeps.csv"))
for k in d:
    db.students.insert_one(k)

d=csv.DictReader(open("courses.csv"))
for k in d:
    db.courses.insert_one(k)


print db.students.count()
print db.courses.count()

from pymongo import MongoClient
import csv       #facilitates CSV I/O

server = MongoClient('127.0.0.1')

db = server.theMangoDB

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

#db.close()


fObj=open("peeps.csv")
d=csv.DictReader(fObj)
for k in d:
    dict = {}
    dict += {'name': k['name'],'age' : k['age'], 'id':k['id']}
# insert 
fObj.close()



q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"
c.execute(q)
fObj=open("courses.csv")
d=csv.DictReader(fObj)
for k in d:
    p = "INSERT INTO courses VALUES (\""+k['code']+"\","+k['id']+","+k['mark']+")"
    c.execute(p)

fObj.close()


#==========================================================
db.commit() #save changes
db.close()  #close database

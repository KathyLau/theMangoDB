from pymongo import MongoClient
import csv       #facilitates CSV I/O

server = MongoClient('localhost')
db = server.theMangoDB

def listify(fname):
    d = csv.DictReader(open(fname))
    return [row for row in d]

def mongolify():
    peeps=listify("peeps.csv")
    courses=listify("courses.csv")
    mainList = [] #to hold list of updated dictionaries
    for peep in peeps:
        courseD = {}
        for course in courses:
            if course['id'] == peep['id']: 
                courseD[course['code']] = course['mark'] #store as {'course1':mark, etc}
        peep['courses'] = courseD #add courses to student dictionary
        mainList.append(peep)
    db.students.insert_many(mainList)

if db.students.count() == 0:
    mongolify()

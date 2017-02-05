from pymongo import MongoClient
from csv import DictReader       #facilitates CSV I/O
server = MongoClient('localhost')
db = server.theMangoDB

if db.students.count() == 0:
    p=[r for r in DictReader(open("peeps.csv"))]
    c=[r for r in DictReader(open("courses.csv"))]
    mainList = [] #to hold list of updated dictionaries
    for peep in p:
        courseD = {}
        for course in c:
            if course['id'] == peep['id']:
                courseD[course['code']] = course['mark'] #store as {'course1':mark, etc}
        peep['courses'] = courseD #add courses to student dictionary
        mainList.append(peep)
    db.students.insert_many(mainList)

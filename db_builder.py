#Team 'TheMangoDB'
#Kathy Lau, Felix Rieg-Baumhauer

from pymongo import MongoClient
from csv import DictReader       #facilitates CSV I/O
server = MongoClient('149.89.150.100')
db = server.theMangoDB

if db.students.count() == 0:
    p = DictReader(open("peeps.csv"))
    for peep in p:
        courses = {}
        c = DictReader(open("courses.csv"))
        for course in c:
            if course['id'] == peep['id']:
                courses[course['code']] = course['mark'] #store as {'course1':mark, etc}
        peep['courses'] = courses #add courses to student dictionary
        db.students.insert_one(peep)


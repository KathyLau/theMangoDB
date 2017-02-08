#Team 'TheMangoDB
#Kathy Lau, Felix Rieg-Baumhauer

from pymongo import MongoClient
from csv import DictReader       #facilitates CSV I/O
server = MongoClient('149.89.150.100')
db = server.theMangoDB

db.students.drop()
p = DictReader(open("peeps.csv"))
c = [course for course in DictReader(open("courses.csv"))]

for peep in p:
    mList = []
    for course in c:
        if course['id'] == peep['id']:
           mList.append({'code': course['code'], 'mark': int(course['mark'])})
    peep['courses'] = mList #add courses to student dictionary
    peep['age'] = int(peep['age']) #convert all to int
    peep['id'] = int(peep['id'])
    db.students.insert_one(peep)

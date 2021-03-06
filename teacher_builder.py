#Team 'TheMangoDB'
#Kathy Lau, Felix Rieg-Baumhauer

from pymongo import MongoClient
from csv import DictReader       #facilitates CSV I/O
server = MongoClient('149.89.150.100')
db = server.theMangoDB

db.teachers.drop()
t = DictReader(open("teachers.csv"))

for teacher in t:
	students = db.students.find({'courses.code':teacher['code']})
	s=[]
	for stud in students:
		s.append(stud['id'])
	teacher['peeps'] = s
	teacher['period'] = int(teacher['period'])
	db.teachers.insert_one(teacher)

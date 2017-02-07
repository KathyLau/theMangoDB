#Team 'TheMangoDB'
#Kathy Lau, Felix Rieg-Baumhauer

from pymongo import MongoClient
from csv import DictReader       #facilitates CSV I/O
server = MongoClient('149.89.150.100')
db = server.theMangoDB

db.teachers.drop()

t = DictReader(open("teachers.csv"))
for teacher in t:
	students = db.students.find({'courses'.name:teacher['code']})
	teacher['students'] = students	
	db.insert_one({teacher})


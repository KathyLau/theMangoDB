from pymongo import MongoClient
server = MongoClient('149.89.150.100')
db = server.theMangoDB
        
for c in db.students.find():
    avg = 0
    d = c['courses'] # ex: {'systems': '75', 'softdev': '65', 'ceramics': '99'}
    if len(d)!=0: # if student has 0 courses, avg is 0
        avg = sum([int(d[k]) for k in d]) / len(d) # turn dict into a list of just values , ex: [75,65,95]. add it up and divide by len
    print c['name'], c['id'], avg

import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.school

students = db.students.find()



for student in students:
    scores = student['scores']

    homeworks = filter(lambda score:score['type'] =='homework', scores)
    smalest  = homeworks[0]

    for hw in homeworks:
        if hw['score'] < smalest['score']:
            smalest = hw

    print student['name']
    print 'smaller : ' + str(smalest['score'])
    student['scores'].remove(hw)

    for hw in student['scores']:
        print hw

    db.students.save(student)
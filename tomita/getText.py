
import os

def checkPersons(db, path = ""):
    if not os.path.isfile(path + 'personFIO.txt'):
        f = open ('personFIO.txt', 'w')
        person = db.person.find()
        for text in person:
            f.write(text.get("personName") +'\n')
        f.close()

def checkPlaces(db, path = ""):
    if not os.path.isfile(path +'attractionsNames.txt'):
        f = open ('attractionsNames.txt', 'w')
        attractions = db.attractions.find()
        for text in attractions:
            f.write(text.get("attractionsNames") +'\n')
        f.close()


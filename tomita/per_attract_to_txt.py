import os.path

def checkPersons(db):
    if not os.path.isfile('personFIO.txt'):
        f = open ('personFIO.txt', 'w')
        person = db.person.find()
        for text in person:
            f.write(text.get("personName") +'\n')
        f.close()

def checkPlaces(db):
    if not os.path.isfile('attractionsNames.txt'):
        f = open ('attractionsNames.txt', 'w')
        attractions = db.attractions.find()
        for text in attractions:
            f.write(text.get("attractionsNames") +'\n')
        f.close()






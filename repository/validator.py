from Domain.event import Event
from Domain.person import Person
import datetime
class Validator:
    def __init__(self):
        pass
    def validateNewPerson(self, personList, newPerson):
        for person in personList:
            if person.getID() == newPerson.getID():
                raise ValueError("Enter a unique ID")

    def validateNewEvent(self, eventsList, newEvent):
        for event in eventsList:
            if event.getIDEvent() == newEvent.getIDEvent():
                raise ValueError("Enter a unique ID")

def testValidator():
    person = Person(1, 'Dan', 'Adr')
    personList = []
    personList.append(person)
    val = Validator()
    try:
        val.validateNewPerson(personList, person)
        assert False
    except:
        assert True

    event = Event('1', datetime.datetime(2023, 12, 19, 20, 36), 'Labtest')
    eventList = []
    eventList.append(event)
    try:
        val.validateNewEvent(eventList, event)
        assert False
    except:
        assert True

testValidator()
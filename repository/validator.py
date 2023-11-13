class EqualIDError(Exception):
    pass
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
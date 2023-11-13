from repository.validator import Validator
from Domain.event import Event
import datetime
class InMemoryRepositoryEvents:
    def __init__(self):
        self.__eventsList = {}
        self.__validator = Validator()

    def addEvent(self, event):
        try:
            eventsList = self.getAllEvents()
            self.__validator.validateNewEvent(eventsList, event)
            self.__eventsList[event.getIDEvent()] = event
            # print(eventsList)
        except ValueError as ex:
            print(ex)

    def eventDoesExist(self, idEvent):
        for id in self.__eventsList:
            if id == idEvent:
                return True
        return False

    def getAllEvents(self):
        return list(self.__eventsList.values())

    def deleteEvent(self, eventID):
        del self.__eventsList[eventID]

    def size(self):
        return len(self.__eventsList)


def testRepEvents():
    repEvent = InMemoryRepositoryEvents()
    event1 = Event('1', datetime.datetime(2023, 12, 19, 20, 36), 'Labtest')
    repEvent.addEvent(event1)
    assert repEvent.size() == 1
    repEvent.deleteEvent('1')
    assert repEvent.size() == 0

testRepEvents()
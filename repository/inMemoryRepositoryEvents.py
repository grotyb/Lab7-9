from Domain.event import Event
import datetime
class InMemoryRepositoryEvents:
    def __init__(self):
        self.__eventsList = {}

    def addEvent(self, event):
        self.__eventsList[event.getIDEvent()] = event

    def getAllEvents(self):
        return list(self.__eventsList.values())

    def deleteEvent(self, eventID):
        del self.__eventsList[eventID]

    def modifyEventDate(self, idEvent, year, month, day):
        self.__eventsList[idEvent].setDateOnlyEvent(year, month, day)

    def modifyEventHour(self,idEvent, hour, minutes):
        self.__eventsList[idEvent].setHourOnly(hour, minutes)

    def modifyEventDescription(self, idEvent, newDescription):
        self.__eventsList[idEvent].setDescription(newDescription)

    def find(self, idEvent):
        return self.__eventsList.get(idEvent)

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
import datetime
import random
import string

from Domain.event import Event
class EventService:
    def __init__(self, repoEvents, validator):
        self.__repo = repoEvents
        self.__validator = validator

    def addEvent(self, IDEvent, eventDate, eventDescription):
        newEvent = Event(IDEvent, eventDate, eventDescription)
        try:
            self.__validator.validateNewEvent(self.__repo.getAllEvents(), newEvent)
            self.__repo.addEvent(newEvent)
            print("Event saved...")
        except:
            print("Event was not saved, ID must be unique")

    def deleteEvent(self, iDEvent):
        if self.eventDoesExist(iDEvent):
            self.__repo.deleteEvent(iDEvent)
            print("Event was deleted...")
        else:
            print("An event with the specified ID does not exist")

    def modifyDate(self, id, year, month, day):
        if self.eventDoesExist(id) == True:
            self.__repo.modifyEventDate(id, year, month, day)
        else:
            print("Cannot modify event date, an event with the specified ID does not exist")

    def modifyEventHour(self, id, hour, minutes):
        if self.eventDoesExist(id) == True:
            self.__repo.modifyEventHour(id, hour, minutes)
        else:
            print("Cannot modify event hour, an event with the specified ID does not exist")

    def modifyEventDescription(self, id, newDescription):
            if self.eventDoesExist(id) == True:
                self.__repo.modifyEventDescription(id, newDescription)
            else:
                print("Cannot modify event description, an event with the specified ID does not exist")

    def cautaDupaID(self, id):
        """
        Searches for an event with ID=id
        :param id: string
        :return: The person if it was found, None otherwise
        """
        if self.eventDoesExist(id) == True:
            eventList = self.__repo.getAllEvents()
            for event in eventList:
                if event.getIDEvent() == id:
                    return event
        else:
            print("A person with the specified ID does not exist")
    def eventDoesExist(self, idEvent):
        """
        Searches for an event with the specified id
        :param idEvent: string
        :return: True if found and False otherwise
        """
        for event in self.__repo.getAllEvents():
            if event.getIDEvent() == idEvent:
                return True
        return False

    def addRandomEvents(self, nrOfEvents):
        i = 0
        while i < nrOfEvents:
            idEvRand = "".join(random.choices(string.ascii_lowercase, k=5))
            dataEvRand = datetime.datetime(random.randint(2023, 2030), random.randint(1, 12), random.randint(1, 30), random.randint(0, 23), random.randint(0, 59))
            descEv = "".join(random.choices(string.ascii_lowercase, k=10))
            evRand = Event(idEvRand, dataEvRand, descEv)
            try:
                self.__validator.validateNewEvent(self.__repo.getAllEvents(), evRand)
                self.__repo.addEvent(evRand)
                i+=1
            except:
                pass


    def getMaxIdEvents(self):
        eventsList = self.__repo.getAllEvents()
        maxID = 0
        for event in eventsList:
            if event.getIDEvent() > maxID:
                maxID = event.getIDEvent()
        return maxID


def testEventService():
    from repository.validatorEvents import EventValidator
    from repository.inMemoryRepositoryEvents import InMemoryRepositoryEvents
    rep = InMemoryRepositoryEvents()
    val = EventValidator()
    srv = EventService(rep, val)
    testEvent = Event("1", datetime.datetime(2023, 5, 14, 12, 34), "Apa plata")
    srv.addEvent(testEvent.getIDEvent(), testEvent.getDataEvent(), testEvent.getEventDescription())
    assert srv.eventDoesExist("1") == True
    assert srv.eventDoesExist("2") == False

# testEventService()
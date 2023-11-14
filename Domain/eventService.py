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

    def eventDoesExist(self, idEvent):
        for event in self.__repo.getAllEvents():
            if event.getIDEvent() == idEvent:
                return True
        return False
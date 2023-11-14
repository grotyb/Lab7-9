from Domain.event import Event
import datetime
class EventValidator:
    def __init__(self):
        pass

    def validateNewEvent(self, eventsList, newEvent):
        for event in eventsList:
            if event.getIDEvent() == newEvent.getIDEvent():
                raise ValueError("Enter a unique ID")


def testValidatorEvents():
    event = Event('1', datetime.datetime(2023, 12, 19, 20, 36), 'Labtest')
    eventList = []
    val = EventValidator
    eventList.append(event)
    try:
        val.validateNewEvent(eventList, event)
        assert False
    except:
        assert True
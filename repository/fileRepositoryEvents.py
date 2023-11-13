import datetime

from repository.inMemoryRepositoryEvents import InMemoryRepositoryEvents
from UTILS.readFileHandler import ReadFromFile
from Domain.event import Event
from repository.validator import Validator
class FileRepoEvents(InMemoryRepositoryEvents):
    def __init__(self, fileName):
        InMemoryRepositoryEvents.__init__(self)
        self.__fileName = fileName
        self.__loadFromFile()
        self.__validator = Validator()

    def __loadFromFile(self):
        textData = ReadFromFile(self.__fileName)
        textData = textData.getTextData()
        for line in textData:
            newEvent = self.__parseTextLineIntoEvent(line)
            InMemoryRepositoryEvents.addEvent(self, newEvent)

    def __parseTextLineIntoEvent(self, textLine):
        textLine = textLine.split(',')
        data = self.parseStringIntoDateTime(textLine[1], textLine[2])
        newEvent = Event(textLine[0], data, textLine[3])
        return newEvent

    def parseStringIntoDateTime(self, date, hour):
        date = date.split('.')
        hour = hour.split(':')
        dateTimeObject = datetime.datetime(int(date[2]), int(date[1]), int(date[0]), int(hour[0]), int(hour[1]))
        return dateTimeObject
    def addEvent(self, event):
        InMemoryRepositoryEvents.addEvent(self, event)
        self.__loadToFile(InMemoryRepositoryEvents.getAllEvents(self))

    def __parseEventIntoTextLine(self, event):
        stringToWrite = ''
        stringToWrite += event.getIDEvent()
        stringToWrite += ','
        stringToWrite += self.parseDateIntoString(event.getDataEvent())
        stringToWrite += ','
        stringToWrite += event.getEventDescription()
        return stringToWrite

    def deleteEvent(self, eventID):
        InMemoryRepositoryEvents.deleteEvent(self, eventID)
        self.__loadToFile(self.getAllEvents())

    def parseDateIntoString(self, data):
        dateString = ''
        dateString += str(data.day) + '.' + str(data.month) + '.' + str(data.year)
        dateString +=','
        dateString += str(data.hour) + ':' + str(data.minute)
        return dateString

    def __loadToFile(self, eventsList):
        f = open(self.__fileName, "w")
        for event in eventsList:
            stringToWrite = self.__parseEventIntoTextLine(event)
            stringToWrite += '\n'
            f.write(stringToWrite)
        f.close()

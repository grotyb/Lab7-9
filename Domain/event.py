class Event:
    def __init__(self, ID, data, descriere):
        """
        A class that stores an event
        :param ID: a unique identifier for each event
        :param data: a dateTime object that contains the year, moth, day, hour and minute
        :param descriere: A description for the event
        """
        self.__id = ID
        self.__data = data
        self.__description = descriere

    def getIDEvent(self):
        """
        Getter for an event id
        :return:
        """
        return self.__id

    def getDataEvent(self):
        """
        Getter for an event date
        :return:
        """
        return self.__data

    def getEventDescription(self):
        """
        Getter for an event description
        :return:
        """
        return self.__description

    def setDateOnlyEvent(self, year, month, day):
        self.__data = self.__data.replace(year = year, month = month, day = day)

    def setHourOnly(self, hour, minutes):
        self.__data = self.__data.replace(hour = hour, minute = minutes)

    def setDescription(self, newDescription):
        self.__description = newDescription

    # def __eq__(self, other):
    #     if self.getIDEvent() == other.getIDEvent():
    #         return True
    #     return False
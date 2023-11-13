from repository.inMemoryRepositoryEvents import InMemoryRepositoryEvents
class FileRepoEvents(InMemoryRepositoryEvents):
    def __init__(self, fileName):
        InMemoryRepositoryEvents.__init__(self)
        self.__fileName = fileName

    def addEvent(self, event):
        InMemoryRepositoryEvents.addEvent()

from repository.inMemoryRepoParticipare import InMemoryRepoParticipare
from Domain.participare import Participa
class FileRepoParticipari(InMemoryRepoParticipare):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.loadFromFile()

    def storeParticipare(self, participare):
        super().storeParticipare(participare)
        self.loadToFile(super().getAllParticipari())

    def deleteParticipare(self, participare):
        super().deleteParticipare(participare)
        self.loadToFile(super().getAllParticipari())

    def loadFromFile(self):
        file = open(self.__fileName, 'r')
        fileText = file.readlines()
        file.close()
        for line in fileText:
            self.storeParticipare(self.createParticipareFromString(line))

    def createParticipareFromString(self, stringParticipare):
        stringParticipare = stringParticipare[:-1]
        stringParticipare = stringParticipare.split(',')
        participare = Participa(stringParticipare[0], int(stringParticipare[1]))
        return participare

    def loadToFile(self, listaParticipari):
        file = open(self.__fileName, 'w')
        for p in listaParticipari:
            file.write(self.createParticipareString(p))
        file.close()

    def createParticipareString(self, participare):
        participareIDEvent = participare.getEventID()
        participareIDPers = participare.getPersonID()
        participareIDPers = str(participareIDPers)
        string = participareIDEvent
        string += ','
        string += participareIDPers
        string += '\n'
        return string



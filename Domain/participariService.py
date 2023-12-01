from Domain.participare import Participa
import datetime
class ParticipariService:
    def __init__(self, repoParticipari, validatorParticipare, repoEvenimente, repoPersoane):
        self.__repoParticipari = repoParticipari
        self.__validatorParticipare = validatorParticipare
        self.__repoPers = repoPersoane
        self.__repoEvenimente = repoEvenimente


    def inscrierePersoanaLaEveniment(self, personID, eventID):
        participare = Participa(eventID, personID)
        try:
            self.__validatorParticipare.validateParticipare(participare)
            self.__repoParticipari.storeParticipare(participare)
        except Exception as ex:
            print(ex)

    def listaEvenimentePtPersoana(self, idPersoana):
        listaParticipari = self.__repoParticipari.getAllParticipari()
        listaIDEvenimentePtPersoanaData = []
        for p in listaParticipari:
            if p.getPersonID() == idPersoana:
                listaIDEvenimentePtPersoanaData.append(p.getEventID())
        eventList = []
        for eventID in listaIDEvenimentePtPersoanaData:
            event = self.__repoEvenimente.find(eventID)
            eventList.append(event)
        eventList = sorted(eventList, key=lambda x: (x.getEventDescription() ,x.getDataEvent()))
        for event in eventList:
            print(event.getIDEvent(), event.getEventDescription(), event.getDataEvent())

    def raportNumarPersoaneLaEveniment(self):
        nrEvenimentePerPers = {}
        persoaneMax = []
        max = -1
        listaParticipari = self.__repoParticipari.getAllParticipari()
        for participare in listaParticipari:
            if nrEvenimentePerPers.get(participare.getPersonID()) != None:
                nrEvenimentePerPers[participare.getPersonID()] += 1
            else:
                nrEvenimentePerPers[participare.getPersonID()] = 1
            if nrEvenimentePerPers[participare.getPersonID()] == max:
                persoaneMax.append(self.__repoPers.find(participare.getPersonID()))
            elif nrEvenimentePerPers[participare.getPersonID()] > max:
                persoaneMax.clear()
                persoaneMax.append(self.__repoPers.find(participare.getPersonID()))
                max = nrEvenimentePerPers[participare.getPersonID()]

        for p in persoaneMax:
            print(p.getID(), p.getName(), p.getAdress())

    def evenimenteCuCeiMaiMultiParticipanti(self):
        nrPersPerEveniment = {}
        evenimenteMax = []
        max = -1
        listaParticipari = self.__repoParticipari.getAllParticipari()
        for participare in listaParticipari:
            if nrPersPerEveniment.get(participare.getEventID()) != None:
                nrPersPerEveniment[participare.getEventID()] += 1
            else:
                nrPersPerEveniment[participare.getEventID()] = 1

        sortedDictAsList = sorted(nrPersPerEveniment.items(), key=lambda x:x[1],reverse=True)
        nrOfEvents = len(sortedDictAsList)
        for indexEventHigh in range(nrOfEvents//5):
            event = self.__repoEvenimente.find(sortedDictAsList[indexEventHigh][0])
            print(event.getIDEvent(), event.getEventDescription(), event.getDataEvent())

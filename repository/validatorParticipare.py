class ValidatorParticipare:
    def __init__(self, repoPers, repoEvenimente):
        self.__repoPers = repoPers
        self.__repoEvenimente = repoEvenimente

    def validateParticipare(self, participare):
        persoanaParticipanta = participare.getPersonID()
        evenimentParticipat = participare.getEventID()
        listaEvenimente = self.__repoEvenimente.getAllEvents()
        listaPersoane = self.__repoPers.getAllPeople()
        persIDExists = False
        eventIDExists = False
        for persoana in listaPersoane:
            if persoana.getID() == persoanaParticipanta:
                persIDExists = True
        for evenimente in listaEvenimente:
            if evenimente.getIDEvent() == evenimentParticipat:
                eventIDExists = True
        if eventIDExists == True and persIDExists == True:
            return True
        else:
            raise Exception("Event ID or person ID does not exist")

def testValidatorPersoane():
    from repository.inMemoryRepositoryEvents import InMemoryRepositoryEvents
    from repository.inMemoryRepositoryPeople import InMemoryRepositoryPeople
    from Domain.event import Event
    import datetime
    from Domain.person import Person
    repP = InMemoryRepositoryPeople()
    repE = InMemoryRepositoryEvents()
    e = Event("1", datetime.datetime(2023, 12, 23, 20, 21), "Test")
    p = Person(2, "Test", "test")
    repP.addPerson(p)
    repE.addEvent(e)
    InMemoryRepositoryEvents
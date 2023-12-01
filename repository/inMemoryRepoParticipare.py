class InMemoryRepoParticipare:
    def __init__(self):
        self.__listaParticipari = []

    def storeParticipare(self, participare):
        if self.participareDoesExist(participare) != None:
            raise Exception("This participation already exsits")
        self.__listaParticipari.append(participare)

    def deleteParticipare(self, participare):
        participareDoesExist = self.participareDoesExist(participare)
        if participareDoesExist == None:
            raise Exception("This participation does not exist")
        del self.__listaParticipari[participareDoesExist]

    def getAllParticipari(self):
        return list(self.__listaParticipari)

    def participareDoesExist(self, participare):
        """
        returneaza indexul participarii daca exista, iar in caz contrar returneaza None
        :param participare:
        :return:
        """
        for index, p in enumerate(self.__listaParticipari):
            if p.getEventID() == participare.getEventID() and p.getPersonID() == participare.getPersonID():
                return index
        return None

def testRepoInMemParticipari():
    from Domain.participare import Participa
    rep = InMemoryRepoParticipare()
    p = Participa("1", 3)
    assert rep.participareDoesExist(p) == None
    rep.storeParticipare(p)
    assert rep.participareDoesExist(p) is not None
    rep.deleteParticipare(p)
    assert rep.participareDoesExist(p) == None

testRepoInMemParticipari()
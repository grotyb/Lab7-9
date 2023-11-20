from UI.displayMenu import Menu
from UI.handleUserInput import UserInput
from Domain.person import Person
from Domain.event import Event
class UI(Menu, UserInput):
    def __init__(self, servicePeople, serviceEvents):
        """
        A class that handles all the UI for the app
        :param repositoryPeople: A repository for performing operations on people
        :param repositoryEvents: A repository for performing operations on events
        """
        Menu.__init__(self)
        UserInput.__init__(self)
        self.__servicePeople = servicePeople
        self.__serviceEvents = serviceEvents

    def __redirectionareInSubmeniuAles(self, submeniu):
        """
        O functie care redirectioneaza in submeniul corespunzator alegerii din meniul principal
        :param submeniu: Tasta introdusa in meniul principal
        :return:
        """
        if submeniu == 1:
            self.__gestiuni()
        elif submeniu == 2:
            self.__cautari()
        elif submeniu == 3:
            pass
        elif submeniu == 4:
            pass
        elif submeniu == 5:
            self.__adaugariRandomPeople()
        elif submeniu == 6:
            self.__adaugariRandomEvents()

    def __adaugariRandomEvents(self):
        numarEvenimenteDeAdaugat = self.citireNumarDeEvenimenteDeAdaugatRandom()
        if numarEvenimenteDeAdaugat != None:
            self.__serviceEvents.addRandomEvents(numarEvenimenteDeAdaugat)
    def __adaugariRandomPeople(self):
        """
        O metoda care citeste valori aditionale necesare adaugarii a X persoane random
        :return:
        """
        numarPersDeAdaugat = self.citireNumarDePersoaneDeAdaugatRandom()
        if numarPersDeAdaugat != None:
            self.__servicePeople.addRandomPeople(numarPersDeAdaugat)

    def __cautari(self):
        self.afisareMeniuCautari()
        userInput = self.citireTastaCautari()
        if userInput == 1:
            id = self.readIDForPerson()
            person = self.__servicePeople.cautaDupaId(id)
            if person != None:
                self.afisarePersoana(person)
        elif userInput == 2:
            id = self.readIDForEvent()
            event = self.__serviceEvents.cautaDupaID(id)
            if event != None:
                self.displayEvent(event)

    def __gestiuni(self):
        """
        Functia gare gestioneaza submeniul de gestiuni
        :return:
        """
        self._Menu__afisareGestiuneDorita()
        tastaUser = self._UserInput__citireTastaAditionalaMeniuGesiuni()
        if tastaUser == 1:
            self.gestiuniPersoana()
        elif tastaUser == 2:
            self.gestiuniEvenimente()

    def gestiuniPersoana(self):
        self._Menu___afisareMeniuGestiuniPersoane()
        userInput = self._UserInput___citireValoriAditionaleGestiuniPersoane()
        if userInput == 1:
            self.__adaugaPersoana()
        elif userInput == 2:
            self.__stergePersoana()
        elif userInput == 3:
            self.__modificaPersoana()

    def gestiuniEvenimente(self):
        self._Menu___afisareMeniuGestiuniEvenimente()
        userInput = self._UserInput__citireValoriAditionaleGestiuniEvenimente()
        if userInput == 1:
            self.__adaugaEveniment()
        if userInput == 2:
            self.__stergeEveniment()
        elif userInput == 3:
            self.__modificaEveniment()
    def __modificaEveniment(self):
        self.afisareMeniuModificareEveniment()
        tastaUser = self.citireTastaMeniuModificariEvenimente()
        if tastaUser == 1:
            self.__modificaDataEveniment()
        elif tastaUser == 2:
            self.__modificaOraEveniment()
        elif tastaUser == 3:
            self.__modificaDesriereEveniment()
    def __stergeEveniment(self):
        idEventToDelete = UserInput.readIDForEvent(self)
        self.__serviceEvents.deleteEvent(idEventToDelete)

    def __modificaDataEveniment(self):
        id = self.readIDForEvent()
        data = self.citireData()
        self.__serviceEvents.modifyDate(id, data['an'], data['luna'], data['zi'])

    def __modificaDesriereEveniment(self):
        id = self.readIDForEvent()
        newDescription = self.readEventDescription()
        self.__serviceEvents.modifyEventDescription(id, newDescription)


    def __modificaOraEveniment(self):
        id = self.readIDForEvent()
        hour = self.citireOra()
        self.__serviceEvents.modifyEventHour(id, hour['ora'], hour['minute'])

    def modificaDescriereEveniment(self):
        id = self.readIDForEvent()
        newDescription = self.readEventDescription()
        self.__serviceEvents.modifyEventDescription(id, newDescription)

    def __adaugaEveniment(self):
        """
        Functia care gestioneaza adaugarea unui eveniment
        """
        eventData = self._UserInput__citireDateEveniment()
        self.__serviceEvents.addEvent(eventData['id'], eventData['date'], eventData['description'])

    def __modificaPersoana(self):
        self.afisareMeniuModificarePersoana()
        tastaUser = self.citireTastaMeniuModificariPeroana()
        if tastaUser == 1:
            self.modificaNumePersoana()
        elif tastaUser == 2:
            self.modificaAdresaPersoana()

    def modificaNumePersoana(self):
        personID = self.readIDForPerson()
        newName = self.citireNumeNou()
        self.__servicePeople.modifyPersonName(personID, newName)

    def modificaAdresaPersoana(self):
        personID = self.readIDForPerson()
        newAddress = self.citireAdresaNoua()
        self.__servicePeople.modifyPersonAddress(personID, newAddress)
    def __stergePersoana(self):
        """
        Functia care gestioneaza stergerea unei persoane
        :return:
        """
        personId = UserInput.readIDForPerson(self)
        self.__servicePeople.deletePerson(personId)

    def __adaugaPersoana(self):
        """
        Functia care gestioneaza adaugarea unei persoane
        :return:
        """
        personData = self._UserInput__citireDatePersoana()
        self.__servicePeople.addPerson(personData['id'], personData['nume'], personData['adresa'])

    def showUI(self):
        """
        Functia care se apeleaza pentru a afisa UIul aplicatiei
        :return:
        """
        while True:
            self._Menu__afisareMeniu()
            submenu = self._UserInput__citireTastaMeniuPrincipal()
            self.__redirectionareInSubmeniuAles(submenu)

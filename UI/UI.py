from UI.displayMenu import Menu
from UI.handleUserInput import UserInput
from Domain.person import Person
from Domain.event import Event
class UI(Menu, UserInput):
    def __init__(self, repositoryPeople, repositoryEvents):
        """
        A class that handles all the UI for the app
        :param repositoryPeople: A repository for performing operations on people
        :param repositoryEvents: A repository for performing operations on events
        """
        Menu.__init__(self)
        UserInput.__init__(self)
        self.__repositoryPeople = repositoryPeople
        self.__repositoryEvents = repositoryEvents

    def __redirectionareInSubmeniuAles(self, submeniu):
        """
        O functie care redirectioneaza in submeniul corespunzator alegerii din meniul principal
        :param submeniu: Tasta introdusa in meniul principal
        :return:
        """
        if submeniu == 1:
            self.__gestiuni()
        elif submeniu == 2:
            pass
        elif submeniu == 3:
            pass
        elif submeniu == 4:
            pass

    def __gestiuni(self):
        """
        Functia gare gestioneaza submeniul de gestiuni
        :return:
        """
        self._Menu__afisareGestiuneDorita()
        tastaUser = self._UserInput__citireTastaAditionalaMeniuGesiuni()
        if tastaUser == 1:
            self._Menu___afisareMeniuGestiuniPersoane()
            userInput = self._UserInput___citireValoriAditionaleGestiuniPersoane()
            if userInput == 1:
                self.__adaugaPersoana()
            elif userInput == 2:
                self.__stergePersoana()
        elif tastaUser == 2:
            self._Menu___afisareMeniuGestiuniEvenimente()
            userInput = self._UserInput__citireValoriAditionaleGestiuniEvenimente()
            if userInput == 1:
                self.__adaugaEveniment()
            if userInput == 2:
                self.__stergeEveniment()

    def __stergeEveniment(self):
        idEventToDelete = UserInput.readIDForDeletionEvent(self)
        if self.__repositoryEvents.eventDoesExist(idEventToDelete) == True:
            self.__repositoryEvents.deleteEvent(idEventToDelete)
        else:
            print("An event with the specified ID does not exist")
    def __adaugaEveniment(self):
        """
        Functia care gestioneaza adaugarea unui eveniment
        """
        eventData = self._UserInput__citireDateEveniment()
        newEvent = Event(eventData['id'], eventData['date'], eventData['description'])
        self.__repositoryEvents.addEvent(newEvent)
    def __stergePersoana(self):
        """
        Functia care gestioneaza stergerea unei persoane
        :return:
        """
        personId = UserInput.readIDForDeletionPerson(self)
        if self.__repositoryPeople.personDoesExist(personId) == True:
            self.__repositoryPeople.deletePerson(personId)
        else:
            print("A person with the specified ID does not exist")
    def __adaugaPersoana(self):
        """
        Functia care gestioneaza adaugarea unei persoane
        :return:
        """
        personData = self._UserInput__citireDatePersoana()
        pupil = Person(personData['id'], personData['nume'], personData['adresa'])
        self.__repositoryPeople.addPerson(pupil)

    def showUI(self):
        """
        Functia care se apeleaza pentru a afisa UIul aplicatiei
        :return:
        """
        while True:
            self._Menu__afisareMeniu()
            submenu = self._UserInput__citireTastaMeniuPrincipal()
            self.__redirectionareInSubmeniuAles(submenu)

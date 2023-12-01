class Menu:
    def __init__(self):
        pass

    def __afisareGestiuneDorita(self):
        print("Apasati tasta 1 daca doriti sa gestionati lista de persoane")
        print("Apasati tasta 2 daca doriti sa gestionati lista de evenimente")

    def __afisareMeniu(self):
        print("Apasati tasta 1 pentru Gestiuni")
        print("Apasati tasta 2 pentru Cautari")
        print("Apasati tasta 3 pentru Inscrieri")
        print("Apasati tasta 4 pentru Rapoarte")
        print("Apasati tasta 5 pentru a adauga un numar dat de studenti(Initializati cu valori aleatorii)")
        print("Apasati tasta 6 pentru a adauga un numar dat de evenimente(Initializati cu valori aleatorii)")
        print("Apasati tasta 7 pentru a inscrie o persoana la un eveniment")
        print("Apasati tasta 8 pentru a accesa meniul rapoarte")

    def afisareMeniuRapoarte(self):
        print("Apasati tasta 1 pentru a afisa lista de evenimente la care participă o persoană ordonat alfabetic după descriere, după dată")
        print("Apasati tasta 2 pentru a afisa persoanele participante la cele mai multe evenimente")
        print("Apasati tasta 3 a afisa primele 20% evenimente cu cei mai mulți participanți (descriere, număr participanți)")
        print("Apsati tasta 4 pentru a afisa evenimentele din luna curenta")

    def ___afisareMeniuGestiuniPersoane(self):
        print("Apasati tasta 1 pentru a adauga o persoana")
        print("Apasati tasta 2 pentru a sterge o persoana")
        print("Apasati tasta 3 pentru a modifica o persoana")

    def ___afisareMeniuGestiuniEvenimente(self):
        print("Apasati tasta 1 pentru a adauga un eveniment")
        print("Apasati tasta 2 pentru a sterge un eveniment")
        print("Apasati tasta 3 pentru a modifica un eveniment")

    def afisareMeniuModificarePersoana(self):
        print("Apasati tasta 1 pentru a modifica numele persoanei")
        print("Apasati tasta 2 pentru a modifica adresa persoanei")

    def afisareMeniuModificareEveniment(self):
        print("Apasati tasta 1 pentru a modifica data evenimentului")
        print("Apasati tasta 2 pentru a modifica ora evenimentului")
        print("Apasati tasta 3 pentru a modifica descrierea evenimentului")

    def afisareMeniuCautari(self):
        print("Apasati tasta 1 pentru a cauta o persoana dupa id")
        print("Apasati tasta 2 pentru a cauta un eveniment dupa id")

    def afisarePersoana(self, persoana):
        print(persoana.getID(), persoana.getName(), persoana.getAdress())

    def displayEvent(self, event):
        print(event.getIDEvent(), self.parseDateIntoString(event.getDataEvent()), event.getEventDescription())
    def parseDateIntoString(self, data):
        dateString = ''
        dateString += str(data.day) + '.' + str(data.month) + '.' + str(data.year)
        dateString += ','
        dateString += str(data.hour) + ':' + str(data.minute)
        return dateString
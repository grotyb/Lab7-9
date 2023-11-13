import datetime


class UserInput:
    def __init__(self):
        pass

    def __citireTastaMeniuPrincipal(self):
        return self.__readUserInput(4, 1)

    def __citireTastaAditionalaMeniuGesiuni(self):
        return self.__readUserInput(2, 1)

    def ___citireValoriAditionaleGestiuniPersoane(self):
        return self.__readUserInput(3, 1)

    def __citireValoriAditionaleGestiuniEvenimente(self):
        return self.__readUserInput(3, 1)

    def __citireDatePersoana(self):
        id = input("Introduceti IDul dorit: ")
        nume = input("Introduceti Numele dorit: ")
        adresa = input("Introduceti adresa dorita: ")
        return {'id': id, 'nume': nume, 'adresa': adresa}

    def __citireDateEveniment(self):
        id = input("Introduceti IDul dorit: ")
        dataAndHour = self.__citireData()
        desc = input("Introduceti descrierea evenimentului: ")
        return {'id': id, 'date': dataAndHour, 'description': desc}

    def __citireOra(self):
            ora = input("Introduceti ora(hh:mm): ")
            ora = ora.split(':')
            try:
                hour = int(ora[0])
                minutes = int(ora[1])
                if hour < 0 or hour > 24:
                    raise Exception("Invalid Hour")
                if minutes < 0 or minutes >= 60:
                    raise Exception("Invalid Minutes")
                return hour, minutes
            except Exception as ex:
                print(ex)
    def __citireData(self):
        try:
            an = int(input("Introduceti anul in care va avea loc evenimentul: "))
            luna = int(input("Introduceti luna in care va avea loc evenimentul: "))
            zi = int(input("Introduceti ziua in care va avea loc evenimentul: "))
            ora = self.__citireOra()
            date = datetime.datetime(an, luna, zi, ora[0], ora[1])
            return date
        except:
            print("Enter a valid value")
    def readIDForDeletion(self):
            id = input("introduceti IDul persoanei pe care doriti sa o stergeti): ")
            return id

    def __readUserInput(self, maxInput, lowerBoundInput):
        """
        A function that prompts the user to input a value and validates that it is an int and that it is contained between the lower and upper bound
        :param maxInput: Upper bound for input(as an int)
        :param lowerBoundInput: Lower bound for input(as an int)
        :return: The user input
        """
        try:
            userInput = int(input("Introduceti tasta dorita: "))
            if userInput < lowerBoundInput or userInput > maxInput:
                raise ValueError("Input is not in range")
            return userInput
        except ValueError as ex:
            print(ex)
        except:
            print("Intoduceti o valoare corecta")
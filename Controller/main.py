from UI.UI import UI
from repository.fileRepositoryPeople import FileRepoPeople
from repository.fileRepositoryEvents import FileRepoEvents
from Domain.personService import PersonService
from Domain.eventService import EventService
from repository.validatorPeople import PersonValidator
from repository.validatorEvents import EventValidator

repPeople = FileRepoPeople('/Users/danpetri/Documents/IT/personal_projects/PYTHON/Lab7-9/Data/persoane.txt')
repEvents = FileRepoEvents('/Users/danpetri/Documents/IT/personal_projects/PYTHON/Lab7-9/Data/evenimente.txt')
validatorPeople = PersonValidator()
validatorEvents = EventValidator()
srvPeople = PersonService(repPeople, validatorPeople)
srvEvents = EventService(repEvents, validatorEvents)
ui = UI(srvPeople, srvEvents)
ui.showUI()
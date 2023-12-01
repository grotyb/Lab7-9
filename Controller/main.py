from UI.UI import UI
from repository.fileRepositoryPeople import FileRepoPeople
from repository.fileRepositoryEvents import FileRepoEvents
from Domain.personService import PersonService
from Domain.eventService import EventService
from repository.validatorPeople import PersonValidator
from repository.validatorEvents import EventValidator
from repository.validatorParticipare import ValidatorParticipare
from Domain.participariService import ParticipariService
from repository.fileRepoParticipari import FileRepoParticipari

repPeople = FileRepoPeople('/Users/danpetri/Documents/IT/personal_projects/PYTHON/Lab7-9/Data/persoane.txt')
repEvents = FileRepoEvents('/Users/danpetri/Documents/IT/personal_projects/PYTHON/Lab7-9/Data/evenimente.txt')
repParticipari = FileRepoParticipari('/Users/danpetri/Documents/IT/personal_projects/PYTHON/Lab7-9/Data/participari.txt')
validatorPeople = PersonValidator()
validatorEvents = EventValidator()
validatorParticipari = ValidatorParticipare(repPeople, repEvents)
srvPeople = PersonService(repPeople, validatorPeople)
srvEvents = EventService(repEvents, validatorEvents)
srvParticipari = ParticipariService(repParticipari, validatorParticipari, repEvents, repPeople)
ui = UI(srvPeople, srvEvents, srvParticipari)
ui.showUI()
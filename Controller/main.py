from UI.UI import UI
from repository.fileRepositoryPeople import FileRepoPeople
from repository.fileRepositoryEvents import FileRepoEvents

repPeople = FileRepoPeople('/Users/danpetri/Documents/IT/personal_projects/PYTHON/Lab7-9/Data/persoane.txt')
repEvents = FileRepoEvents('/Users/danpetri/Documents/IT/personal_projects/PYTHON/Lab7-9/Data/evenimente.txt')
ui = UI(repPeople, repEvents)
ui.showUI()
import os
from organiser import Organiser

class CLI:
    'Command-line interface for the organiser component'


    myOrganiser = Organiser()


    def __init__(self) -> None:
        self.myOrganiser.addTodo('Une première Todo')
        print(self.myOrganiser.todos[0].title)
        self.myOrganiser.todos[0].addTask('Une première task, pour voir')
        print(self.myOrganiser.todos[0].tasks[0].description)
        self.myOrganiser.todos[0].checkTask(0)
        print(self.myOrganiser.todos[0].tasks[0].checked)
        self.myOrganiser.todos[0].checkTask(0)
        print(self.myOrganiser.todos[0].tasks[0].checked)
        self.myOrganiser.todos[0].deleteTask(0)
        print(len(self.myOrganiser.todos[0].tasks))
        self.myOrganiser.deleteTodo(0)
        print(len(self.myOrganiser.todos))
        pass


    def displayInterface(self):
        return

    
    def displayTitle(self):

        return


interface = CLI()
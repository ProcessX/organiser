from interfaceTodoList import InterfaceTodoList
from interface import Interface
from organiser import Organiser


class InterfaceOrganiser(Interface):
    'Command-line interface for the organiser'


    myOrganiser = Organiser()
    interfaceTodoList = None


    def __init__(self) -> None:
        super().__init__()
        self.title = 'PERSONAL ORGANISER'
        self.commands['0'] = [
            self.accessTodos,
            'Access your todos'
        ]
        self.interfaceTodoList = InterfaceTodoList(self.myOrganiser.todos)
    

    def displayInterface(self):
        # Display the modules of the organiser
        print('[0] My Todos\n')

    
    def accessTodos(self):
        # Run the todo module.
        self.interfaceTodoList.run()
        return
from interface import Interface

class InterfaceTodoList(Interface):


    myTodos = []


    def __init__(self, todos) -> None:
        super().__init__()
        self.title = 'Your todos'
        self.myTodos = todos

    
    def displayInterface(self):
        if(len(self.myTodos) >= 1):
            for todo in self.myTodos:
                print(todo.title)
        else:
            print('No todo in your list')

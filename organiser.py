from components.todo import Todo

class Organiser:

    todos = []

    def __init__(self) -> None:
        pass


    def addTodo(self, title):
        # Add to the list a todo titled after the title parameter
        # @param title : title of the new todo
        self.todos.append(Todo(title))
        return

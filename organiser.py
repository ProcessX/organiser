from components.todo import Todo

class Organiser:
    'Personal organiser with : todos'

    todos = []

    def __init__(self) -> None:
        pass


    def addTodo(self, title):
        # Add to the list a todo titled after the title parameter
        # @param title : title of the new todo
        self.todos.append(Todo(title))
        return
    
    def deleteTodo(self, index):
        # Delete the todo at the specified index from the list.
        # @param index : index of the todo to delete
        del self.todos[index]
        return
    
    def renameTodo(self, index, newTitle):
        # Pass a new title to the todo.
        # @param index : index of the todo to update
        # @param newTitle : new title to pass to the todo
        self.todos[index].rename(newTitle)
        return

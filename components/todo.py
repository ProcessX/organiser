from components.task import Task

class Todo:

    title = 'My Todo'
    tasks = []

    def __init__(self, title) -> None:
        self.title = title
        pass


    def addTask(self, description):
        # Add a task to the list
        # @param description : description of the new task
        self.tasks.append(Task(description))

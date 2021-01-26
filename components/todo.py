from components.task import Task

class Todo:
    'List of tasks to complete'


    title = 'My Todo'
    tasks = []


    def __init__(self, title) -> None:
        self.title = title
        pass


    def rename(self, newTitle):
        # Change the title
        # @param newTitle : the new title to apply
        self.title = newTitle
        return


    def addTask(self, description):
        # Add a task to the list
        # @param description : description of the new task
        self.tasks.append(Task(description))


    def deleteTask(self, index):
        # Delete the task at the specified index from the list.
        # @param index : index of the task to delete
        del self.tasks[index]
        return

    
    def checkTask(self, index):
        # Check the task at the required index.
        # @param index : index of the task to check
        self.tasks[index].check()
        return


    def rewriteTask(self, index, description):
        # Change the description of the task
        # @param index : index of the task in the list
        # @param description : new description of the task
        self.tasks[index].rewrite(description)

    
class Task:
    'Task to complete'


    description = 'My task'
    checked = False


    def __init__(self, description) -> None:
        self.description = description
        pass


    def check(self):
        # Toggle the status of the task (checked or unchecked).
        self.checked = not self.checked

    
    def rewrite(self, newDescription):
        # Rewrite the description of the task
        # @param newDescription : new description to replace the old one
        self.description = newDescription
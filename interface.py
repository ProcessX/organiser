class Interface:
    'Command-line interface system'


    commands = {}


    def __init__(self) -> None:
        self.commands['cmd'] = [
            self.displayCommands(),
            'Display commands'
        ]
        pass


    def run(self):
        # Run the interface module
        running = True
        while(running):
            userInput = input('Your action? ')


    def displayCommands(self):
        # Display the command list and their description.
        return

    
    def quit(self):
        # Quit the current interface and return to the previous one.
        return

    

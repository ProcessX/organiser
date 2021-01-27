import os

class Interface:
    'Command-line interface system'


    commands = {}
    callToAction = 'Votre action?'
    title = 'Title'
    message = 'Bienvenue'


    def __init__(self) -> None:
        self.commands['cmd'] = [
            self.displayCommands,
            'Display command list'
        ]
        pass


    def run(self):
        # Run the interface module
        running = True
        while(running):
            self.clearInterface()
            self.displayInterface()
            userInput = input(f'{self.callToAction} ')
            self.runCommand(userInput)


    def runCommand(self, cmd):
        # Run the command entered by the user
        # @param cmd : title of the entered command
        print(f'Run command: {cmd}')

        command = self.commands.get(cmd, False)
        if(not command):
            self.message = 'Error: cmd invalid'
            return False
        else:
            command[0]()
        return True


    def clearInterface(self):
        # Clear the CLI for new content
        if os.name == 'nt': 
            _ = os.system('cls') 
    
        else: 
            _ = os.system('clear')


    def displayInterface(self):
        # Display the content of the interface
        print(self.title)
        if(self.message):
            print(self.message)
            self.message = None


    def displayCommands(self):
        # Display the command list and their description.
        commandList = 'COMMANDS: '
        for command in self.commands:
            commandList += f'"{command}" => {self.commands[command][1]}, '
        self.message = commandList
        return

    
    def quit(self):
        # Quit the current interface and return to the previous one.
        return

    

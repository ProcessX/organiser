import os

class Interface:
    'Command-line interface system'


    running = False
    commands = {}
    callToAction = 'Your action?'
    title = 'Title'
    message = None


    def __init__(self) -> None:
        self.commands['cmd'] = [
            self.displayCommands,
            'Display command list'
        ]

        self.commands['return'] = [
            self.goBack,
            'Go Back'
        ]
        pass


    def run(self):
        # Run the interface module
        self.running = True
        while(self.running):
            self.clearInterface()
            self.displayTitle()
            self.displayInterface()
            self.displayMessage()
            userInput = input(f'{self.callToAction} ')
            self.runCommand(userInput)


    def runCommand(self, cmd):
        # Run the command entered by the user
        # Change the message to error if cmd isn't recognised
        # @param cmd : title of the entered command
        command = self.commands.get(cmd, False)
        if(not command):
            self.message = 'Error: cmd invalid'
            return True
        else:
            return command[0]()


    def clearInterface(self):
        # Clear the CLI for new content
        if os.name == 'nt': 
            _ = os.system('cls') 
    
        else: 
            _ = os.system('clear')


    def displayInterface(self):
        # Display the content of the interface (title + message)
        return


    def displayTitle(self):
        # Display the title of the module
        titleLen = len(self.title)
        print('-' * titleLen)
        print(self.title)
        print(('-' * titleLen) + '\n')


    def displayMessage(self):
        # Display the message if there is any.
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

    
    def goBack(self):
        # Return to the previous interface level.
        self.running = False

    

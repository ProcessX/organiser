from interface import Interface
from interfaceOrganiser import InterfaceOrganiser

class Main:


    myInterface = InterfaceOrganiser()


    def __init__(self) -> None:
        self.myInterface.run()
        pass


main = Main()
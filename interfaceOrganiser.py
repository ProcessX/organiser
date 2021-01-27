from interface import Interface


class InterfaceOrganiser(Interface):
    'Command-line interface for the organiser'

    def __init__(self) -> None:
        super().__init__()
        self.title = 'PERSONAL ORGANISER'
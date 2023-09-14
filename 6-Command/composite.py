from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class WBFilter(Command):

    def execute(self):
        print('WbFillter applied')


class HighContrast(Command):
    def execute(self):
        print('High contrast filter')


class Composite(Command):

    def __init__(self) -> None:
        self.commands: list[Command] = []

    def add(self, command: Command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()


if __name__ == "__main__":
    compoite = Composite()
    compoite.add(HighContrast())
    compoite.add(WBFilter())
    compoite.execute()

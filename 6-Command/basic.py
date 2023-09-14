from abc import abstractmethod, ABC


class Command(ABC):
    
    @abstractmethod
    def execute(self):
        pass


class Button:
    def __init__(self, command) -> None:
        self.command = command

    def click(self):
        self.command.execute()


class UserService:
    def add_user(self):
        print('user added')

class UserAddCommand(Command,UserService):

    def add_user(self):
        return super().add_user()
    
    def execute(self):
        self.add_user()
        return super().execute()
    
if __name__=="__main__":
    service=UserService()
    command=UserAddCommand()
    button=Button(command)
    button.click()

from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, next) -> None:
        self.next: Handler = next

    def handle(self, *args, **kwargs):
        res = self.do_handle(*args, **kwargs)
        if (res):
            return res
        
        if self.next :
            self.next.handle()

    @abstractmethod
    def do_handle(self):
        pass


class Authenticator(Handler):
    def __init__(self, next) -> None:
        super().__init__(next)

    def do_handle(self, user, password):
        isValid: bool = (user == 'admin' and password == '1234')
        print("authenticated")
        return not isValid


class Compressor(Handler):
    def __init__(self, next) -> None:
        super().__init__(next)

    def do_handle(self):
        print("compressed!!!")
        return False


class Logger(Handler):
    def __init__(self, next) -> None:
        super().__init__(next)

    def do_handle(self):
        print("Log")
        return False


class Encryptor(Handler):
    def __init__(self, next) -> None:
        super().__init__(next)

    def do_handle(self):
        print("encrypted")
        return False


class WebServer:
    def __init__(self, handler: Handler) -> None:
        self.handler = handler

    def handle(self, *args, **kwargs):
        self.handler.handle(*args, **kwargs)



if __name__=='__main__':
    encryptor=Encryptor(None)
    compressor=Compressor(encryptor)
    logger=Logger(compressor)
    authenticator=Authenticator(logger)
    server=WebServer(authenticator)
    server.handle(user='admin',password='1234')
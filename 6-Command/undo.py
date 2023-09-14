from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class UndoableCommand(Command):

    @abstractmethod
    def unexecute(self):
        pass


class HtmlDocument:
    def __init__(self) -> None:
        self._content: str = ''

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    def bold_content(self):
        self._content = '<b>'+self.content+'</b>'


class History:
    def __init__(self) -> None:
        self.history_list: list[UndoableCommand] = []

    def push(self, command: Command):
        self.history_list.append(command)

    def pop(self) -> UndoableCommand:
        return self.history_list.pop()


class BoldCommand(UndoableCommand):
    def __init__(self, document: HtmlDocument, history) -> None:
        self.document = document
        self.prev_content: str = ''
        self.history = history

    def unexecute(self):
        self.document.content = self.prev_content

    def execute(self):
        self.prev_content = self.document.content
        self.document.bold_content()
        self.history.push(self)


class UndoCommand(Command):

    def __init__(self, history: History) -> None:
        self.history = history

    def execute(self):
        command = self.history.pop()
        command.unexecute()


if __name__ == "__main__":
    document = HtmlDocument()
    document.content="hello world!!!"
    history = History()
    command = BoldCommand(document, history)
    command.execute()

    print(document.content)

    undo_command=UndoCommand(history)
    undo_command.execute()

    print(document.content)


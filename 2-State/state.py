from abc import abstractmethod, ABC

# State
class Tool(ABC):
    # handler1
    @abstractmethod
    def mouse_down(self):
        pass

    # handler2
    @abstractmethod
    def mouse_up(self):
        pass


# Context
class Canvas:
    def __init__(self) -> None:
        self._curent_tool: Tool

    @property
    def tool(self):
        return self._curent_tool

    @tool.setter
    def tool(self, value):
        self._curent_tool = value

    # request1
    def mouse_down(self):
        self._curent_tool.mouse_down()

    # request2
    def mouse_up(self):
        self._curent_tool.mouse_up()


# Selection1
class Selection(Tool):
    # handler
    def mouse_down(self):
        print("changing icon to selection")
    # handler

    def mouse_up(self):
        print("draw a line")


# Selection2
class Brush(Tool):
    # handler
    def mouse_down(self):
        print("changing icon to brush")

    # handler
    def mouse_up(self):
        print("brushing")

# we can also add as many class as we want


if __name__ == "__main__":
    canvas=Canvas()
    canvas.tool=Selection()
    canvas.mouse_down()
    canvas.mouse_up()

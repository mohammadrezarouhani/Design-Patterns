# Exercise
# In the Exercises project, look at the code in the memento/Document
# class. This class represents a document in a word processor like MS
# Word or Apple Pages.
# Our Document class has three attributes:
# - content
# - fontName
# - fontSize
# We should allow the user to undo the changes to any of these
# attributes. In the future, we may add additional attributes in this
# class and these attributes should also be undoable.
# Implement the undo feature using the memento pattern.



from dataclasses import dataclass

from pyparsing import ABC


@dataclass
class EditorState:
    content: str
    font: str
    font_size: int

class EditorHistory:
    def __init__(self) -> None:
        self.state: list = []

    def pushHistory(self, state: EditorState):
        self.state.append(state)

    def popHistory(self) -> EditorState:
        last_state = self.state.pop()
        return last_state
    
class Editor:
    def __init__(self):
        self._content: str = ''
        self._font: str = ''
        self._font_size: int = 0

    def create_state(self) -> EditorState:
        return EditorState(self.content, self.font, self.font_size)

    def restore_state(self, state: EditorState):
        self.content = state.content
        self.font = state.font
        self.font_size = self.font_size

    def set_content(self, content: str, font: str = 'default', font_size: int = 12):
        self.content = content
        self.font = font
        self.font_size = font_size

    def get_content(self) -> tuple:
        return (self.content, self.font, self.font_size)


if __name__ == '__main__':
    editor = Editor()
    history = EditorHistory()

    editor.set_content('first content')
    history.pushHistory(editor.create_state())

    editor.set_content('second content')
    history.pushHistory(editor.create_state())

    editor.set_content('third content')
    editor.restore_state(history.popHistory())
    print(editor.get_content())

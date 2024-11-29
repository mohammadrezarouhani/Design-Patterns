from dataclasses import dataclass


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

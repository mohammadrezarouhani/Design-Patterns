from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def current(self) -> str:
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def prev(self):
        pass

    @abstractmethod
    def has_next(self) -> bool:
        pass


class BrowsHistory:
    def __init__(self) -> None:
        self.uri_list = []

    def push(self, value: str):
        self.uri_list.append(value)

    def pop(self) -> str:
        return self.uri_list.pop()

    def create_itrator(self) -> 'BrowsHistory.ListIterator':
        return self.ListIterator(self)

    class ListIterator(Iterator):
        def __init__(self, history:'BrowsHistory') -> None:
            self.history = history
            self.index = 0

        def current(self) -> str:
            return self.history.uri_list[self.index]

        def next(self):
            self.index += 1
            return self.history.uri_list[self.index]

        def prev(self):
            self.index -= 1
            return self.history.uri_list[self.index]

        def has_next(self) -> bool:
            try:
                self.history.uri_list[self.index+1]
                return True
            except IndexError:
                return False


if __name__ == '__main__':
    history = BrowsHistory()
    history.push('a')
    history.push('b')
    history.push('c')
    history.push('d')
    itr = history.create_itrator()

    while(itr.has_next()):
        print(itr.current())
        itr.next()
    
    itr.prev()
    itr.prev()
    itr.prev()
    print(itr.current())

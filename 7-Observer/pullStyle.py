from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Subject():
    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def add_observer(self, obs: Observer):
        self.observers.append(obs)

    def delete_observer(self, obs: Observer):
        self.observers.remove(obs)

    def notify(self, value):
        for obs in self.observers:
            obs.update(value)


class DataSource(Subject):
    def __init__(self) -> None:
        self._data = None
        super().__init__()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class SpreedSheet(Observer):
    def __init__(self, data_source: DataSource) -> None:
        self.data_source = data_source
        super().__init__()

    def update(self):
        print('spreed sheed updated'+DataSource.data)


class Chart(Observer):
    def __init__(self, data_source: DataSource) -> None:
        self.data_source = data_source

    def update(self):
        print('chart updated'+DataSource.data)

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, value):
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
    def _data(self):
        return self._data

    @_data.setter
    def _data(self, value):
        self._data = value
        self.notify(value)


class SpreedSheet(Observer):
    def update(self, value):
        print('spreed sheed updated'+value)


class Chart(Observer):
    def update(self, value):
        print('chart updated'+value)

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
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify(value)


class SpreedSheet(Observer):
    def update(self, value):
        print('spreed sheed updated'+value)


class Chart(Observer):
    def update(self, value):
        print('chart updated'+value)


if __name__=="__main__":
    data_source=DataSource()
    sp1=SpreedSheet()
    chart=Chart()

    data_source.add_observer(sp1)
    data_source.add_observer(chart)

    data_source.data='==> new data'
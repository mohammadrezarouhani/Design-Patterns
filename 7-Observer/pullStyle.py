from abc import ABC, abstractmethod
import pdb


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

    def notify(self):
        for obs in self.observers:
            obs.update()


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
        print('spreed sheed updated'+self.data_source.data)


class Chart(Observer):
    def __init__(self, data_source: DataSource) -> None:
        self.data_source = data_source

    def update(self):
        print('chart updated'+self.data_source.data)


if __name__=="__main__":
    data_source=DataSource()
    sp1=SpreedSheet(data_source)
    chart=Chart(data_source)

    data_source.add_observer(sp1)
    data_source.add_observer(chart)

    data_source.data='==> new data'
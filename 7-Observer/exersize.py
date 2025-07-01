from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


class Screen(Observer):
    def update(self, value):
        print(f"pull data from datasource {value}")


class DataSource:
    def __init__(self):
        self.__data = 0
        self.__observer_list: List[Observer] = []

    def add_observer(self, obs: Observer):
        self.__observer_list.append(obs)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value
        for obs in self.__observer_list:
            obs.update(value)


obs = Screen()
d = DataSource()
d.add_observer(obs)
d.data = 1024

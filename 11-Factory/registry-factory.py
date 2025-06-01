from enum import Enum
from dataclasses import dataclass
from abc import ABC, abstractmethod


class OrderType(Enum):
    FOLLOW = 0
    POST = 1
    STORY = 2


@dataclass
class OrderData:
    action_count: int
    order_type: OrderType


@dataclass
class FollowData(OrderData):
    count: int


@dataclass
class PostData(OrderData):
    media_type: str
    caption: str


@dataclass
class StoryData(OrderData):
    media_type: str


class BaseOrder(ABC):
    @abstractmethod
    def execute(self):
        pass


class OrderManagerFactory:
    factory_mapper = {}

    def create(self, type: OrderType, *args, **kwds) -> BaseOrder:
        return self.factory_mapper[type](*args, **kwds)

    @classmethod
    def register(cls, type):
        def wrapper(cls, *args, **kwds):
            OrderManagerFactory.factory_mapper[type] = cls
            return OrderManagerFactory.factory_mapper[type]

        return wrapper


@OrderManagerFactory.register(OrderType.FOLLOW)
class FollowOrder(BaseOrder):
    def execute(self, data: FollowData):
        print("followed some user on social media with count: " + data.count)


@OrderManagerFactory.register(OrderType.POST)
class PostOrder(BaseOrder):
    def execute(self, data: PostData):
        print("create new post with caption: " + data.caption)


@OrderManagerFactory.register(OrderType.STORY)
class StoryOrder(BaseOrder):
    def execute(self, data: StoryData):
        print("create new story with type: " + data.media_type)

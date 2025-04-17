# in this scenario we have some order that execute some action on a social media
#  like follow, send_post, send_story, send message


from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
import pdb
from typing import Optional


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


class FollowOrder(BaseOrder):
    def execute(self, data: FollowData):
        print("followed some user on social media with count: " + data.count)


class PostOrder(BaseOrder):
    def execute(self, data: PostData):
        print("create new post with caption: " + data.caption)


class StoryOrder(BaseOrder):
    def execute(self, data: StoryData):
        print("create new story with type: " + data.media_type)


class OrderManagerFactory:
    factory_mapper = {}

    def __init__(self):
        for type in OrderType:
            name = type.name[0] + type.name[1:].lower() + "Order"
            self.factory_mapper[type] = eval(name)

    def create_order(self, data: OrderData) -> BaseOrder:
        order = self.factory_mapper[data.order_type]
        return order()


if __name__ == "__main__":
    data = FollowData(order_type=OrderType.FOLLOW, count=10, action_count=15)
    data = PostData(
        order_type=OrderType.POST,
        media_type="photo",
        caption="such amazing view",
        action_count=15,
    )
    # data = StoryData(order_type=OrderType.STORY, media_type="video", action_count=15)

    order_manager = OrderManagerFactory()
    order = order_manager.create_order(data)
    order.execute(data)

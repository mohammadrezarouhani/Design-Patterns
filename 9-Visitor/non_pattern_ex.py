from abc import ABC, abstractmethod
from typing import List


# the problem is if we want to add new operation we should add new methods to this class
# this violate the open close principle
class HtmlNode(ABC):
    @abstractmethod
    def highlight(self):
        """highlight the tag in editors"""
        pass

    def plain_text(self):
        """give the value of the node"""
        pass

    ...  # every time we should add new action


# all the node we can have
class AnchorNode(HtmlNode):
    def highlight(self):
        print("highlight anchor")


class HeadNode(HtmlNode):
    def highlight(self):
        print("highlight heading")


class HtmlDocument:
    def __init__(self):
        self._html_node: List[HtmlNode] = []

    def add(self, node: HtmlNode):
        self._html_node.append(node)

    def highlight(self):
        for node in self._html_node:
            node.highlight()


if __name__ == "__main__":
    document = HtmlDocument()
    document.add(HeadNode())
    document.add(AnchorNode())
    document.highlight()

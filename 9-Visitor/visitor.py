from abc import ABC, abstractmethod
from typing import List


class HtmlNode(ABC):
    @abstractmethod
    def execute(self, operation: 'Operation'):
        pass

## Nodes
class AnchorNode(HtmlNode):
    def execute(self, operation: 'Operation'):
        operation.apply_anchor(self)


class HeadingNode(HtmlNode):
    def execute(self, operation: 'Operation'):
        operation.apply_heading(self)


# Operation
class Operation(ABC):
    @abstractmethod
    def apply_heading(self, heading: "HeadingNode"):
        pass

    @abstractmethod
    def apply_anchor(self, anchor: "AnchorNode"):
        pass


class Highlight(Operation):
    def apply_heading(self, heading: "HeadingNode"):
        print("Highlighting heading")

    def apply_anchor(self, anchor: "AnchorNode"):
        print("Highlighting anchor")



# our main executable class
class HtmlDocument:
    def __init__(self):
        self.nodes: List[HtmlNode] = []

    def add(self, node: HtmlNode):
        self.nodes.append(node)

    def execute(self, operation: Operation):
        for node in self.nodes:
            node.execute(operation)




if __name__ == "__main__":
    doc = HtmlDocument()
    doc.add(AnchorNode())
    doc.add(HeadingNode())
    doc.execute(Highlight())

from abc import ABC, abstractmethod

# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def change(self, traffic_light):
        pass

    @abstractmethod
    def display(self):
        pass


# Concrete States
class RedLight(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = GreenLight()

    def display(self):
        print("🚦 Red Light - STOP")


class GreenLight(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = YellowLight()

    def display(self):
        print("🚦 Green Light - GO")


class YellowLight(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = RedLight()

    def display(self):
        print("🚦 Yellow Light - SLOW DOWN")


# Context
class TrafficLight:
    def __init__(self):
        self.state: TrafficLightState = RedLight()  # Default state

    def change(self):
        self.state.change(self)

    def display(self):
        self.state.display()


# Client Code
if __name__ == "__main__":
    traffic_light = TrafficLight()

    for _ in range(6):
        traffic_light.display()
        traffic_light.change()

import copy

# The Prototype Pattern is a creational design pattern
# used in software engineering to create objects by cloning an existing object,
# known as the prototype, rather than instantiating new ones from scratch

# ✅ Purpose:

# The goal of the Prototype Pattern is to reduce the cost of object creation, especially when:

#     Object creation is expensive (e.g., deep copies, complex initialization).

#     You want to avoid subclassing by letting objects define how they’re copied.

#     You want to preserve object configuration without reinitializing it manually.


# 🧠 Key Idea:

# Instead of creating a new instance of a class, clone an existing one and modify it if necessary.


# 🛠️ Use Cases:
#     Game development (cloning enemies, bullets, etc.).
#     UI frameworks (duplicating complex widget trees).
#     Configuration or setup templates (e.g., copying default system settings).


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Car(Prototype):
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.color} {self.model}"


car1 = Car("Tesla Model S", "Red")

car2 = car1.clone()
car2.color = "Blue"

print(car1)
print(car2)

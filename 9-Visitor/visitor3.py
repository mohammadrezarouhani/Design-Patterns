from abc import ABC, abstractmethod

# Visitor Interface
class DiscountVisitor(ABC):
    @abstractmethod
    def apply_electronics_discount(self, product: "Electronics"):
        pass

    @abstractmethod
    def apply_clothing_discount(self, product: "Clothing"):
        pass

    @abstractmethod
    def apply_grocery_discount(self, product: "Grocery"):
        pass


# Concrete Visitor 1: Seasonal Discount
class SeasonalDiscount(DiscountVisitor):
    def apply_electronics_discount(self, product: "Electronics"):
        print(f"Applying 10% seasonal discount on Electronics: {product.name}")

    def apply_clothing_discount(self, product: "Clothing"):
        print(f"Applying 20% seasonal discount on Clothing: {product.name}")

    def apply_grocery_discount(self, product: "Grocery"):
        print(f"Applying 5% seasonal discount on Grocery: {product.name}")


# Concrete Visitor 2: Black Friday Discount
class BlackFridayDiscount(DiscountVisitor):
    def apply_electronics_discount(self, product: "Electronics"):
        print(f"Applying 50% Black Friday discount on Electronics: {product.name}")

    def apply_clothing_discount(self, product: "Clothing"):
        print(f"Applying 30% Black Friday discount on Clothing: {product.name}")

    def apply_grocery_discount(self, product: "Grocery"):
        print(f"Applying 15% Black Friday discount on Grocery: {product.name}")


# Abstract Element (Product)
class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def accept(self, visitor: DiscountVisitor):
        pass


# Concrete Elements (Different Product Types)
class Electronics(Product):
    def accept(self, visitor: DiscountVisitor):
        visitor.apply_electronics_discount(self)


class Clothing(Product):
    def accept(self, visitor: DiscountVisitor):
        visitor.apply_clothing_discount(self)


class Grocery(Product):
    def accept(self, visitor: DiscountVisitor):
        visitor.apply_grocery_discount(self)


# Client Code
if __name__ == "__main__":
    products = [
        Electronics("Laptop", 1000),
        Clothing("Jacket", 100),
        Grocery("Milk", 5)
    ]

    seasonal_discount = SeasonalDiscount()
    black_friday_discount = BlackFridayDiscount()

    print("Applying Seasonal Discount:")
    for product in products:
        product.accept(seasonal_discount)

    print("\nApplying Black Friday Discount:")
    for product in products:
        product.accept(black_friday_discount)

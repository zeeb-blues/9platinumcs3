# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
In a sari-sari store inventory system, each item's state (name, quantity, price) and behavior (adding, removing, displaying) is unaffected by the rest of the system unless required otherwise, including the other items' states and behaviors and the rest of the code in the system that plays with the variables. This way, the system's code is more maintainable and fit for the needs of the store's handler.

### 2. Abstraction
As the handler makes inputs and navigates the inventory system, they may choose which state or behavior of which item to make changes to or utilize without focusing on other items in the system. For example, if the handler were to want to up the price of an item, they could simply make an input to make changes to only that item and its price. This allows the handler to focus on essential matters whenever possible without having to analyze the whole system at once.

### 3. Inheritance
Every item has the same properties and actions that the handler deems especially important enough to include in the system. This makes the system more organized and consistent throughout for the sake of quality of life for the handler.

```python
class Item():

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def add(self):
        self.quantity += int(input(""))

    def remove(self):
        self.quantity -= int(input(""))
    
    def display(self):
        print(f"{self.name} {self.quantity} {self.price}")
```

### 4. Polymorphism
Each item in the system gets to have its own name, price, and quantity. This allows the handler of the inventory system to include a variety of items corresponding as well to the items in the very store, allowing for much accuracy.

## Reflection
While I think each pillar very much has its own role in improving the inventory system, I think polymorphism has the biggest among them. While the other pillars especially improve upon the organization and structure of the system, polymorphism lays out the foundation for the other pillars to actually then improve on.
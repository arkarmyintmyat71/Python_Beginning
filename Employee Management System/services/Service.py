class Thing:
    def __init__(self, name, type_, color, weight, age):
        self.name = name
        self.type = type_
        self.color = color
        self.weight = weight
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.type}, {self.color}, {self.weight}kg, {self.age} years"

def add_thing():
    print("hello")
class ThingManager:
    def __init__(self):
        self.things = []


    # def add_thing(self, name, type_, color, weight, age):
    #     name = input()
    #     type_ = input("Enter type: ")
    #     color = input("Enter color: ")
    #     try:
    #         weight = float(input("Enter weight: "))
    #         age = int(input("Enter age: "))
    #     if weight <= 0 or age < 0:
    #         print("Invalid weight or age. Please enter positive values.")
    #         return
    #     new_thing = Thing(name, type_, color, weight, age)
    #     self.things.append(new_thing)
    #     print(f"{name} added successfully!")

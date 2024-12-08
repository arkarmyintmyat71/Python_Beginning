import json
import csv

# Define the Thing class
class Thing:
    def __init__(self, name, type_, color, weight, age):
        self.name = name
        self.type = type_
        self.color = color
        self.weight = weight
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.type}, {self.color}, {self.weight}kg, {self.age} years"


# Define the ThingManager class
class ThingManager:
    def __init__(self):
        self.things = []

    def display_all(self):
        print("\nAll Things:")
        if self.things:
            for thing in self.things:
                print(thing)
        else:
            print("No things to display.")

    def add_thing(self, name, type_, color, weight, age):
        if weight <= 0 or age < 0:
            print("Invalid weight or age. Please enter positive values.")
            return
        new_thing = Thing(name, type_, color, weight, age)
        self.things.append(new_thing)
        print(f"{name} added successfully!")

    def total_number(self):
        return len(self.things)

    def search_by_name(self, name):
        results = [thing for thing in self.things if thing.name.lower() == name.lower()]
        if results:
            for result in results:
                print(result)
        else:
            print("No match found.")

    def search_by_group(self, type_):
        results = [thing for thing in self.things if thing.type.lower() == type_.lower()]
        if results:
            for result in results:
                print(result)
        else:
            print("No match found.")

    def delete_thing(self, name):
        for thing in self.things:
            if name.lower() == thing.name.lower():
                self.things.remove(thing)
                print(f"{name} has been deleted.")
        else:
            print("Thing not found.")

    def update_thing(self, name, **kwargs):
        for thing in self.things:
            if thing.name.lower() == name.lower():
                thing.name = kwargs.get("name", thing.name)
                thing.type = kwargs.get("type",gi thing.type)
                thing.color = kwargs.get("color", thing.color)
                thing.weight = kwargs.get("weight", thing.weight)
                thing.age = kwargs.get("age", thing.age)
                print(f"{name} has been updated.")
                return
        print("Thing not found.")

    def save_to_file(self, filename="things_data.json"):
        with open(filename, "w") as file:
            data = [thing.__dict__ for thing in self.things]
            json.dump(data, file)
        print("Data saved successfully.")

    def load_from_file(self, filename="things_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.things = [Thing(
                    name=item['name'],
                    type_=item['type'],  # Map 'type' to 'type_'
                    color=item['color'],
                    weight=item['weight'],
                    age=item['age']
                ) for item in data]
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")
        except KeyError as e:
            print(f"Missing key in the data: {e}")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

    def export_to_csv(self, filename="things_data.csv"):
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Type", "Color", "Weight", "Age"])
            for thing in self.things:
                writer.writerow([thing.name, thing.type, thing.color, thing.weight, thing.age])
        print("Data exported to CSV successfully.")

    def sort_things(self, attribute="name"):
        try:
            self.things.sort(key=lambda x: getattr(x, attribute))
            print(f"Things sorted by {attribute}.")
        except AttributeError:
            print("Invalid attribute for sorting.")


# Define the interactive menu
def menu():
    manager = ThingManager()
    while True:
        print("\n--- Menu ---")
        print("1. Display All Things")
        print("2. Add New Thing")
        print("3. Search by Name")
        print("4. Search by Group")
        print("5. Delete Thing")
        print("6. Update Thing")
        print("7. Save Data")
        print("8. Load Data")
        print("9. Export to CSV")
        print("10. Sort Things")
        print("11. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            manager.display_all()
        elif choice == "2":
            name = input("Enter name: ")
            type_ = input("Enter type: ")
            color = input("Enter color: ")
            try:
                weight = float(input("Enter weight: "))
                age = int(input("Enter age: "))
                manager.add_thing(name, type_, color, weight, age)
            except ValueError:
                print("Invalid input. Please enter numeric values for weight and age.")
        elif choice == "3":
            name = input("Enter name to search: ")
            manager.search_by_name(name)
        elif choice == "4":
            type_ = input("Enter group/type to search: ")
            manager.search_by_group(type_)
        elif choice == "5":
            name = input("Enter name to delete: ")
            manager.delete_thing(name)
        elif choice == "6":
            name = input("Enter name to update: ")
            color = input("Enter new color (leave blank to keep current): ")
            weight = input("Enter new weight (leave blank to keep current): ")
            age = input("Enter new age (leave blank to keep current): ")
            update_args = {}
            if color: update_args['color'] = color
            if weight: update_args['weight'] = float(weight)
            if age: update_args['age'] = int(age)
            manager.update_thing(name, **update_args)
        elif choice == "7":
            manager.save_to_file()
        elif choice == "8":
            manager.load_from_file()
        elif choice == "9":
            manager.export_to_csv()
        elif choice == "10":
            attribute = input("Enter attribute to sort by (name, type, color, weight, age): ")
            manager.sort_things(attribute)
        elif choice == "11":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.")

# Run the menu
menu()

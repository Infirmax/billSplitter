from person import Person
from item import Item

class Bill:
    def __init__(self, people = [], items = [], tax = 0, tip = 0) -> None:
      self.people = people
      self.items = items
      self.tax = tax
      self.tip = tip
        
    def add_person(self, person):
        if person in self.people:
            raise Exception('This person already exists!')
        self.people.append(person)
    
    def add_item(self, item):
        self.items.append(item)
    
    # Find first item with matching name
    def find_item(self, name):
        name = name.lower()
        for item in self.items:
            if item.name.lower() == name:
                return item
        return None

    # Find first person with matching name
    def find_person(self, name):
        name = name.lower()
        for person in self.people:
            if person.name.lower() == name:
                return person
        return None
    
    # Calculate each person's cost
    def calculate(self):
        results = {}
        for person in self.people:
            total = 0
            for item in person.items:
                total += item.price/len(item.people)
            total *= (1 + self.tax + self.tip)
            results[person] = round(total, 2)
        return results
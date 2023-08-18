from person import Person

class Item:
    def __init__(self, name, price, people = None):
        self.name = name
        self.price = price
        self.people = people or []

    def add_person(self, person):
        self.people.append(person)
        
    def __repr__(self) -> str:
        return self.name
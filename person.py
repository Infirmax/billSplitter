class Person:
    def __init__(self, name, items=None):
        self.name = name
        self.items = items or []
        
    def add_item(self, item):
        self.items.append(item)

    def __repr__(self) -> str:
        return self.name
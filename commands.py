from bill import Bill
from person import Person
from item import Item

def help():
    print("""show people/food/bill (Shows the list of people, foods or the entire bill)
people add bob schrodinger (Adds person to table)
item add shrimp fried rice:5.00 (Adds item with price 5.00 to table)
split shrimp fried rice:bob schrodinger (Adds item to person, item id can be used when there are duplicates)
tax 0.0085 (Sets tax %)
tip 0.15 (sets tip %)
calculate (Show final results, automatically splitting remaining funds)
""")

# bob schrodinger
def add_people(bill, text):
    person = Person(text)
    bill.add_person(person)

# shrimp fried rice:5.00
def add_item(bill, text):
    tokens = text.split(":")
    name = tokens[0]
    price = float(tokens[1])
    item = Item(name, price)
    bill.add_item(item)

# Show the full list of people
def show_people(bill):
    for i in range(len(bill.people)):
        person = bill.people[i]
        print(f'({i}) {person}:{person.items}')
    
# Show the full list of items (and their index)
def show_item(bill):
    for i in range(len(bill.items)):
        item = bill.items[i]
        print(f'({i}) {item}:{item.people}')

# 0.15
def set_tip(bill, text):
    bill.tip = float(text)
    print(f'Tip is now {bill.tip}.')

# 0.00875
def set_tax(bill, text):
    bill.tax = float(text)
    print(f'Tax is now {bill.tax}.')
    
# shrimp fried rice:bob schrodinger
def split(bill, text):
    # Find the corresponding item and person
    [itemName, personName] = text.split(":")
    item = bill.find_item(itemName)
    person = bill.find_person(personName)

    # Add the item and person to each other
    item.add_person(person)
    person.add_item(item)

    # Show results
    print(f"Added {item.name} to {person.name}.")
    print(f"{item} : {item.people}")
    print(f"{person} now has: {person.items}")
    
# No input, just shows results from price calculations
def calculate(bill):
    results = bill.calculate()
    for key, value in results.items():
        print(f"{key} has to pay ${value}")

# Sanitizes input
def sanitize(text):
    return text.strip().lower()

# Process command
def process_command(bill, text):
    text = text.strip().lower()
    if text == "help":
        help()
    elif text.startswith("people add"):
        add_people(bill, sanitize(text[10:]))
    elif text.startswith("item add"):
        add_item(bill, sanitize(text[8:]))
    elif text.startswith("show people"):
        show_people(bill)
    elif text.startswith("show item"):
        show_item(bill)
    elif text.startswith("tip"):
        set_tip(bill, sanitize(text[3:]))
    elif text.startswith("tax"):
        set_tax(bill, sanitize(text[3:]))
    elif text.startswith("split"):
        split(bill, sanitize(text[5:]))
    elif text.startswith("calculate"):
        calculate(bill)
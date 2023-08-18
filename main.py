from commands import process_command
from bill import Bill

print("Welcome to bill splitter! Enter help for more info.")
bill = Bill()
while True:
    process_command(bill, input())
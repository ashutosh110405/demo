#if age is less than 12 give 10% off to the ticket price, and above 12 no discount take input and fix ticket rate accordingly

age = int(input("Enter your age: "))
ticket_price = 100

if age < 12:
    ticket_price *= 0.9

print("Ticket price:", ticket_price)
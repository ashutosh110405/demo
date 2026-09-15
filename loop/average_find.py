#enter a list of numbers and find the average of those numbers and find sum and average of those numbers
numbers = input("Enter a list: ")
number_list = [float(x) for x in numbers.split()]
total = sum(number_list)
average = total / len(number_list) if number_list else 0
print(f"Sum: {total}, Average: {average}")

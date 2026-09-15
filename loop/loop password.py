# check password
correct_pass = "same_pass"
not_found = True

while not_found:
    string = input("Enter a string: ")
    if string == correct_pass:
        not_found = False
    else:
        print("Incorrect Please try again.")

print("Password MAtched!")

# print even  number from 0 to 120 only

i = 0
while i <= 120:
    i+= 2
    print(i)

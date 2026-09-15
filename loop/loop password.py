# check password
correct_pass = "same_pass"
not_found = True

while not_found:
    string = input("Enter a string: ")
    if string == correct_pass:
        not_found = False
        break
    else:
        print("Incorrect Please try again.")

print("Password MAtched!")

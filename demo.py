role = input("Enter u r role: ")
age = int(input("Enter u r age: "))
eligible = (role.lower() == "student") and (age < 21)
print("Eligible:", eligible)
role = input("Enter u r role: ")
age = int(input("Enter u r age: "))
eligible = (role.lower() == "student") and (age < 21)
print("Eligible:", eligible)
# version 1.0.1 commit temp
#demo version
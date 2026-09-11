# take input from user and give score grade to the student if above 90% O grade , above 80% A grade, above 65 b, above 35 C, input should not be grater than 100%

Marks = int(input("Enter Marks: "))

if Marks >= 90 and Marks <= 100:
    print("Grade is O")
elif Marks >= 65 and Marks <= 89:
    print("Grade is A")
elif Marks >= 35 and Marks <= 64:
    print("grade is B")
elif Marks >= 0 and Marks <= 34:
    print("fail")
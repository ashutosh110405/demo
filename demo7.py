a = int(input("Enter Value A: "))

b = int(input("Enter Value B: "))

c = int(input("Enter Value C: "))

if a > b and a > c:
    print("Greater value is A : ",a)
elif b > c and b > a:
    print("Greater value is B :",b)
elif c > a:
    print("Greater value is C : ",c)

elif a ==  b == c:
    print("All values are same")
elif a == b:
    print("Value A & B are the same")
elif b == c:
    print("Value B & C are the same")
elif c == a:
    print("Value C & A are the same")


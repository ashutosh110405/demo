a = int(input("Enter Value A: "))

b = int(input("Enter Value B: "))

c = int(input("Enter Value C: "))

if a >= b and a >= c:
    print("Greater value is",a)
elif b >= c and b >= a:
    print("Greater value is",b)
elif c > a:
    print("Greater value is",c)

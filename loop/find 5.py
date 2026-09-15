#find 5 and stop priniting from the loop, start from 0 and print till 10 not 5
i = 0
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i+= 1
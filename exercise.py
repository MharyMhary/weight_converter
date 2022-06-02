
# code to print prime number

a = int(input("Enter a Number "))
if a > 1:
    for x in range (2, a):
        if (a % x) == 0:
            print("Not Prime")
            break
        else:
            print("Prime")
            break
else:
    print("Not Prime")

# code to print even numbers

a = int(input("Enter a Number "))
if a > 2:
    for x in range (2, a):
        if a % x == 0:
            print("It's an Even Number!")
            break
        else:
            print("It's a Prime Number")
            break
else:
    print("Not Even")

# print every fourth item of a sequence

a = range(21)
for x in a[6::4]:
    print(x,  end=' ')







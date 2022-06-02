

i = 1
while i <= 10:
    print(i * '*')
    i = i + 1

names = ["Titi", "Reki", "Wike"]
print(len(names))
for item in names:
    print(item[0])

i = 0
while i < len(names):
    print(names[i])
    i = i + 1

numbers = range(1, 5, 2)
for num in numbers:
    print(num)


# Program to display an even number 1 to 10 and type "We have - even numbers at the end.

num = [2, 9, 2]
for x in range(2, 9, 2):
    print(x)
    num.append(x)
b = len(num)
print(f"We have {b} even numbers")






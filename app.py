first = input("First_Number: ")
second = input("Second_Number: ")
sum = float(first) + float(second)
print("Sum = " + str(sum))

# Weight: 170
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))




# Create your repo
# Repo Address
# git add .
# git commit -m "My first git push"
# git branch -M "address"
# git push









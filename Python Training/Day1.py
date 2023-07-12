val = int(input("Enter a number: "))

if (val % 2 != 0):
    print("Weird")
elif (2 <= val <= 5):
    print("Not Weird")
elif (6 <= val <= 20):
    print("Weird")
else:
    print("Not Weird")
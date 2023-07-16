n = int(input("Enter a range: "))
count = 0

# for i in range(n):
#     if (i%2 == 0):
#         count += 1
# else:
#     print("Even") if (count%2 == 0) else print("Odd")

i = 0
while i<=n:
    if (i%2 == 0):
        count += 1
        i += 1
        break
else:
    print("Even") if (count%2 == 0) else print("Odd")
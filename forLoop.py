obj = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 11]

for i in obj:
    print(i)

for i in obj:
    if i % 2 == 0:
        print("Even Number", i)
    else:
        print("Odd Number", i)

summation=0
for i in range(1, 6):
    print(i)
    summation=summation+i
print(summation)

for k in range(1, 10, 2):
    print("number with difference", k)
# Continue


start1 = int(input("Enter start: "))
end = int(input("Enter end: "))

count = 0
for i in range(start1, end+1):
    if (i % 2 == 1):
        continue
    print(i)
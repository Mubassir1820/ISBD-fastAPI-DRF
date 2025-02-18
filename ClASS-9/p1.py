'''
3,7


4,6
'''

# Naive way

start1 = int(input("Enter start: "))
end = int(input("Enter end: "))

count = 0
for i in range(start1, end+1):
    if (i % 2 == 0):
        print(i)
        count = count + 1

print(f"Total even: {count}")
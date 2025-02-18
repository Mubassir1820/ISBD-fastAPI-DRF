# Stepping

'''
2, 4, 6, 8


'''
start1 = int(input("Enter start: "))
end = int(input("Enter end: "))

for i in range(start1, end+1, 2):
    print(i)



"""
Bug:
    1) If start is an ODD number

"""

# If start is an odd number then convert it into the next even number
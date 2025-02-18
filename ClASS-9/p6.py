'''
5 * 1 = 5
5 * 2 = 10
..........
'''
n1 = 2
n2 = 5

for number in range(n1, n2+1):
    print(f"{number} er namta : ")

    for j in range(1, 11):
        print(f"{number} * {j} = {number * j}")
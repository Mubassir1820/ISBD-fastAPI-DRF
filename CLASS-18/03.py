# Unpack

ls1 = [1,2,3]

ls2 = [*ls1]
ls2[0] = 10

print(ls1)
print(ls2)

print(*['a', 'b'])
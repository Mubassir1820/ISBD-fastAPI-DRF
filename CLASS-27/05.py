"""
Syntax:

f = open(filename, mode)
# Operation on f based on mode
f.close()
"""


filename = 'file_handling.txt'
read_mode = 'r'
f = open(filename, read_mode)

# content = f.read()
# print(content)

content = f.readline()
print(content)
content = f.readline()
print(content)
content = f.readline()
print(content)

f.close()


# how to use while loop with readline
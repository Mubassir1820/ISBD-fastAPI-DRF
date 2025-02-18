filename = 'demo.txt'
read_mode = 'r'

try:
    f = open(filename, read_mode)

    content = f.readline()
    print(content)


    f.close()
except FileNotFoundError:
    f = open(filename, 'x')
    f.close()

# What kind of challenges you faced when trying read mode: If the file doesnt exist, it will throw an error
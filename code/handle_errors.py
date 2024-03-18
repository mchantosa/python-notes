import sys

file_name = 'recipes.txt'
try:
    my_file = open(file_name, 'x')  #x is mode for creation
    my_file.write('meatballs\n')
    my_file.close()

except FileExistsError:
    print(f"{file_name} already exists")
    sys.exit(1) #non zero exit code means error
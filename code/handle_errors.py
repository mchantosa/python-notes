import sys

file_name = 'recipes.txt'
try:
    my_file = open(file_name, 'x')  #x is mode for creation
    #my_file.write(b'meatballs\n')   #toggle for error 2
    my_file.write('meatballs\n')    
    my_file.close()

except FileExistsError:
    print(f"{file_name} already exists")

except:
    print(f"Unable to create {file_name}")

else:
    print(f"{file_name} was created")

finally:
    print("Executing completed")
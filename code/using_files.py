my_file = open('xmen.txt', 'w+') #this file doesn't need to exist yet
my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n', 
    'Nightcrawler\n'
])
my_file.close()

with open('xmen.txt', 'r') as my_file: 
    my_file = open('xmen.txt', 'r') #read only
    print(my_file.read())
    print("I'm reading again")
    print(my_file.read())   #only reads once, cursor was already at the end
    print("Moved cursor back to beginning\n")
    my_file.seek(0) #go back to the beginning
    print(my_file.read())
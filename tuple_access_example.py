#tuple to access using for loop
print('\n here is an exmaple of tuple assignment and accessing it')

contacts = [('Jason', '255-053'), ('Marry', '133-254'), ('Sunanda', '2541-9509')]

for (person, phno) in contacts:
    print('\n Person is {} and phn no. is {}'.format(person, phno))
    

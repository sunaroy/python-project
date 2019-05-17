#dictionary
#a dictionary in python is a hash having key value pairs.

#like contacts = {} ...here contacts is an empty dictionary
#like contacts = {'Jason': '123-456', 'Carl': '001-002'}

contacts = {'Jason': '123-456', 'Carl': '001-002'}

jason_phone = contacts['Jason']
carl_phone = contacts['Carl']

print('First value of the dictionary is {}'.format(jason_phone))

print('Second value of the dictionary is {}'.format(carl_phone))


#add a ney key-value to the existing dictionary


contacts['new_man'] = '222-555'

print("after addition of new key the length of dictionary is : {}".format(len(contacts)))


#multivalue

contacts['jason'] = ['123-456', '100-0001']

print('Now the value of jason is {}'.format(contacts['jason']))

#####
print('\n\n')

for contact in contacts['jason']:
    print('one contact of jason is: {}'.format(contact))
    

#if the values in dictionary

if '123-456' in contacts.values():
    print("Hey I am here")


##check if a key exists in a dictionary or not

if 'jason' in contacts.keys():
    print('Hi jason is a key')
    print(contacts['jason'][0])

if 'tony' in contacts.keys():
    print('Hi I am tony but not in dictionary')



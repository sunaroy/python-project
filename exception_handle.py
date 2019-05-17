#exception handling in python

animals = ['horse', 'cow']
animals.append('tortoise')
print("after appending we get: {}".format(animals))

animals.extend(['rabbit','goat'])
print("after extending we get: {}".format(animals))

animals.insert(1,'donkey')
print("after appending donkey at index {} we get the list{}".format(animals.index('donkey'),animals))


#now get data from last

print('The last data in animals list is: {}'.format(animals[-1]))

print('The second last data of animals is : {}'.format(animals[-2]))

#do slicing to get the partials data

print("the data from index 2 to index 4 excluding index 4 is {}".format(animals[2:4]))


print("the first three data of the list is {}".format(animals[0:3]))

print("data from index two  to end is {}".format(animals[2:]))


#get partial of a list starting from end

print("the list of data starting from last fourth index to last 2nd index excluding the 2nd index".format(animals[-4:-2]))



try:
    cat_index = animals.index('cat')

except:
    cat_index = "no cat found"
print(cat_index)



#for loop


print("Finally the animals list is: {}\n".format(animals))

for animal in animals:
    print(animal.upper())


 #while loop
index = 0
while index < len(animals):
    print("\n {}".format(animals[index]))
    index += 1




    
        

    

#tuple is an  immutable list

#tuples are ordeded
#values of tuples are accesssed by index
#tuple doesnot support item assignment


#example of tuple

tuple_name = ('item_1', 'item_2', 'item_3')

print("here is the entire tuple{}".format(tuple_name))


# incase of a tuple with single item: tuple_item must end with a ,


tuple_name2 = ('item_1',)

print('\n the tuple with a single item is {}'.format(tuple_name2))

days_of_the_week = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

monday = days_of_the_week[0]

print('\n day shoul be mnday: {}'.format(monday))

print('\n \n')
for day in days_of_the_week:
    print(day)

#tuple doesnot support changes like items assignment
days_of_the_week = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'newday')

#delete tuple
del(days_of_the_week)


#tuple to list

weekend_tuple = ('sunday', 'monday')
weekend_list = list(weekend_tuple)
#get the type of tuple and list

print('\n the type of week_end_tuple is {}'.format(type(weekend_tuple)))

print('\n the type of week_end_tuple is {}'.format(type(weekend_list)))

print('\n after tuple to list is:{}'.format(weekend_list))

print('\n\n')
list_to_tuple = tuple(weekend_list)
print('\n from list to tuple is {}'.format(list_to_tuple))
tuple_1 = list_to_tuple


#access tuple items

for item in tuple_1:
    print(item)


#multiples to assign values
print('\n the below example is tuple value assignment from another tuple')
weekend_days = ('saturday', 'sunday')

(sat, sun) = weekend_days

print('\n')
print(sat)

print(sun)


#tuple assignment from list

print('\n below is an example of tuple  assignment using list')
my_numbers = [100, 200]

(hundred,twohund) = my_numbers

print('\n value of hundred  is: {} and twohhundred is: {} after assigning list value to tuple'.format(hundred, twohund))


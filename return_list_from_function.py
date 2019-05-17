#returning a tuple from a function
#get max and min value
my_values = [1,300,5,33,2,9,11,67,100,20]

def get_max_and_min(list_value):
    '''This is a function that returns a min and max value form a list of values'''
    min_value = min(list_value)
    max_value = max(list_value)
    return(min_value, max_value)

(lowest, highest) = get_max_and_min(my_values)

print('\n highest value is {} and lowest value is: {}'.format(highest, lowest))


    

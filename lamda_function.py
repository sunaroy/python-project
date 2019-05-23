#lambda function is an anonymous function ,i.e a function without name.
#filter() is a python built in function whic is capable to hold some filtered values
#filter takes two arguments ..1> the fuction using which to filter 2> the list  which is to be filtered


#lamda


# lamda x :  means  #lamda is a function with parameter or argument x.

my_list = [1,6,9,10, 13]

get_list = list(filter(lambda x: x != 10,my_list)) # filter is a fuction with 2 arguments ...i.e filter filters my_list using the provided lamda function
#and lamda function takes one parameter here it is x.

#so above will return a list of numbers who are not 10

print(get_list)
   

#get all even numbers from a list


even_list = list(filter(lambda x: x%2 == 0, my_list))

print(even_list)

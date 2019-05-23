# *args is used to make a list of argument, so that for calling a method with any number of arguments gets fitt in to the called method.


#i.e when a function is called as part of signature checking, the called method matches the  number of arguments. to get rid of it in the called method we can use *args.


#like below

def my_addition(arg1, arg2):
    return arg1 + arg2

x = my_addition(1, 2)


#so in the above unction while calling my_addition two arguments are passed , and in the function definition of my_addition two arguments are declared


#now what if wecall the same function by passing 3 arguments?

# x = my_addition(1, 2, 4) this will fail due to number of arguments missmatch

#so thus wile defining the method instaed of mentioning bumebr of arguments we can just use * args,
#which actually makes a list using the passed in parameters and puts it in *args


#now the modified program becomes

def my_addition(*args):
    print(args)
    #here args makes a list using the passed in parameters and puts it in *args
    print(sum(args))


my_addition(2, 3,7)

my_addition(1,2, 6,8,9,10)

#**kwargs means keyword arguments, i.e pas any numebr of arguments using the key= value type
print('..........................................................................')
def my_addition(*args, **kwargs):
    print(args)
    print(kwargs)
    #here args makes a list using the passed in parameters and puts it in *args
    print(sum(args))


my_addition(2, 3,7) #sohere args = (2,3,7) and kwargs = {} since no keyword arguments are sent

my_addition(1,2, 6,8,9,10, last_value = 40) # here kwargs = {lats_value= 40} and args = (1,2,6,8,9,10)




        

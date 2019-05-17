#odd or even check

def odd_even():
    """Using this function you can check odd and even numbers"""
    number = input("enter a number")
    if(number % 2 == 0):
        return("the number #{} is even".format(number))
    else:
        return("the number #{} is odd".format(number))



    odd_even()
    

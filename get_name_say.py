def get_name():
    name = input("Enter a name u want to say")
    return name

def say_name(name = "Sunanda"):
    print("The name is {}".format(name))

def get_and_say_name():
    """This funtion is to get and say a name"""
    name = get_name()
    say_name(name)


get_and_say_name()

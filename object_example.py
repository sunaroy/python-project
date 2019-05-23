#object in python example
#dictionary is not an object...to make a dictionary an object we have to pass through class, that is have to make a class for it and then initialize it

#lottery_player is a dictionary
lottery_player = {
    'name':'sunanda',
    'numbers': (3, 4, 7, 9)
    }

#now to make the dictionary an object we need a clas with constractor init

class LotteryPlayer:
    def __init__(self, player):
        self.name = player['name']
        self.numbers = player['numbers']
    def total(self):
        return sum(self.numbers)

        

#below is a player object
player = LotteryPlayer(lottery_player)

print(player.name)
print(player.total())




# second example

class Student:
    def __init__(self, st_data):
        self.name = st_data['name'],
        self.school = st_data['school']

    def goto_school(self):
        print("{}".format(self.name))
        print("{} goes to school:{}".format(self.name, self.school))


anna = Student({'name': 'anna', 'school': 'mit'})

anna.goto_school()


#inheritance and class method
#student1 = {'name': 'anna', 'school': 'oxford'}


class Student:
    def __init__(self, student_info):
        self.name = student_info['name']
        self.school = student_info['school']

    def go_to_school(self):
        print("\n {} goes to school {}".format(self.name, self.school))

#get a friend of anna from a school of anna.

    def get_friend(self, friend_name):
        return Student({'name': friend_name, 'school': self.school})
        

anna = Student({'name': 'anna', 'school': 'oxford'})

anna.go_to_school()

annas_frnd = anna.get_friend('suchita')

print("\n anna's friend name is : {}".format(annas_frnd.name))

annas_frnd.go_to_school()


#class working student gets all the things inherited from class Student #just like copying and pasting all info of student class to WorkingStudent class
class WorkingStudent(Student):
    pass


jeorge = WorkingStudent({'name': 'jeorge', 'school': 'BMGHS'})


jeorge.go_to_school()

#after this go to inheritance_two.py to  get next implementation




        




    
        

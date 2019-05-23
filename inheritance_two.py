class Student:
    def __init__(self, student_info):
        self.name = student_info['name']
        self.school = student_info['school']

    def go_to_school(self):
        print("\n {} goes to school {}".format(self.name, self.school))

#get a friend of anna from a school of anna.
        #from a clss method we can not access 'self', i.e the object did call it, in that case to get the object's propery in this class method we need to pass that object    @classmethod
    @classmethod
    def get_friend(cls, origin, friend_name, salary = 200):
        print("\n\n {}".format(origin.name))
        return cls({'name': friend_name, 'school': origin.school}, salary)
        

anna = Student({'name': 'anna', 'school': 'oxford'})

anna.go_to_school()

#annas_frnd = anna.get_friend('suchita')

#print("\n anna's friend name is : {}".format(annas_frnd.name))

#annas_frnd.go_to_school()

#working student is a student who gets a salary
class WorkingStudent(Student):
    def __init__(self, student_info, salary):
        super().__init__(student_info) #init of superclass i.e student class is calle dwoth passing studeent_info
        self.salary = salary
        

jeorge = WorkingStudent({'name': 'jeorge', 'school': 'BMGHS'}, 3000)

#so, now jeorrge is an object of type working student

jeorge.go_to_school()

print(' slary of jeorge is{}'.format(jeorge.salary))
#here passing the object itself during calling of a class method
jeorges_frnd = WorkingStudent.get_friend(jeorge,'riya', 4000)


jeorges_frnd.go_to_school()

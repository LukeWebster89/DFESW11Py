#class Dog:
#    energy = "high"
#
#    def speak(self):
#        print("woof")
#
#bilbo_waggins = Dog()
#
#print(bilbo_waggins.energy)
#bilbo_waggins.speak()

#class Student:
#
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#John = Student("John", "21")
#Jane = Student("Jane", "22")
#
#print(getattr(John, "age"))

class Student:

    def __init__(self, name, major, gpa, is_on_probabtion):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probabtion = is_on_probabtion

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student2.name, student2.major)
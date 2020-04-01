class Person():
    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    def printName(self):
        print(f"{self.firstname} {self.lastname}")

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        Person.__init__(self, firstname, lastname)
        self.subject = subject
    def __str__(self):
        return f"{self.firstname} {self.lastname}, {self.subject}"
    def printNameSubject(self):
        print(self)
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course
    def __str__(self):
        return f"{self.firstname} {self.lastname}, {self.course}"
    def printNameCourse(self):
        print(self)

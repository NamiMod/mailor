# In this file we define student object

class Student:

    def __init__(self, fname, lname, email, university_class, grade):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.university_class = university_class
        self.grade = grade

    def myfunc(self):
        print("Hello my name is " + self.fname)

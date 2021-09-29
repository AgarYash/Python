class Student:
    def __init__(self):
        self.name = input("Enter your name:")
        self.cname = input("Enter your college name:")
        self.roll = int(input("Enter your roll number:"))
        self.marks = int(input("Enter your marks:"))
class Test(Student):
    ss=""
    def check(self):
        if self.marks >=90:
            self.ss="Merit"
        elif (self.marks >=60):
            self.ss="First"
        elif self.marks >= 50:
            self.ss="Second"
        elif self.marks >= 33:
            self.ss="Third"
        else:
            self.ss="Fail"
class Admin(Test):
    def display(self):
        print("============ Student info is ==========")
        print("Name is : ", self.name)
        print("College Name is : ", self.cname)
        print("Roll number is : ", self.roll)
        print("Marks is : ", self.marks)
        print("Grade is : ", self.ss)
obj = Admin()
obj.check()
obj.display()

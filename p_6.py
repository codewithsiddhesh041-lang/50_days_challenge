#Program to Display Student Information Using Multiple Inheritance

# Parent Class 1
class PersonalInfo:
    def get_personal(self):
        self.name = input("Enter Name: ")
        self.roll_no = int(input("Enter Roll No: "))

# Parent Class 2
class AcademicInfo:
    def get_academic(self):
        self.branch = input("Enter Branch: ")
        self.marks = float(input("Enter Marks: "))

# Child Class
class Student(PersonalInfo, AcademicInfo):
    def display(self):
        print("\n--- Student Information ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Branch:", self.branch)
        print("Marks:", self.marks)

# Main Program
s = Student()
s.get_personal()
s.get_academic()
s.display()
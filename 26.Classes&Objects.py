
class Student:
       Name = "Bilal Khan"
       Subject = "BS-CET"
       Age = 25
       Is_Study = True

       def info_Out(self): #Print Out The Data
        print(f"Name: {self.Name}")
        print(f"Subject: {self.Subject}")
        print(f"Age: {self.Age}")

        if self.Is_Study == True:                   #Convert True, False Into Yes,No
              self.Is_Study = "Yes"
              print(f"Study: {self.Is_Study}")
              self.Is_Study = True
        elif self.Is_Study == False:
              self.Is_Study = "No"
              print(f"Study: {self.Is_Study}")
              self.Is_Study = False
        else:
            print("Study: No Valid Record")






print("-------------------Student 1--------------------------------")
student_1 = Student()

student_1.Name = "Ahmed Obaid"
student_1.Subject = "BS-Data Science"
student_1.Age = 20
student_1.Is_Study = True

student_1.info_Out()

print("-------------------Student 2--------------------------------")
student_2 = Student()

student_2.Name = "Hammad Shuja"
student_2.Subject = "BS-CET"
student_2.Age = 21
student_2.Is_Study = True

student_2.info_Out()

print("-------------------Student 3--------------------------------")
student_3 = Student()

student_3.Name = "Jawad Shuja"
student_3.Subject = "BS-English"
student_3.Age = 21
student_3.Is_Study = False

student_3.info_Out()
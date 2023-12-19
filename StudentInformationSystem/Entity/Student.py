class Student:
    def __init__(self,StudentID,FirstName,LastName,DateOfBirth,Email,PhoneNumber):
        self.StudentID=StudentID
        self.FirstName=FirstName
        self.LastName=LastName
        self.DateOfBirth=DateOfBirth
        self.Email=Email
        self.PhoneNumber=PhoneNumber
        print(f"Student ID:{self.StudentID} \nFirst Name:{self.FirstName} \nLast Name:{self.LastName} \nDate of Birth:{self.DateOfBirth}"
              f"\nEmail:{self.Email} \nPhone Number:{self.PhoneNumber}")

Student(1,"Sona","Vuthur",'2002-01-06','sona@gmail.com','8247238787')
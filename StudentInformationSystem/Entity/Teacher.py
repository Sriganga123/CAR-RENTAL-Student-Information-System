class Teacher:
    def __init__(self,TeacherID,FirstName,LastName,Email):
        self.TeacherID=TeacherID
        self.FirstName=FirstName
        self.LastName=LastName
        self.Email=Email
        print(f"Teacher ID:{self.TeacherID} \nFirst Name:{self.FirstName} \nLast Name:{self.LastName} \nEmail:{self.Email}")

Teacher(400,"Dhana","Laxmi",'dhana@gmail.com')
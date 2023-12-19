from util.ConnUtil import dbConnection
from datetime import datetime
from exception.StudentNotFoundException import StudentNotFoundException
from exception.InvalidStudentDataException import InvalidStudentDataException
class Students(dbConnection):
    try:
        def __init__(self):
            super().__init__()

        def addStudent(self, StudentID, FirstName, LastName, DateOfBirth, Email, PhoneNumber):
            self.StudentID = StudentID
            self.FirstName = FirstName
            self.LastName = LastName
            self.DateOfBirth = DateOfBirth
            self.Email = Email
            self.PhoneNumber = PhoneNumber
            self.open()
            insert_str = '''insert into Student(StudentID, FirstName, LastName, DateOfBirth, Email, PhoneNumber)
                            values(%s, %s, %s, %s, %s, %s)'''
            data = [(self.StudentID, self.FirstName, self.LastName, self.DateOfBirth, self.Email, self.PhoneNumber)]
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            print("Student added successfully")
            self.close()

        def UpdateStudentInfo(self):
            try:
                StudentID = int(input("Enter StudentID you want to update:"))
                if not self.studentExists(StudentID):
                    raise StudentNotFoundException(f"Student with ID {StudentID} not found.")
                self.FirstName = input("First Name:")
                self.LastName = input("Last Name:")
                self.DateOfBirth = input("Date of Birth (YYYY-MM-DD):")
                self.Email = input("Email:")
                if not self.validate_email(self.Email):
                    raise InvalidStudentDataException("Invalid email format.")

                self.PhoneNumber = input("Phone Number:")
                self.open()
                update_str = '''update Student set FirstName=%s,LastName=%s,DateOfBirth=%s,Email=%s,PhoneNumber=%s 
                                where StudentID=%s'''
                data = [(self.FirstName, self.LastName, self.DateOfBirth, self.Email, self.PhoneNumber, StudentID)]
                self.stmt.executemany(update_str, data)
                self.conn.commit()
            except InvalidStudentDataException as e:
                print(e)
            except StudentNotFoundException as e:
                print(e)
            except Exception as e:
                print(e)
            finally:
                self.close()

        def DisplayStudentInfo(self):
            self.open()
            select_str = '''select * from Student'''
            self.stmt.execute(select_str)
            data = self.stmt.fetchall()
            for i in data:
                print(i)
            self.close()

        def studentExists(self, StudentID):
            self.open()
            select_str = '''select COUNT(*) from Student where StudentID=%s'''
            self.stmt.execute(select_str, (StudentID,))
            count = self.stmt.fetchone()[0]
            return count > 0
            self.close()

        def validate_email(self, email):
            return '@' in email
    except Exception as e:
        print(e)







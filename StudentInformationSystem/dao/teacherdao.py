from util.ConnUtil import dbConnection
from exception.TeacherNotFoundException import TeacherNotFoundException
from exception.InvalidTeacherDataException import InvalidTeacherDataException
class Teacher(dbConnection):
    def addTeacher(self,TeacherID,FirstName,LastName,Email):
        self.TeacherID=TeacherID
        self.FirstName=FirstName
        self.LastName=LastName
        self.Email=Email
        try:
            self.open()
            insert_str="insert into Teacher(TeacherID,FirstName,LastName,Email)values(%s,%s,%s,%s)"
            data=[(TeacherID,FirstName,LastName,Email)]
            self.stmt.executemany(insert_str,data)
            self.conn.commit()
            print("Teacher added successfully")
            self.close()
        except Exception as e:
            print(e)
    def UpdateTeacherInfo(self):
        try:
            TeacherID=int(input("Enter Teacher ID you want to update:"))
            self.FirstName=input("Enter First Name:")
            self.LastName=input("Last Name:")
            self.Email=input("Email:")
            if not self.validate_email(self.Email):
                raise InvalidTeacherDataException("Invalid email format.")
            self.open()
            update_str='''update Teacher set FirstName=%s,LastName=%s,Email=%s where TeacherID=%s'''
            data=[(self.FirstName,self.LastName,self.Email,TeacherID)]
            self.stmt.executemany(update_str,data)
            self.conn.commit()
            print("Updated successfully")
            self.close()
        except InvalidTeacherDataException as e:
            print(e)
        except Exception as e:
            print(e)
    def DisplayTeacherInfo(self):
        try:
            self.open()
            print("Teacher Info:")
            select_str='''select * from teacher'''
            self.stmt.execute(select_str)
            data=self.stmt.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)
        finally:
            self.close()
    def GetAssignedCourses(self):
        try:
            self.open()
            print("Assigned Courses")
            select_str='''select TeacherID,CourseID from Course'''
            self.stmt.execute(select_str)
            data=self.stmt.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)

    def teacherExists(self, TeacherID):
        try:
            self.open()
            select_str = '''select COUNT(*) from Teacher where TeacherID=%s'''
            self.stmt.execute(select_str, (TeacherID,))
            count = self.stmt.fetchone()[0]
            return count > 0
        except Exception as e:
            print(e)
        finally:
            self.close()

    def AssignTeacherToCourse(self, TeacherID, CourseID):
        try:
            self.open()
            if not self.teacherExists(TeacherID):
                raise TeacherNotFoundException(f"Teacher with ID {TeacherID} not found.")
            print(f"Assigned teacher {TeacherID} to course {CourseID}")
        except TeacherNotFoundException as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def validate_email(self, email):
        return '@' in email




from util.ConnUtil import dbConnection
from exception.InvalidCourseDataException import InvalidCourseDataException
class Course(dbConnection):
    def AddCourse(self,CourseID,CourseName,CourseCode,InstructorName):
        self.CourseID=CourseID
        self.CourseName=CourseName
        self.CourseCode=CourseCode
        self.InstructorName=InstructorName
        self.open()
        insert_str='''insert into Course(CourseID,CourseName,CourseCode,InstructorName) values(%s,%s,%s,%s)'''
        data=[(self.CourseID,self.CourseName,self.CourseCode,self.InstructorName)]
        self.stmt.executemany(insert_str,data)
        self.conn.commit()
        self.close()
    def UpdateCourseInfo(self):
        try:
            CourseID=int(input("Enter Course ID u want to update:"))
            self.CourseName=input("Enter Course Name:")
            self.CourseCode=input("Enter Course Code:")
            self.InstructorName=input("Enter Instructor Name:")
            self.open()
            if not self.validate_course_data():
                raise InvalidCourseDataException("Invalid course data.")
            update_str='''update Course set CourseName=%s,CourseCode=%s,InstructorName=%s where CourseID=%s'''
            data=[(self.CourseName,self.CourseCode,self.InstructorName,CourseID)]
            self.stmt.executemany(update_str,data)
            self.conn.commit()
            print("Courses updated successfully")
        except InvalidCourseDataException as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            self.close()
    def DisplayCourseInfo(self):
        self.open()
        select_str='''select * from Course'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    def GetEnrollments(self):
        self.open()
        select_str='''select StudentID,CourseID from Enrollment'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    def AssignTeacher(self):
        self.open()
        CourseID=int(input("Enter CourseID to assign teacher:"))
        self.TeacherID=int(input("TeacherID:"))
        update_str='''update Course set TeacherID=%s where CourseID=%s'''
        data=[(self.TeacherID,CourseID)]
        self.stmt.executemany(update_str,data)
        self.conn.commit()
        print("Teacher assigned successfully")
        self.close()
    def GetTeacher(self):
        self.open()
        print("Teacher assigned to course:")
        select_str='''select CourseID,TeacherID from Course'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    def validate_course_data(self):
        if len(self.CourseCode) < 3 or len(self.InstructorName) < 3:
            return False
        return True




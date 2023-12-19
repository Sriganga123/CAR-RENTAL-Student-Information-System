from util.ConnUtil import dbConnection
from datetime import datetime
from exception.InvalidEnrollmentDataException import InvalidEnrollmentDataException
from exception.InsufficientFundsException import InsufficientFundsException
class Enrollment(dbConnection):
    def GetStudent(self):
        try:
            self.open()
            print("Students enrolled:")
            select_str='''select EnrollmentID as EID,StudentID as SID from Enrollment'''
            self.stmt.execute(select_str)
            data=self.stmt.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def GetCourse(self):
        try:
            self.open()
            print("Courses Enrolled:")
            select_str='''select EnrollmentID,CourseID from Enrollment'''
            self.stmt.execute(select_str)
            data=self.stmt.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def validate_enrollment_data(self, StudentID, CourseID):
        try:
            if not (isinstance(StudentID,int) and isinstance(CourseID,int)):
                raise InvalidEnrollmentDataException("Invalid enrollment data. Both StudentID and CourseID must be integers.")
        except InvalidEnrollmentDataException as e:
            print(e)

    def check_sufficient_funds(self, StudentID):
        try:
            self.open()
            select_str = '''select Amount from Payment where StudentID = %s'''
            self.stmt.execute(select_str, (StudentID,))
            total_payment = sum(row[0] for row in self.stmt.fetchall())
            return total_payment > 0
        except Exception as e:
            print(e)
            return False
        finally:
            self.close()

    def EnrollStudentInCourse(self, StudentID, CourseID):
        try:
            self.validate_enrollment_data(StudentID, CourseID)
            if not self.check_sufficient_funds(StudentID):
                raise InsufficientFundsException(f"Insufficient funds for student with ID {StudentID}.")

            self.open()
            insert_str = '''insert into Enrollment(StudentID, CourseID, EnrollmentDate)
                            values(%s, %s, %s)'''
            data = [(StudentID, CourseID, datetime.now())]
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            print("Student enrolled in course successfully")
        except InsufficientFundsException as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            self.close()

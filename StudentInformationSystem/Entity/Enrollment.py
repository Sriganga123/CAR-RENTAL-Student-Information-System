class Enrollment:
    def __init__(self,EnrollmentID,StudentID,CourseID,EnrollmentDate):
        self.EnrollmentID=EnrollmentID
        self.StudentID=StudentID
        self.CourseID=CourseID
        self.EnrollmentDate=EnrollmentDate
        print(f"Enrollment ID={self.EnrollmentID} \nStudent ID={self.StudentID} \nCourse ID={self.CourseID} \nEnrollment Date:{self.EnrollmentDate}")

Enrollment(200,11,102,'2022-06-12')
class Course:
    def __init__(self,CourseID,CourseName,CourseCode,InstructorName):
        self.CourseID=CourseID
        self.CourseName=CourseName
        self.CourseCode=CourseCode
        self.InstructorName=InstructorName
        print(f'Course ID:{self.CourseID} \nCourse Name:{self.CourseName} \nCourseCode:{self.CourseCode} \nInstructor Name:{self.InstructorName}')


Course(100,"Java",'J100','Sara')
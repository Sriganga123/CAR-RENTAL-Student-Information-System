class TeacherNotFoundException(Exception):
    def __init__(self,msg="Teacher not found"):
        self.msg=msg
        super().__init__(self,msg)

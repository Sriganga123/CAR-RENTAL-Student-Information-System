class LeaseNotFoundException(Exception):
    def __init__(self,message="Lease Not Found"):
        self.message=message
        super().__init__(self,message)

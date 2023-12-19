class CarNotFoundException(Exception):
    def __init__(self, message="Car not found"):
        self.message = message
        super().__init__(self.message)

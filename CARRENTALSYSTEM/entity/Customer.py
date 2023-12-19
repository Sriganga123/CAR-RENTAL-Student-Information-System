class Customer:
    def __init__(self,customerID,firstName,lastName,email,phoneNumber):
        self.customerID=customerID
        self.firstName=firstName
        self.lastName=lastName
        self.email=email
        self.phoneNumber=phoneNumber
        print(f'Customer ID={self.customerID} \nFirst Name={self.firstName} \nLast Name={self.lastName} \nEmail={self.email} \nPhone Number={self.phoneNumber}')

Customer(23,"Mona","Vuthur",'mona@gmail.com','8989898989')
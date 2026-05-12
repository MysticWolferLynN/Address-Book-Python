# Create your Contact class here
class Contact:

    def __init__(self, first_name, last_name, phone_number):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

        def __str__(self):
        
            return (
            "First Name: " + self.first_name +
            " | Last Name: " + self.last_name +
            " | Phone Number: " + self.phone_number
        )
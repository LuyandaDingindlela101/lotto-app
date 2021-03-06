class Person:
    def __init__(self, name, email, address, id_number, player_id):
        self.name = name
        self.email = email
        self.address = address
        self.player_id = player_id
        self.id_number = id_number

    #   __str__ FUNCTION IS TO PRINT A STRING VERSION OF THE CLASS
    def __str__(self):
        return "\n { name: " + self.name + ", " + "email: " + self.email + ", " + "address: " + self.address + ", " + "player id: " + self.player_id + ", " + "id number: " + self.id_number + " } "

    #   MAKE A DICTIONARY FROM THE Person DETAILS
    def make_dict(self):
        return {
                    "name": self.name,
                    "email": self.email,
                    "address": self.address,
                    "id number": self.id_number,
                    "player id": self.player_id
                }

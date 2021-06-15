class Person():
    def __init__(self, name, email, address, id_number, player_id):
        self.name = name
        self.email = email
        self.address = address
        self.player_id = player_id
        self.id_number = id_number

    #   __str__ FUNCTION IS TO PRINT A STRING VERSION OF THE CLASS
    def __str__(self):
        return "{ \n    name: " + self.name + ", \n" + "    email: " + self.email + ", \n" + "    address: " + self.address + ", \n" + "    player id: : " + self.player_id + ", \n" + "    id number: " + self.id_number + " \n}"

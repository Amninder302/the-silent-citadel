class Item:
    def __init__(self,name,description,durability = 100):
        self.name = name
        self.description = description
        self.durability = durability
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name = name
    def get_description(self):
        return self.description
    def set_description(self,description):
        self.description = description
    def get_durability(self):
        return self.durability
    def set_durability(self,durability):
        self.durability = durability

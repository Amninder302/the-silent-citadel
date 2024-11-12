class Room:
    number_of_rooms = 0
    def __init__(self,room_name,description = 'empty',detailed = "Undetermined"):
        self.room_name = room_name
        self.description = description
        self.linked_rooms = {}
        self.characters = []
        self.items = []
        self.detailed = detailed
        Room.number_of_rooms = Room.number_of_rooms + 1
    def get_detailed(self):
        print(self.detailed)
    def get_description(self):
        return self.description
    def set_description(self,description):
        self.description = description
    def describe(self):
        print(self.description)
    def link_room(self,room_to_link,direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.room_name + "linked rooms :" + repr(self.linked_rooms))
    def get_name(self):
        return self.room_name
    def get_characters(self):
        return self.characters
    def add_characters(self,character):
        self.characters.append(character)
    def rid_characters(self,character):
        self.characters.remove(character)
    def get_details(self):
        print(f"You are in the {self.room_name}\n ----------------------------------\n{self.description}")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")
    def move(self,direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go there")
            return self

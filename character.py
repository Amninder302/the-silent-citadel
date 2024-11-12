class Character:

    # Create a character
    def __init__(self, char_name, char_description, convo, weakness = "None"):
        self.name = char_name
        self.description = char_description
        self.conversation = convo
        self.weakness = weakness

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation != "None":
            print("[" + self.name + " says]: " + self.conversation)

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    def get_character(self):
        return self.name

class Enemy(Character):
    def __init__(self,char_name,char_description,convo,weakness):
        super().__init__(char_name,char_description,convo,weakness)

    def get_weakness(self):
        return self.weakness

    def set_weakness(self,weakness):
        self.weakness = weakness

    def fight(self,combat_item):
        if combat_item == self.weakness:
            print(f"You fend off {self.name} with a {combat_item} and win.")
            return True
        else:
            print(f"You couldn't defeat {self.name} with your {combat_item}")
            return False


class Friend(Character):
    def __init__(self, char_name, char_description,detailed):
        super().__init__(char_name, char_description,detailed)
        self.gifted = False
        self.talked = False
    def talk(self):
        print("[" + self.name + " says]: " + self.conversation)
        self.talked = True

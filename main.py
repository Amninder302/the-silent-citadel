# Main code of my little game, code.py is just additional, maybe helpful code, not used in the game
import time
from room import Room
from item import Item
from character import Character
from character import Enemy
from character import Friend
from rpginfo import RPGinfo

# setting up
inventory = []
pickaxe = Item("pickaxe","your trusty pickaxe",60)
inventory.append(pickaxe.name)
inn_room = Room("inn room","you wake you up in an inn. this was not where you went to sleep. but you can't remember where you went to bed either.","it is a rather small room, with just a bed and a bedside table with a candle on top of it, but nothing that could be useful to you.")
inn = Room("inn","a huge inn, yet no people in sight, and the quiet was uncomfortable.")
tavern = Room("tavern","you've never seen a tavern so devoid of people, stools and tables are lying on their sides. seems like a few hundred brawls took place here.")
butchers = Room("butcher's","the stink coming from this room is so terrible, it could probably kill.")
book_sellers = Room("book seller's","fragile books as far as the eye can see, perhaps some history of what has happened has been recorded here?.")
apothecary = Room("apothecary","dusty and humid, it seems whatever potions were once brewed here have long turned to poison.")
apothecary_basement = Room("the tunnel has lead you to underneath the apothecary. empty vials lie and pastes, and grimy cloths were littered around bed. the walls were colored with blood. it looks like a twisted scene from Frankenstein.")
keep = Room("keep","a towering castle, looming over the rest of the city, like death.")
keep_library = Room("keep's library","an expanse of books and bookshelves. surely something here could help you.")
keep_bedroom = Room("lord's bedroom","no signs of struggle here. seems he was warned of whatever was coming.")
keep_kitchen = Room("keep's kitchens","eerie atmosphere surrounded this place, stranger than the other places you've visited. if all the blood was any sign, something terrible happened here.")
keep_tunnel = Room("keep's tunnel","a long, twisty tunnel, from the keep's kitchen. the dark paths looks ominous.")
town_hall = Room("town hall","a open, friendly-looking hub, where you can access most of the town, but the blood stains and guillotine suggest a different story.")
black_smith = Room("black smith's","rows of tools and weapons line the walls, some even look usable.")
cathedral = Room("cathedral","the second-most impressive building in the inner city, even crumbling and rotting, it manages to look majestic.")
cathedral_basement = Room("cathedral basement","a dark, vast dungeon, filled with mountains and mountains of gold.")
bakery = Room("bakery","a run-down, moulding place, with walls that looked like someone tried to burn down.")
#print(Room.number_of_rooms)


# linking together my town - there has to be an easier way to do this .......
inn_room.link_room(inn,"downstairs")
inn.link_room(inn_room,"upstairs")
town_hall.link_room(cathedral,"north")
town_hall.link_room(apothecary,"north east")
town_hall.link_room(bakery,"east")
town_hall.link_room(inn,"south east")
town_hall.link_room(butchers,"south")
town_hall.link_room(book_sellers,"south west")
town_hall.link_room(black_smith,"west")
town_hall.link_room(tavern,"north west")
cathedral.link_room(keep,"north")
keep.link_room(cathedral,"south")
cathedral.link_room(town_hall,"south")
apothecary.link_room(town_hall,"south west")
apothecary.link_room(bakery,"south")
bakery.link_room(apothecary,"north")
bakery.link_room(town_hall,"west")
bakery.link_room(inn,"south")
inn.link_room(bakery,"north")
inn.link_room(town_hall,"north west")
inn.link_room(butchers,"west")
butchers.link_room(inn,"east")
butchers.link_room(town_hall,"north")
butchers.link_room(book_sellers,"west")
book_sellers.link_room(butchers,"east")
book_sellers.link_room(town_hall,"north east")
book_sellers.link_room(black_smith,"north")
black_smith.link_room(book_sellers,"south")
black_smith.link_room(town_hall,"east")
black_smith.link_room(tavern,"north")
tavern.link_room(black_smith,"south")
tavern.link_room(town_hall,"south east")
keep.link_room(keep_kitchen,"east")
keep.link_room(keep_library,"west")
keep_kitchen.link_room(keep_tunnel,"south")
keep_kitchen.link_room(keep,"west")
keep_library.link_room(keep,"east")
keep_library.link_room(keep_bedroom,"south")
keep_bedroom.link_room(keep_library,"north")
keep_tunnel.link_room(keep_kitchen,"north")

# now the characters :D
septima = Friend("septima","- a normal-looking woman, however she seems immensely distressed","m-m-my name is septima, i...i. i went on ... a trip..... to the capital. a work thing... and a nice bre-a-ack from the b-b-baby. but i can't.. i can't find them now.... (she starts wailing, and refuses to elaborate anymore) ")
inn.add_characters(septima)
norbet = Character("norbet","- the skeleton of a once living man...","")
butchers.add_characters(norbet)
samreet = Character("samreet","a skeleton, humched over at the edge of the room","")
kyle = Enemy("kyle","an unnatural, small, fuming dragon, who looks like he really wants to kill you. he will not let you pass","raaaaahhhhhhh","diamond")












#the game loooopppppp

silent_citadel = RPGinfo("the silent citadel")
silent_citadel.welcome()
RPGinfo.info()
current_room = inn_room
key = True
while key:
    print("\n")
    current_room.get_details()
    time.sleep(1)
    inhabitants = current_room.get_characters()
    if len(inhabitants) != 0 :
        for i in range(len(inhabitants)):
            inhabitants[i].describe()
            time.sleep(0.5)
    time.sleep(0.5)
    command = input("What would you like to do? > ")
    if command in ["north","south","west","east","upstairs","downstairs","north west","south east","south west","north west"] :
        current_room = current_room.move(command)
        time.sleep(1)
    elif "inside" in command :
        current_room.get_detailed()
        time.sleep(2)
    elif command == "talk" and len(inhabitants) != 0:
        person = input("Who would you like to talk to? ").lower()
        person_found = False
        for inhabitant in inhabitants:
            if person == inhabitant.name.lower():
                inhabitant.talk()
                time.sleep(3)
                person_found = True
                break
        if not person_found:
            print("That person isn't here.")
    elif command == "fight" and len(inhabitants) != 0:
        person = input("Who would you like to fight? ").lower()
        item = input("What would you like to fight with?")
        person_found = False
        if item in inventory :
            for inhabitant in inhabitants:
                if person == inhabitant.name.lower():
                    person_found = True
                    if inhabitant.fight(item) == False:
                        print("You died")
                        key = False
                        break
                    break
            if not person_found:
                print("That person isn't here.")
        else:
            print("Item is not in your inventory")
    elif "inve" in command:
        print(f"Your inventory {inventory}")

    else:
        print("Invalid input, please make sure to check the spelling, and if moving rooms, only enter the direction you wish to go.")
RPGinfo(credits)

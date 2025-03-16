my_inventory = [{'name': 'trident', 'type': 'weapon', 'damage': '3d6', 'range': 'melee', 'description' : None},
               {'name': 'shocking grasp', 'type': 'spell', 'damage': '1d8', 'range': 'touch', 'description': None}, ]



def store():
    """This function prompts user to select item type (weapon, spell, treasure, junk) and, if a valid option is chosen,
     calls the name check function to see if the item already exists in the inventory"""
    print("What would you like to store?")
    inv_type = input(" Type 'w' for weapon\n Type 's' for spell\n Type 't' for treasure\n "
                     "Or type 'u' for useless piece of crap: ").lower()
    types = ['w', 's', 't', 'u']
    if inv_type in types:
        name_check(inv_type)
    else:
        return

def overwrite(item_name):
    print("overwriting!")


def name_check(type):
    """This function takes an argument of item type (w, s, t, u) and prompts the user to input the item name.
    This check the name against the current inventory, and if it already exists, asks the user if they would
    like to overwrite the item information"""
    name = input("What is the name of your object/spell?:")

    #Check name in current inventory
    for val in my_inventory:
        if val["name"] == name:
            overwrite_choice = input("This name is already in use. Would you like to overwrite? (yes/no): ").lower()
            if overwrite_choice == 'yes':
                overwrite(name)
            elif overwrite_choice == 'no':
                retry = input("Would you like to enter another name? (yes/no): ").lower()
                if retry =='no':
                    return
                else:
                    name_check(type)
            else:
                return
    add_new_item(name, type)

def add_new_item(name, type):
    """This function takes the item name and type as parameters and adds the item to the inventory based on attack
    items (weapons/spells) or objects (treasure/junk)."""
    if type == 'w' or type == 's':
        damage = input("How much damage does this do?: ")
        dam_range = input("What is the range?: ")
        new_item = {'name' : name, 'type' : type, 'damage': damage, 'range' : dam_range, 'description': None}
    else:
        description = input("Enter a brief description: ")
        new_item = {'name' : name, 'type' : type, 'damage': None, 'range' : None, 'description': description}
    print(my_inventory)
    my_inventory.append(new_item)
    print(my_inventory)


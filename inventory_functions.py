import csv


# my_inventory = [{'name': 'trident', 'type': 'weapon', 'damage': '3d6', 'range': 'melee', 'description' : None},
#                {'name': 'shocking grasp', 'type': 'spell', 'damage': '1d8', 'range': 'touch', 'description': None}, ]
#
# with open('inventory.csv', 'w', newline='') as csvfile:
#     fieldnames = ['name', 'type', 'damage', 'range', 'description']
#     writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
#     writer.writeheader()
#     writer.writerows(my_inventory)

#f
def read_inv():
    inv = []
    with open('inventory.csv', 'r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            inv.append(row['name'])
    return inv


def is_inventory_empty():
    file_size = len('inventory.csv')
    if file_size == 0:
        return True
    else:
        return False


def name_exists(name):
    my_inventory = read_inv()
    for val in my_inventory:
        if val == name:
            return True
        else:
            return False


def overwrite(name):
    print("overwriting")


def view_item(name):
    my_inventory = read_inv()
    for index, entry in enumerate(my_inventory):
        if entry['name'] == name:
            for key in entry:
                value = str(entry[key])
                print(key.title(), ':', value.title())


def view_inventory():
    my_inventory = read_inv()
    for index, entry in enumerate(my_inventory):
        print(index+1, entry['name'].title())


def name_check():
    with open('inventory.json', 'r') as infile:
        my_inventory = json.load(infile)
    name = input("Please enter the name of your object/spell: ").lower()
    for val in my_inventory:
        if val["name"] == name:
            overwrite_choice = input("This name is already in use. Would you like to overwrite? (yes/no): ").lower()
            if overwrite_choice == 'yes':
                print("overwriting!")
            elif overwrite_choice == 'no':
                retry = input("Would you like to enter another name? (yes/no): ").lower()
                if retry =='no':
                    return
                else:
                    name_check()
            else:
                return
    add_new_item(name)


def object_type():
    """This function prompts the user to determine a 'type' for their object, which determines which attributes it has"""
    print("What kind item would you like to store?")
    inv_type = input(" Type 'w' for weapon\n Type 's' for spell\n Type 't' for treasure\n "
                     "Or type 'u' for useless piece of crap: ").lower()
    types = ['w', 's', 't', 'u']
    if inv_type in types:
        return inv_type

#
# def add_new_item(name):
#     """This function takes the item name and type as parameters and adds the item to the inventory based on attack
#     items (weapons/spells) or objects (treasure/junk)."""
#     ob_type = object_type()
#     if ob_type == 'w' or ob_type == 's':
#         damage = input("How much damage does this do?: ")
#         dam_range = input("What is the range?: ")
#         new_item = {'name' : name, 'type' : type, 'damage': damage, 'range' : dam_range, 'description': None}
#     else:
#         description = input("Enter a brief description: ")
#         new_item = {'name' : name, 'type' : type, 'damage': None, 'range' : None, 'description': description}
#
#     with open('inventory.json', 'r') as f:
#         current_inv = json.load(f)
#     print(current_inv.update(new_item))
#     # with open('inventory.json', 'w') as f:
#     #     json.dump(current_inv, f)


def choose_action():
    correct_response = False
    while correct_response is False:
        print("What would you like to do?\n - Type 's' to store an item,\n - Type 'r' to retrieve an item,\n "
                           "- Type 'i' to view a list of inventory,\n - Or type 'x' to exit\n")
        user_input = input("I would like to: ").lower()
        options = ['s', 'r', 'i', 'x']
        if user_input in options:
            correct_response = True
            return user_input
        else:
            print("That is not an option, please try again\n")






# def store():
#     """This function prompts user to select item type (weapon, spell, treasure, junk) and, if a valid option is chosen,
#      calls the name check function to see if the item already exists in the inventory"""
#     print("What would you like to store?")
#     inv_type = input(" Type 'w' for weapon\n Type 's' for spell\n Type 't' for treasure\n "
#                      "Or type 'u' for useless piece of crap: ").lower()
#     types = ['w', 's', 't', 'u']
#     if inv_type in types:
#         name_check(inv_type)
#     else:
#         return
#
#
# def overwrite(item_name):
#     print("overwriting!")
#
#
# def name_check(type):
#     """This function takes an argument of item type (w, s, t, u) and prompts the user to input the item name.
#     This check the name against the current inventory, and if it already exists, asks the user if they would
#     like to overwrite the item information"""
#     name = input("What is the name of your object/spell?:")
#
#     #Check name in current inventory
#     for val in my_inventory:
#         if val["name"] == name:
#             overwrite_choice = input("This name is already in use. Would you like to overwrite? (yes/no): ").lower()
#             if overwrite_choice == 'yes':
#                 overwrite(name)
#             elif overwrite_choice == 'no':
#                 retry = input("Would you like to enter another name? (yes/no): ").lower()
#                 if retry =='no':
#                     return
#                 else:
#                     name_check(type)
#             else:
#                 return
#     add_new_item(name, type)
#


